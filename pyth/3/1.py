string = input()
string_list = list(string)
summary = len(string_list)
final = ''
for i in range(summary-1):
    if string_list[i].isnumeric() and string_list[i+1].isnumeric():
        new_value = string_list[i] + string_list[i+1]
        temp = i
        del string_list[i]
        del string_list[i]
        string_list.insert(temp, new_value)
summary = len(string_list)
for i in range(summary-1):
    if string_list[i].isnumeric() == False and string_list[i+1].isnumeric() == True:
        final += string_list[i] * int(string_list[i+1])
    elif string_list[i].isnumeric() == True and string_list[i+1].isnumeric() == False:
        final += string_list[i+1]
    elif string_list[i].isnumeric() == False and string_list[i+1].isnumeric() == False:
        final += string_list[i+1]
print(final)