import os
import subprocess
import threading
from time import sleep


class PlayerManager(object):
    """
    Class to play music with mplayer
    """
    MPLAYER_EXEC_PATH = "/usr/bin/mplayer"

    @classmethod
    def play(cls, url, blocking_thread=False):
        # kill process if already running
        if cls.is_started():
            cls.stop()
        mplayer_exec_path = [cls.MPLAYER_EXEC_PATH]
        mplayer_options = ['-slave', '-quiet']
        mplayer_command = list()
        mplayer_command.extend(mplayer_exec_path)
        mplayer_command.extend(mplayer_options)

        mplayer_command.extend([url])
        print("Mplayer cmd: %s" % str(mplayer_command))

        if blocking_thread:
            # blocking thread
            p = subprocess.Popen(mplayer_command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p.communicate()
            # the following line will only be printed when the process mplayer will be killed
            print "Mplayer stopped"
        else:
            fnull = open(os.devnull, 'w')
            subprocess.Popen(mplayer_command, stdout=fnull, stderr=fnull)

    @classmethod
    def stop(cls):
        """
        Kill mplayer process
        """
        p = subprocess.Popen("killall mplayer", shell=True)
        p.communicate()

    @classmethod
    def is_started(cls):
        # check number of process
        p = subprocess.Popen("pgrep mplayer", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output == "":
            return False
        else:
            return True


class ThreadTimeout(object):
    def __init__(self, callback_instance, backup_instance, timeout):
        self.callback_instance = callback_instance
        self.backup_instance = backup_instance
        self.timeout = timeout
        self.main_thread = None

    def run(self):
        def target():
            print 'Thread started'
            self.callback_instance.start()
            print 'Thread finished'

        def waiting_target():
            print "Wait %s seconds before checking if the thread is alive" % self.timeout
            sleep(self.timeout)
            if self.main_thread.is_alive():
                print 'Thread is alive'
                # thread.join()
            else:
                print 'Thread is dead'
                if self.backup_instance is not None:
                    print "Playing backup file"
                    self.backup_instance.start()
                else:
                    print "Not backup file provided"

        # start a thread to play the webradio
        self.main_thread = threading.Thread(target=target)
        self.main_thread.start()

        # start a thread that will check that the first thread is alive
        thread_waiting = threading.Thread(target=waiting_target)
        thread_waiting.start()


class CallbackPlayer(object):
    def __init__(self, url=None):
        self.url = url

    def start(self):
        PlayerManager.play(self.url, blocking_thread=True)
