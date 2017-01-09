import alsaaudio


class SoundManager(object):

    m = alsaaudio.Mixer()

    @classmethod
    def set_volume(cls, volume_level):
        cls.m.setvolume(int(volume_level))

    @classmethod
    def get_volume(cls):
        vol = cls.m.getvolume()
        return int(vol[0])
