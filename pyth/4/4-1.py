list = [3, 7, 1, 9, 5, 2]


  
min = list.index(min(list))
max = list.index(max(list))
    
list[min], list[max] = list[max], list[min]
    
print(list)