cities = set()

while True:
    city = input('Город: ')
    
    if city != 'q':
        cities.add(city)
    else:
        print(len(cities))
        break