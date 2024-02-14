import random

kamni = random.randint(-100, 100)
sumKamni = random.randint(1, 10)
substractKamni = random.randint(1, 10)
print("У вас ", kamni, "кам1ней, вы можете выполнить три действия:")
print(" 1 чтобы прибавить камни к текущим")
print(" 2 чтобы вычесть камни из текущих")



while True:
    if (kamni != 0):
        sumKamni = random.randint(1, 10)
        substractKamni = random.randint(1, 10)
        print("+", sumKamni)
        print("-", substractKamni)

        userChoice = int(input())
        if (userChoice == 1):
            kamni += sumKamni
            print(kamni, "камней.")
        if (userChoice == 2):
            kamni -= substractKamni
            print("Второе действие ", kamni, "камней.")
        if (userChoice == 3):
            break;
    else:
        print("Вы выиграли")
        break;