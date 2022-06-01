import os
import matplotlib.pyplot as plt
import librosa, librosa.display
import IPython.display as ipd
import numpy as np

def funcFrequencyMagnitude(audio_dir):
    # audio_dir = "E:/Learn/tool_instrument_voice_recognition/src/File âm thanh/1 máy sấy tóc/may_say_toc_1.wav"
    audio, sr = librosa.load(audio_dir, duration = 7)
    X = np.fft.fft(audio)
    X_mag = np.absolute(X)

    f = np.linspace(0, sr, len(X_mag))
    f_bins = int(len(X_mag))  

    #print(f)
    ################################################3 print(X_mag.size)
    #plt.plot(f[:f_bins], X_mag[:f_bins])
    f[:f_bins], X_mag[:f_bins]

    #print(f)
    #print(X_mag)
    #print(f.size)
    #print(f_bins)
    freq =[] #Freq là mảng ghi tần số có mức độ xuất hiện lớn nhất
    freq = [0 for i in range(7)]

    magnitude =[] #Magnitude là cụ thể mức độ xuất hiện là bao nhiêu
    magnitude = [0 for i in range(7)]

    position = 0
    max = 0
    pos = 0

    for i in range(0, len(X_mag)):        
        if(X_mag[i] > max):
            max = X_mag[i]
            pos = i
        if(i> 0):
            if( (i % int(len(X_mag)/7)) == 0 and i != len(X_mag)-1):            
                freq[position] = pos
                magnitude[position] = max
                #print('Position value at checkpoint: ' + str(position))
                position += 1
                max = 0
            if(i == len(X_mag)-1):            
                freq[position] = pos
                magnitude[position] = max
                #print('Position value at checkpoint: ' + str(position))  

        
    pairs = list(zip(freq, magnitude))
    # print(freq) 
    # print(magnitude)  
    return pairs


# test
print(funcFrequencyMagnitude("E:/Learn/tool_instrument_voice_recognition/src/File âm thanh/1 máy sấy tóc/may_say_toc_1.wav"))