import librosa
import librosa.display
from matplotlib import pyplot as plt
import numpy as np

x, sampling_rate = librosa.load('./máy phát điện 1.wav')
# print('Sampling Rate: ', sampling_rate)
# plt.figure(figsize=(14, 5))
# plt.plot(x[:sampling_rate * 5])
# plt.title('Plot for the first 5 seconds')
# plt.xlabel('Frame number')
# plt.ylabel('Magnitude')
# plt.show()

D = librosa.stft(x)
D_left = librosa.stft(x, center=False)
D_short = librosa.stft(x, hop_length=64)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(D)), y_axis='log', x_axis='time')
plt.title('Power spectrogram')
plt.colorbar(format='%+2.0f dB')
plt.tight_layout()
plt.show()

# x, sr = librosa.load('./máy phát điện 1.wav')
# hop_length = 512
# n_fft = 2048
# X = librosa.stft(x, n_fft=n_fft, hop_length=hop_length)
# S = librosa.amplitude_to_db(abs(X))
# plt.figure(figsize=(15, 5))
# librosa.display.specshow(S, sr=sr, hop_length=hop_length, x_axis='time', y_axis='linear')
# plt.colorbar(format='%+2.0f dB')
# plt.show()