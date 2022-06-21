import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
import IPython.display as ipd

# 700 phần tử. mỗi 1s có 100 p.tử
# giá trị đầu tiên bằng trung bình của 100 phần tử

def funcRMSE(tool1_file):
    # tool1_file = "E:/Learn/tool_instrument_voice_recognition/src/File âm thanh/1 máy sấy tóc/may_say_toc_1.wav"
    #tool1_file = "C:\\Users\\Minh\\Desktop\\Audio_Attr\\inputWav/y2mate.com-Somebody-I-Used-To-Know-Studio-Acapella-Vocal-Only-Track.wav"
    tool1, sr = librosa.load(tool1_file, duration = 7)
    #tool1, sr = librosa.load(tool1_file, duration = 7, offset=32)
    FRAME_SIZE = 1024
    HOP_LENGTH = 512
    rms = librosa.feature.rms(tool1, frame_length=FRAME_SIZE, hop_length=HOP_LENGTH)[0]

    arr = np.array_split(rms, 7)

    result = []
    result = [0 for i in range(7)] 
    window = 0

    #-----------------------Difference Percentage------------
    for i in range(len(arr)):
        sum = 0
        count = 0
        for j in range(len(arr[i])-1):  
            if(arr[i][j] != 0):  
                sum += ((abs(arr[i][j] - arr[i][j+1]))/arr[i][j])*100
            else:
                sum += 0
            # print(sum)
            count += 1
        avg = sum/count
        result[window] = avg
        window += 1
    return result

#----------------------Average Window-------------------- 
# for i in range(len(arr)):
#     sum = 0
#     count = 0
#     for j in range(len(arr[i])):  
#         sum += arr[i][j]
#         count += 1
#     avg = sum/count
#     result[window] = avg
#     window += 1  

# print(funcRMSE("E:/Learn/tool_instrument_voice_recognition/src/File âm thanh/1 máy sấy tóc/may_say_toc_1.wav"))