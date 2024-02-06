import sys
ch, ch1, ch2, ch3 = int(input()), 0, 0, 0

ch1,ch2,ch3 = ch//100,(ch//10)%10,ch%10
ch3_dict = dict([(1, 'один'), (2, 'два'), (3, 'три'), (4, 'четыре'), (5, 'пять'), (6, 'шесть'), (7, 'семь'),
                (8, 'восемь'), (9, 'девять'), (0, '')])
ch2_dict = dict([(2, 'двадцать'), (3, 'тридцать'), (4, 'сорок'), (5, 'пятьдесят'), (6, 'шестьдесят'),
                (7, 'семьдесят'), (8, 'восемьдесят'), (9, 'девяносто'), (0, '')])
ch1_dict = dict([(1, 'сто'), (2, 'двести'), (3, 'триста'), (4, 'четыреста'), (5, 'пятьсот'), (6, 'шестьсот'),
                (7, 'семьсот'), (8, 'восемьсот'), (9, 'девятьсот'), (0, '')])
if ch == 0:
    print('ноль')
    sys.exit()
elif ch == 10:
    print('десять')
    sys.exit()
elif ch == 11:
    print('одиннадцать')
    sys.exit()
elif ch == 12:
    print('двенадцать')
    sys.exit()
elif ch == 13:
    print('тринадцать')
    sys.exit()
elif ch == 14:
    print('четырнадцать')
    sys.exit()
elif ch == 15:
    print('пятнадцать')
    sys.exit()
elif ch == 16:
    print('шестнадцать')
    sys.exit()
elif ch == 17:
    print('семнадцать')
    sys.exit()
elif ch == 18:
    print('восемьнадцать')
    sys.exit()
elif ch == 19:
    print('девятнадцать')
    sys.exit()
if ch1 != 0 and ch2 != 0 and ch3 != 0:
    print(ch1_dict[ch1] + ' ' + ch2_dict[ch2] + ' ' + ch3_dict[ch3])
elif ch1 == 0 and ch2 != 0 and ch3 != 0:
    print(ch2_dict[ch2] + ' ' + ch3_dict[ch3])
else:
    print(ch3_dict[ch3])