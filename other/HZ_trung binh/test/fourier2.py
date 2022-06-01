import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

#frame size
#hop length = frame increment

y, sr = librosa.load('./2.wav')
n_fft = 2048
# ft = np.abs(librosa.stft(y[:n_fft], hop_length = n_fft+1)) 
# plt.plot(ft);

ft = np.abs(librosa.stft(y, n_fft=n_fft,  hop_length=512))
librosa.display.specshow(ft, sr=sr, x_axis='time', y_axis='linear');
plt.colorbar();
# ft_dB = librosa.amplitude_to_db(ft, ref=np.max)
# librosa.display.specshow(ft_dB, sr=sr, hop_length=512, x_axis='time', y_axis='log');
# plt.colorbar(format='%+2.0f dB');

plt.show()