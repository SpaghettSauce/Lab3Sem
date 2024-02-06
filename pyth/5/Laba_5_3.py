def named_cities(set_cities, current_city):
    if current_city in set_cities:
        return 'REPEAT'
    else:
        set_cities.add(current_city)
        return 'OK'

count = int(input())

cities_set = set()

for i in range(count):
    city = input()
    result = named_cities(cities_set, city)
    print(result)