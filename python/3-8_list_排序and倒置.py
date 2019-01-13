city = ['beijing', 'shanghai', 'hongkong', 'los angeles', 'montreal']
for i in range(len(city)):
    city[i] = city[i].title()

print(city)
print(sorted(city))
print(sorted(city, reverse = True))
print(city)
city.sort()
print(city)
city.reverse()
print(city)
