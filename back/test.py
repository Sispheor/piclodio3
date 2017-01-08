import inspect
import os


# command = "python run_web_radio.py 7 1"
# os.system(command)


def get_root_path(current_script_path):
    """
    Return the root path of the
    :param current_script_path:
    :return:
    """
    parent_path = os.path.normpath(current_script_path + os.sep + os.pardir)
    return parent_path


current_script_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print current_script_path
print get_root_path(current_script_path)