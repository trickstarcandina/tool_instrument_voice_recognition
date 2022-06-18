from re import A


class toolInstrumentVoice:
    def __init__(self, a, b, c, d, e):
        self.pitch = a
        self.RMSE = b
        self.percentSilence = c
        self.magnitude = d
        self.frequency = e