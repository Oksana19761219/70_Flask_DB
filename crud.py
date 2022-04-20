from app import City

cities = City.query.all()

for city in cities:
    print(city.name)