### % phần trăm khoảng lặng 0,1
### độ lệch năng lượng 0,3
### pitch 0,3
### tần số có mật độ lớn nhất 0,3
from attribute import toolInstrumentVoice

configPercentSilence = 0.1
configRMSE = 0.3
configPitch = 0.3
configPercentSilence = 0.3

def compareFile(att1, att2): 
    maxRes = 0
    for i in range(7):
        for j in range(7):
            # giongnhau
            same = float(abs(att1[i].percentSilence - att2[j].percentSilence) / max(att1[i].percentSilence, att2[j].percentSilence) * configPercentSilence)
            same = same + float(abs(att1[i].RMSE - att2[j].RMSE) / max(att1[i].RMSE, att2[j].RMSE) * configRMSE)
            same = same + float(abs(att1[i].pitch - att2[j].pitch) / max(att1[i].pitch, att2[j].pitch) * configPitch)
            same = same + float(abs(att1[i].frequencyMagnitude - att2[j].frequencyMagnitude) / max(att1[i].frequencyMagnitude, att2[j].frequencyMagnitude) * configPercentSilence)
            if(maxRes < same):
                maxRes = same
    
    return maxRes
    
# input
att1 = [] 
# for i in range(7):
att1.append(toolInstrumentVoice(54.6511, 138, 32, 520))
att1.append(toolInstrumentVoice(61.7545, 116.8, 33, 815))
att1.append(toolInstrumentVoice(58.1165, 72, 33.5, 1500))
att1.append(toolInstrumentVoice(49.8548, 107.7, 34, 2255))
att1.append(toolInstrumentVoice(53.3301, 120, 35, 2556))
att1.append(toolInstrumentVoice(57.3430, 95, 35.6, 2867))
att1.append(toolInstrumentVoice(62.4325, 91, 37, 520))

# có sẵn
att2 = []
att2.append(toolInstrumentVoice(40, 144, 2, 550))
att2.append(toolInstrumentVoice(41.7545, 123, 3, 315))
att2.append(toolInstrumentVoice(42.1165, 98, 5, 150))
att2.append(toolInstrumentVoice(43.8548, 84, 4, 225))
att2.append(toolInstrumentVoice(44.3301, 115, 10, 280))
att2.append(toolInstrumentVoice(45.3430, 93, 15, 267))
att2.append(toolInstrumentVoice(46.4325, 97, 17, 820))

print(compareFile(att1, att2))