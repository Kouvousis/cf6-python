# list of cities
cities = ["london", "paris", "barcelona", "athens"]

# titled cities
cap_cities = list(map(lambda city: city.title(), cities))
print(cap_cities)

cap_cities2 = [city.title() for city in  cities]
print(cap_cities2)