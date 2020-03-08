import threading
import time
import subprocess
import asyncio

import psutil

from utils.singleton import Singleton


class PlayerManager(object, metaclass=Singleton):
    """
    Class to play music with mplayer
    """
    MPLAYER_EXEC_PATH = "/usr/bin/mplayer"

    def threaded_start(self, url):
        """
        The player manager need to be executed in a thread.
        Use this method to create a thread if the called is not already a thread like the scheduler manager
        """
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        main_thread = threading.Thread(target=self.async_start, args=[loop, url])
        main_thread.start()

    def async_start(self, loop, url, auto_stop_minutes=0, backup_file_path=None):
        seconds = auto_stop_minutes * 60    # need to convert in seconds
        loop.run_until_complete(self.main_loop(url, seconds, backup_file_path))

    async def main_loop(self, url, auto_stop_seconds, backup_file_path, second_to_wait_before_check=35):
        print(f"started at {time.strftime('%X')}")
        # Create an Event object
        event = asyncio.Event()

        start_player_task = asyncio.create_task(
            self.start_player_task(url))
        check_player_alive_task = asyncio.create_task(
            self.check_player_task(event, second_to_wait_before_check, backup_file_path))
        auto_stop_task = asyncio.create_task(
            self.auto_kill_player_task(event, seconds=auto_stop_seconds))

        await start_player_task
        await check_player_alive_task
        await auto_stop_task

        print(f"finished at {time.strftime('%X')}")

    async def start_player_task(self, url):
        print("starting player with URL {}".format(url))
        command = "/usr/bin/mplayer {}".format(url)
        await self.run_command(command)
        print("Player stopped")

    async def check_player_task(self, event, seconds, backup_file_path):
        if backup_file_path is not None:
            print("Wait '{}' seconds before checking player process...".format(seconds))
            await asyncio.sleep(seconds)
            if not event.is_set():
                print("Checking if player process is alive")
                if self.is_started():
                    print("Player is alive")
                else:
                    print("Player not alive")
                    event.set()  # notify auto kill method to not execute the stop
                    await self.run_backup_file(backup_file_path)
                    return False
            else:
                print("Player already stopped. Do not need to check")
        return True

    async def auto_kill_player_task(self, event, seconds=0):
        """
        return true when the player has been stopped
        """
        if seconds > 0:
            print("Wait '{}' seconds before auto stopping player...".format(seconds))
            await asyncio.sleep(seconds)
            if not event.is_set():
                print("Timer exceeded. Killing player")
                command = "killall mplayer"
                await self.run_command(command)
                print("Player killed")
                event.set()
                return True
            else:
                print("Player already stopped. Do not run auto stop")
        return False

    async def run_backup_file(self, file_path):
        print("Running backup MP3 file '{file_path}'")
        command = "/usr/bin/mplayer {}".format(file_path)
        await self.run_command(command)

    async def run_command(self, command):
        """
        Run command in subprocess.

        Example from:
            http://asyncio.readthedocs.io/en/latest/subprocess.html
        """
        # Create subprocess
        process = await asyncio.create_subprocess_shell(
            command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )

        # Status
        print("Started: '%s', pid: '%s'" % (command, process.pid), flush=True)

        # Wait for the subprocess to finish
        stdout, stderr = await process.communicate()

        # Progress
        if process.returncode == 0:
            print(
                "Done: %s, pid=%s, result: %s"
                % (command, process.pid, stdout.decode().strip()),
                flush=True,
            )
        else:
            print(
                "Failed: %s, pid=%s, result: %s"
                % (command, process.pid, stderr.decode().strip()),
                flush=True,
            )

        # Result
        result = stdout.decode().strip()

        # Return stdout and return code
        return result, process.returncode

    @staticmethod
    def stop():
        """
        Kill mplayer process
        """
        p = subprocess.Popen("killall mplayer", shell=True)
        p.communicate()

    @staticmethod
    def is_started():
        process_name = "mplayer"
        # Iterate over the all the running process
        for proc in psutil.process_iter():
            try:
                # Check if process name contains the given name string.
                if process_name.lower() in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False
