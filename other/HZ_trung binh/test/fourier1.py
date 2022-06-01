from scipy.io import wavfile
import glob
from scipy.fftpack import fft,fftfreq
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
import pylab
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import librosa    
import glob


signal, sample_rate = librosa.load("./quạt điện 4.wav", sr = 22050)

# biến đổi Fourier transform
fft = np.fft.fft(signal)
# tính toán các giá trị trung bình trên các số phức để có được độ lớn
spectrum = np.abs(fft)
# biến tần số f
f = np.linspace(0, sample_rate, len(spectrum))
# lấy 1 nửa
left_spectrum = spectrum[:int(len(spectrum)/2)]
left_f = f[:int(len(spectrum)/2)]
max = 0
for i in left_spectrum:
    if max < i:
        max = i
print('TB:')
print(sum(left_spectrum) / len(left_spectrum))
print(max)
plt.plot(left_f, left_spectrum, alpha=0.4)
# plt.plot(f, spectrum, alpha=0.4)
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.title('Power spectrum')
plt.show()