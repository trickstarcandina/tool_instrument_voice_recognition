import sys
import numpy as np
from aubio import source, pitch

win_s = 4096
hop_s = 512 

samplerate = 44100
s = source('./máy phát điện 1.wav', samplerate, hop_s)
samplerate = s.samplerate

tolerance = 0.8

pitch_o = pitch("yin", win_s, hop_s, samplerate)
pitch_o.set_unit("midi")
pitch_o.set_tolerance(tolerance)

pitches = []
confidences = []

total_frames = 0
while True:
    samples, read = s()
    pitch = pitch_o(samples)[0]
    pitches += [pitch]
    confidence = pitch_o.get_confidence()
    confidences += [confidence]
    total_frames += read
    if read < hop_s: break

print("Average frequency = " + str(np.array(pitches).mean()) + " hz")