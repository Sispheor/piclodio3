
import alsaaudio


class SoundManager(object):

    @staticmethod
    def _get_mixer():
        try:
            mixer = alsaaudio.Mixer()
        except alsaaudio.ALSAAudioError:
            # no master, we are on a Rpi
            mixer = alsaaudio.Mixer("PCM")
        return mixer

    @classmethod
    def set_volume(cls, volume_level):
        cls._get_mixer().setvolume(int(volume_level))

    @classmethod
    def get_volume(cls):
        vol = cls._get_mixer().getvolume()
        return int(vol[0])
