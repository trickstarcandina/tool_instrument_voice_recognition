import librosa.display
import matplotlib.pyplot as plt


def Find_Max(arr, f, l):
    """
    :param arr: list of integer
    :return: item max of list
    """
    max = arr[f]

    for i in range(f, l):
        if max < arr[i]:
            max = arr[i]

    return max


def Find_Min(arr, f, l):
    """
    :param arr: list of integer
    :return: item max of list
    """
    min = arr[f]

    for i in range(f, l):
        if min > arr[i]:
            min = arr[i]

    return min


def KhoangLang(arr, f, l):
    max = Find_Max(arr, f, l)
    min = Find_Min(arr, f, l)
    tb = (max + min) / 2
    nguong = tb * 0.3
    dem = 0
    for i in range(f, l):
        if arr[i] > nguong:
            dem = dem + 1

    return 100 - (dem / (l - f)) * 100


# plt.figure(figsize=(5, 5))
# path = "E:/Learn/tool_instrument_voice_recognition/src/File âm thanh/1 máy sấy tóc/may_say_toc_1.wav"
def funcPercentSilence(path):
    y, sr = librosa.load(path)  # y la bien do theo thoi gian, sr tan so lay mau
    # print(librosa.feature.mfcc(y=y, sr=sr).shape)
    # print("khoang lang theo 1 s:")
    result = []
    for i in range(0, 6):
        # print("thoi gian: ", i, " = ",KhoangLang(y, i*sr, (i+1)*sr))
        result.append(KhoangLang(y, i * sr, (i + 1) * sr))
    result.append(KhoangLang(y, 6, len(y)))
    return result


print(
    funcPercentSilence("E:/Learn/tool_instrument_voice_recognition/src/File âm thanh/1 máy sấy tóc/may_say_toc_1.wav"))
