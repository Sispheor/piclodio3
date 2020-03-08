from time import strftime


class Clock(object):

    def __init__(self):
        self.clock = strftime("%Y-%m-%dT%H:%M:%S")
