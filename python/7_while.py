sandwich_orders = ['sand1', 'sand2', 'sand3']
finished_sandwiches = []

while sandwich_orders:
    sand = sandwich_orders.pop()
    print('Ok, ' + sand + ' has been prepared!')
    finished_sandwiches.append(sand)

print('\nThe following sandwiches have been prepared:')
for sand in finished_sandwiches:
    print(sand)
