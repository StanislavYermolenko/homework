class City:
    age = 2000

    def public_transport(self):
        print('working hours around the clock')

city = City()

print(city.age)

class District_Pozniaky(City):

    def bike_lanes(self):
        print("lenght = 70 km")


district = District_Pozniaky()

print(district.bike_lanes())

class Steets(District_Pozniaky):

    def streets_numbers(self):
        pass
streets = Steets()

print(streets.public_transport())