
import copy
import plus_self
from time import *

print(str(2333))
print(int('1')+2332)
print(float('1.2')+2331.8)  # int将str转为int;str将int转为str
# str之间可以用+连接输出，中间没有空格;使用','可以进行多输出，之间用空格隔开
print('-----------------------------')

print(8//2)
print('-----------------------------')

a, b, c = 1+1, 2, 3
print(a, b, c, '\n\n')  # 输出
print('-----------------------------')

while a < 5:
    print(a)
    a += 1
print('-----------------------------')

e = [1, 55, 5, 54, 5454, 54, 5, 545]
for i in e:
    print(i)
for i in range(5):
    print(i)
for i in range(1, 5, 2):
    print(i)
print('-----------------------------')

x = 1
y = 100
z = 3
if x < z and y < z:
    print("z max")
elif z < x and y < x:
    print('x max')
else:
    print('y max')
print('-----------------------------')


def fuction():
    #可以设置缺省值
    #函数调用时可以指定复制，使用语句‘实参=形参’
    global fuck
    fuck = 'fuck'
    return 'you'


you = fuction()
print(fuck, you)
print('-----------------------------')

file = open('file.txt', 'w')
file.write(you)
file.close()
# print('-----------------------------')

file = open('file.txt', 'a')
file.write('\nemmm\nemmm\naaaaaa')
file.close()
# print('-----------------------------')

file = open('file.txt', 'r')
content = file.read()
print(content)
file.close()
# print('-----------------------------')

file = open('file.txt', 'r')
content = file.readlines()
print(content)
print('-----------------------------')

# class

#score = input('show me your score: ')
# if score > '100':
#    print('woc')
# if score <= '100':
#    print('2333')
# print('-----------------------------')

tuple_a = (1, 2257, 57)
list_a = [54, 545, 5455]
for index in range(len(tuple_a)):
    print(tuple_a[index])
list_a.append(59595)
list_a.insert(2, 54546767)
list_a.remove(545)  # remove the first value
print(list_a, '\n',
      list_a[-1], '\n',
      list_a[:-1])
list_a.sort(reverse=True)
print(list_a)
print(list_a.count(5455),  # the first value index
      list_a.index(5455))  # count the number of the value
print('-----------------------------')

dic1 = {'apple': [2, 'emmm', 3], 'pear': 2, 'orange': 3}
dic2 = {1: 'aa', 55: 6}
print(dic1['apple'][1])
del dic1['orange']
print(dic1)
dic1['orange'] = 20
print(dic1)
print('-----------------------------')

# import time as t
# from time import localtime, time
print(localtime(), time())
print('-----------------------------')

print(plus_self.plus(5, 5))
print('-----------------------------')

# continue; break; pass;

try:
    file = open('2333', 'w')
except Exception as e:
    print(e)
else:
    file.write('lalalala')
    file.close()
print('-----------------------------')

a = [1, 2, 3]
b = [4, 5, 6]


def func(x, y): return x + y


for x, y in zip(a, b):  # zip is a object
    print(func(x, y))
print('-----------------------------')
for i in map(func, a, b):
    print(i)
print('-----------------------------')

a = [1, 2, 3]
b = a  # the memory is all the same
c = copy.copy(a)  # shadow copy: the shadow memory is different
a = [1, 2, [3, 4]]
d = copy.copy(a)  # shadow copy: but the deep memory is still the same
e = copy.deepcopy(a)  # deepcopy: the memory is all different
