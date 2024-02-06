listw = ['abc', 'bcd', 'abc', 'abd', 'abd', 'abd', 'dcd', 'abc']


count_dict = {}
for string in listw:
    if string in count_dict:
        count_dict[string] += 1
    else:
        count_dict[string] = 1

print( list(count_dict.values()))

