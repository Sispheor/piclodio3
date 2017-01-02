import subprocess
import re

import logging

logger = logging.getLogger("piclodio")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
# add the handlers to logger
logger.addHandler(ch)


class CrontabManager(object):
    """
    Crontab class.
    Allow to create, remove, disable an enable a Linux crontab line
    """

    COMMENT = "piclodio"
    TMP_FILE = "/tmp/new_newcron.txt"

    @classmethod
    def get_current_crontab(cls):
        """
        Return a dict of current crontab
        """
        # get current crontab
        p = subprocess.Popen("crontab -l", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        mycron = str(output)
        mycron = mycron.splitlines()
        logger.debug("Current crontab line: %s" % str(mycron))
        return mycron

    @classmethod
    def add_job(cls, job):
        """
        Add a new job to the crontab
        :param job: a cron line. E.g: 0 7 * * * echo test # piclodio 1
        :return:
        """
        # get the current crontab
        current_crontab = cls.get_current_crontab()
        current_crontab.append(job)
        cls._write_in_file(current_crontab)
        cls._save_crontab()

    @classmethod
    def disable_job(cls, comment):
        """
        Disable a job by commenting the line in the crontab
        :param comment: The comment to look for to identify the line to comment out
        :return:
        """
        # get the current cron
        current_crontab = cls.get_current_crontab()
        # boolean to kown if the current crontab has been changed
        changed = False
        # prepare a new crontab list of job
        new_crontab = list()

        for line in current_crontab:
            if comment in line and cls._is_job_enable(line):
                commented_line = "# " + line
                new_crontab.append(commented_line)
                changed = True
            else:
                new_crontab.append(line)

        if changed:
            cls._write_in_file(new_crontab)
            cls._save_crontab()

    @classmethod
    def enable_job(cls, comment):
        """
        Enable a job by uncommenting the line in the crontab
        :param comment: The comment to look for to identify the line to activate
        :return:
        """
        # get the current cron
        current_crontab = cls.get_current_crontab()
        # boolean to kown if the current crontab has been changed
        changed = False
        # prepare a new crontab list of job
        new_crontab = list()

        for line in current_crontab:
            if comment in line and not cls._is_job_enable(line):
                index_comment = line.index('#')
                line_without_comment = line[index_comment + 2:len(line)]
                new_crontab.append(line_without_comment)
                changed = True
            else:
                new_crontab.append(line)
        if changed:
            cls._write_in_file(new_crontab)
            cls._save_crontab()

    @classmethod
    def remove_job(cls, comment):
        """
        Delete a job from the crontab by its comment
        :param comment:The comment to look for to identify the line to delete
        :return:
        """
        # get the current cron
        current_crontab = cls.get_current_crontab()
        # boolean to kown if the current crontab has been changed
        changed = False
        # prepare a new crontab list of job
        new_crontab = list()

        for line in current_crontab:
            if comment in line:
                changed = True
            else:
                new_crontab.append(line)
        if changed:
            cls._write_in_file(new_crontab)
            cls._save_crontab()

    @classmethod
    def _is_job_enable(cls, line):
        """
        return True is the job is active in the crontab.
        Active means the line is not commented out
        :param line:
        :return: True if the job is active
        """
        regex = re.compile("^#")
        test = regex.match(line)
        if test:
            return False    # is disable
        return True

    @classmethod
    def _save_crontab(cls):
        """
        save the crontab with the content of the TMP_FILE
        :return:
        """
        # save the crontab from the temp file
        p = subprocess.Popen("crontab %s" % cls.TMP_FILE, stdout=subprocess.PIPE, shell=True)
        p.communicate()

    @classmethod
    def _write_in_file(cls, new_crontab):
        """
        write a new crontab in the temp file
        :param new_crontab: dict of jobs
        :return:
        """
        f = open(cls.TMP_FILE, "w")
        for job_line in new_crontab:
            f.write(job_line)
            f.write('\n')
        f.close()
        logger.debug("saving new crontab in tmp file: %s" % str(new_crontab))
