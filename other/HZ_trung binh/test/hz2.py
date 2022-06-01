import numpy as np
import librosa

y, sr = librosa.load('./2.wav')
# Fs = 16384
n_fft = 256
freqs = np.arange(0, 1 + n_fft / 2) * sr / n_fft
print(freqs)