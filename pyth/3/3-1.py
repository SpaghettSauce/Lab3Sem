string = input()
string_list = list(string)
duplicate = []
for item in string_list:
    if string_list.count(item) > 1 and item not in duplicate:
        duplicate.append(item)
        numbers = string_list.count(item)
        duplicate.append(numbers)
    elif string_list.count(item) == 1:
        duplicate.append(item)
print(''.join(map(str, duplicate)))