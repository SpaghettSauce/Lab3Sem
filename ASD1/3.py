x = int(input())
answ = []

for K in range(100):
    for L in range(100):
        for M in range(100):
            number = 3 ** K * 5 ** L * 7 ** M 

            if number <= x:
                answ.append(number)


for a in sorted(answ):
    print( a, sep='')
    
   