# coding: utf8
import os


TIANGAN = ('甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸')
DIZHI = ('子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥')


def converter(year):
    """公元转干支转换器"""
    # 天干计算
    tianGanModedNumber = (year - 3) % 10
    if tianGanModedNumber != 0:
        tianGanOrderNumber = tianGanModedNumber - 1
    else:
        tianGanOrderNumber = 9
    tianGan = TIANGAN[tianGanOrderNumber]

    # 地支计算
    diZhiModedNumber = (year - 3) % 12
    if diZhiModedNumber != 0:
        diZhiOrderNumber = diZhiModedNumber - 1
    else:
        diZhiOrderNumber = 11
    diZhi = DIZHI[diZhiOrderNumber]

    return f'{tianGan}{diZhi}'


def inputer():
    """输入检查器"""
    inputText = input('请输入公元年：')

    # 判断是否为数字
    try:
        inputNumber = int(inputText)
    except ValueError as identifier:
        print(f'程序错误，原因:"{identifier}"')
        os._exit(1001)
    
    # 判断是否为正数
    if inputNumber > 0:
        ccbText = converter(inputNumber)
    else:
        print('请输入一个大于0的整数!')
        os._exit(1002)
    
    return inputNumber, ccbText


def main():
    """主程序"""
    returnList = inputer()
    print(f'{returnList[0]}年是{returnList[1]}年')
    return 0


main()