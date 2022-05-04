import librosa
import librosa.display
import numpy
from scipy import signal
import matplotlib.pyplot as plt

y, sr = librosa.load('./máy phát điện 1.wav')
# y, sr = librosa.load('./2.wav')

stft = librosa.stft(y, n_fft=256, window=signal.windows.hamming)
spec = numpy.abs(stft)
librosa.display.specshow(spec, sr=sr, x_axis='time', y_axis='linear')
plt.colorbar();
plt.show()

# n_fft = 1024
# hop_length = 512

# spec = numpy.abs(librosa.core.stft(y, n_fft=n_fft, hop_length=hop_length))
# freqs = librosa.core.fft_frequencies(n_fft=n_fft)
# times = librosa.core.frames_to_time(spec[0], sr=sr, n_fft=n_fft, hop_length=hop_length)

# print('spectrogram size', spec.shape)

# fft_bin = 140
# time_idx = 307

# print('freq (Hz)', freqs[fft_bin])
# print('time (s)', times)
# print('amplitude', spec[fft_bin, time_idx])
# print(numpy.matrix(spec))