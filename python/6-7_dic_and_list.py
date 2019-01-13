dog = {
    'host': 'yxr',
    'age': 5
}
cat = {
    'host': 'zzw',
    'age': 1000
}
monkey = {
    'host': 'xsh',
    'age': 90
}
pets = []
pets.append(dog)
pets.append(cat)
pets.append(monkey)
for pet in pets:
    print('Its host is ' + pet['host'] + ', and its age is ' + str(pet['age']))
