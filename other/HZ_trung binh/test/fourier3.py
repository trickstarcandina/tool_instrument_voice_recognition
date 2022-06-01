import librosa
import numpy as np
import matplotlib.pyplot as plt


file = "./máy phát điện 1.wav"
# load the file
y, sr = librosa.load(file, sr=44100)
# short time fourier transform
# (n_fft and hop length determine frequency/time resolution)
n_fft = 2048
S = librosa.stft(y, n_fft=n_fft, hop_length=n_fft//2)
# convert to db
# (for your CNN you might want to skip this and rather ensure zero mean and unit variance)
D = librosa.amplitude_to_db(np.abs(S), ref=np.max)
# average over file
D_AVG = np.mean(D, axis=1)

plt.bar(np.arange(D_AVG.shape[0]), D_AVG)
x_ticks_positions = [n for n in range(0, n_fft // 2, n_fft // 16)]
x_ticks_labels = [str(sr / 2048 * n) + 'Hz' for n in x_ticks_positions]
plt.xticks(x_ticks_positions, x_ticks_labels)
plt.xlabel('Frequency')
plt.ylabel('dB')
plt.show()