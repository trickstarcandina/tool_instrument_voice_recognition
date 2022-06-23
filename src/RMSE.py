import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
import IPython.display as ipd

# 700 phần tử. mỗi 1s có 100 p.tử
# giá trị đầu tiên bằng trung bình của 100 phần tử

# 

def funcRMSE(tool1_file):
    # tool1_file = "E:/Learn/tool_instrument_voice_recognition/src/File âm thanh/1 máy sấy tóc/may_say_toc_1.wav"
    #tool1_file = "C:\\Users\\Minh\\Desktop\\Audio_Attr\\inputWav/y2mate.com-Somebody-I-Used-To-Know-Studio-Acapella-Vocal-Only-Track.wav"
    tool1, sr = librosa.load(tool1_file, duration = 7)
    #tool1, sr = librosa.load(tool1_file, duration = 7, offset=32)
    FRAME_SIZE = 1024
    HOP_LENGTH = 512
    rms = librosa.feature.rms(tool1, frame_length=FRAME_SIZE, hop_length=HOP_LENGTH)[0] #RMS là mảng năng lượng trung bình mặc định mà Librosa trả về

    arr = np.array_split(rms, 7) #Mảng arr là mảng 7 phần tử, mỗi phần tử là đoạn 1/7 cua rms được split ra

    result = []
    result = [0 for i in range(7)] 
    window = 0

    #-----------------------Difference Percentage------------
    for i in range(len(arr)):
        sum = 0
        count = 0
        for j in range(len(arr[i])-1):  
            if(arr[i][j] != 0):  
                sum += ((abs(arr[i][j] - arr[i][j+1]))/arr[i][j])*100 #TBC hiệu 2 giá trị cạnh nhau / giá trị tiếp theo để tính xem 
                                                                        #năng lượng trung bình ở giá trị tiếp theo lệch bn % so với giá trị hiện tại
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