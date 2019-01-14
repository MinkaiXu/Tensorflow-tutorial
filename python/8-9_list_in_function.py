magicians = ['yxy', 'zzw', 'xsh', 'xmk']


def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = 'the Great ' + magicians[i]
    return magicians


def show_magicians(magicians):
    for magician in magicians:
        print(magician.title() + ', you are great!')


great_magicians = make_great(magicians[:])  # 用切片避免列表被更改
show_magicians(magicians)  # 不使用切片，函数直接对列表进行更改
show_magicians(great_magicians)
