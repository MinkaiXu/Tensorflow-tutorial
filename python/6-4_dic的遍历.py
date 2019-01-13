xmk = {
    'BY': 95,
    'DSP': 76,
    'ITC': 87
}
xmk['xakc'] = 95
print(xmk)
del xmk['xakc']

for k, v in xmk.items():
    print(k.title() + ': \t' + str(v))
print()

print(xmk.items())
print(xmk.keys())  # the keys of a dic is a list, 但不支持indexing
print(sorted(xmk.keys()))

print('\nThe average score of xmk is: ' + str(int(sum(xmk.values())/len(xmk.values()))))
