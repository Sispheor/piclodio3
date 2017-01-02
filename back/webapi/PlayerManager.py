import os
import subprocess


class PlayerManager(object):
    """
    Class to play music with mplayer
    """
    MPLAYER_EXEC_PATH = "/usr/bin/mplayer"

    @classmethod
    def play(cls, url):
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
