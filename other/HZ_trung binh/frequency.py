import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import *
from scipy.io import wavfile

def freq(file, start_time, end_time):  # HZ trung binh
    # Open the file and convert to mono
    sr, data = wavfile.read(file)
    if data.ndim > 1:
        data = data[:, 0]
    else:
        pass

    dataToRead = data[int(start_time * sr / 1000): int(end_time * sr / 1000) + 1]

    # Fourier Transform
    N = len(dataToRead)
    yf = rfft(dataToRead)
    xf = rfftfreq(N, 1 / sr)

    plt.plot(xf, np.abs(yf))
    plt.show()

    # Get the most dominant frequency and return it
    idx = np.argmax(np.abs(yf))
    hz = xf[idx]
    return hz

print("hz tb: ", freq('./máy bơm 2.wav', 0, 7000))
print("hz tb: ", freq('./máy phát điện 1.wav', 0, 7000))
print("hz tb: ", freq('./quạt điện 4.wav', 0, 7000))
print("hz tb: ", freq('./cua_dien_1.wav', 0, 7000))
print("hz tb: ", freq('./khoan_dien_1.wav', 0, 7000))
print("hz tb: ", freq('./may_cat_co_2.wav', 0, 7000))
print("hz tb: ", freq('./may_say_toc_1.wav', 0, 7000))