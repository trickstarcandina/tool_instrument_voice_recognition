import librosa
import librosa.display
from matplotlib import pyplot as plt
import numpy as np
import scipy

def fft_plot(audio, sampling_rate):
    n = len(audio)
    T = 1/sampling_rate
    yf = scipy.fft.fft(audio) #.ifft
    xf = np.linspace(0.0, 1.0/(100.0*T), int(n/2))
    fig, ax = plt.subplots()
    ax.plot(xf, 2.0/n * np.abs(yf[:n//2]))
    plt.grid()
    plt.xlabel("Frequency -->")
    plt.ylabel("Magnitude")
    return plt.show()

samples, sampling_rate = librosa.load('./quạt điện 4.wav',
sr = None, mono = True, offset = 0.0, duration = None)
 
print(len(samples) / sampling_rate)

fft_plot(samples, sampling_rate)

#####

# plt.figure()
# librosa.display.waveshow(y = samples, sr = sampling_rate)
# plt.xlabel("Time -->")
# plt.ylabel("Amp")
# plt.show()

######

# samples = 100
# f = 3
# x = np.arange(samples)
# y1 = np.sin(2*np.pi*f * (x/samples))

# plt.figure()
# plt.stem(x,y1, 'r', )
# plt.plot(x,y1)
# plt.xlabel("Time -->")
# plt.ylabel("Amp")

####

# samples = 100
# f = 11
# x = np.arange(samples)
# y2 = 2 * np.sin(2*np.pi*f * (x/samples))
# y3 = y1 + y2
# plt.figure()
# plt.stem(x,y3, 'r', )
# plt.plot(x,y3)
# plt.xlabel("Time -->")
# plt.ylabel("Amp")
# plt.show()

