import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import csv

t = np.linspace(0, 1, 500, endpoint=False)
square_wave = signal.square(2 * np.pi * 5 * t)

plt.plot(t, square_wave)
plt.ylim(-2, 2)
plt.show()

mu, sigma = 0, 0.1
s = np.random.normal(mu, sigma, 1000)
count, bins, ignored = plt.hist(s, 30, density=True)
plt.show()



with open('passengers.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    data = list(reader)
months = [row[0] for row in data]
passn = [int(row[1]) for row in data]

plt.figure()
plt.plot(months, passn)
plt.title('Пассажиропоток за все время')
plt.xlabel('Месяц')
plt.ylabel('Пассажиры')
plt.show()

months_1951_1955 = [months[i] for i in range(len(months)) if '1951' <= months[i][:4] <= '1955']
passengers_1951_1955 = [passn[i] for i in range(len(months)) if '1951' <= months[i][:4] <= '1955']

plt.figure()
plt.hist(passengers_1951_1955, bins=12)
plt.title('Распределение пассажиров по месяцам, 1951 - 1955 гг.')
plt.xlabel('Пассажиры')
plt.ylabel('Частота')
plt.show()

