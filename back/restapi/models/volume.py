from utils.sound_manager import SoundManager


class Volume(object):

    def __init__(self):
        self.volume = SoundManager.get_volume()
