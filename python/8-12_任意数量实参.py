def muti_element(*es):
    for e in es:
        print(e)


def muti_keyvalue(**kvs):
    for k, v in kvs.items():  # 注意.items()
        print('key: ' + k + '\nvalue: ' + str(v))


muti_element(1, 2, 3, 4, 4, 6, 5, 7, 413, 5, 41, 5, 2, 2, 4, 321, 4, 3214)

muti_keyvalue(ask=1, aa=2)
