import inspect
import os


# command = "python run_web_radio.py 7 1"
# os.system(command)

import alsaaudio


m = alsaaudio.Mixer()

vol = m.getvolume()

print vol

m.setvolume(20)
vol = m.getvolume()
print vol