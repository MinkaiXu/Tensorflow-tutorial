class Restaurant():
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_severed = 0

    def discribe_restaurant(self):
        print(self.restaurant_name + ' is a ' +
              self.cuisine_type + ' food restaurant, and ' +
              str(self.number_severed) + ' people have visited here.')

    def open_restaurant(self):
        print(self.restaurant_name + ' is open right now!')

    def set_number_severed(self, num):
        self.number_severed = num

    def increment_number_served(self, num):
        self.number_severed += num


restaurants = []
restaurants.append(Restaurant('KFC', 'fast'))
restaurants.append(Restaurant('HaLe', 'odinary'))
restaurants.append(Restaurant('Penglai Xiaomian', 'delicious'))

i = 5
for restaurant in restaurants:
    restaurant.set_number_severed(5)
    restaurant.increment_number_served(i)
    i += 5
    restaurant.discribe_restaurant()
    restaurant.open_restaurant()
    print()


class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ['stra', 'apple', 'banana']

    def choose_flavor(self):
        print('Choose your favorite flavor: ')
        for flaver in self.flavors:
            print(' - ' + flaver)


r = IceCreamStand('DQ', 'Ice Cream')
r.set_number_severed(100)
r.increment_number_served(5)
r.open_restaurant()
r.discribe_restaurant()
r.choose_flavor()
