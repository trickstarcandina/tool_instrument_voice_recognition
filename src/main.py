from Pitch import funcPitch
from aubio import pitch
from RMSE import funcRMSE
from PercentSilence import funcPercentSilence
from FrequencyMagnitude import funcFrequencyMagnitude


# >>> pairs = [("a", 1), ("b", 2), ("c", 3)]
# >>> for a, b in pairs:
# ...    print a, b
# ... 
# a 1
# b 2
# c 3

path = "E:/Learn/tool_instrument_voice_recognition/src/File âm thanh/1 máy sấy tóc/may_say_toc_1.wav";

# print('=====Pitch=====')
# print(funcPitch(path, pitch))
# print('=====RMSE=====')
# print(funcRMSE(path))
# print('=====PercentSilence=====')
# print(funcPercentSilence(path))
# print('=====FrequencyMagnitude=====')
# print(funcFrequencyMagnitude(path))
######################################################
import csv

with open('src/CSDLDPT.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    header = ['Path', 'Pitch', 'RMSE', 'PercentSilence', 'FrequencyMagnitude']
    writer.writerow(header)
    data = [
        path, 
        funcPitch(path, pitch), 
        funcRMSE(path), 
        funcPercentSilence(path), 
        funcFrequencyMagnitude(path)
    ]
    writer.writerow(data)
