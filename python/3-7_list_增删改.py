name = ['yi xingrui', 'zhao ziwen', 'xie sihong', 'xu minkai']
for i in range(4):
    print("good morning, ".title() + name[i].title() + '!')
print('\n')

print("Oh, zzw is a shit! I want to change a roommate!")
name[1] = "zhao zelin".title()
for i in range(4):
    print("I'd like to live together with you, " + name[i].title() + '!')
print('\n')

print("Ummm, I'm kind of miss zzw...Come back with zzl!")
name.insert(0, 'zhao ziwen'.title())
name.append('zhao zilong'.title())
namelist = ''
for i in range(len(name)):
    namelist += name[i].title()
    if(i != (len(name)-1)):
        namelist += ', '
print(namelist + ': You are all my good roommates!\n')

print('I want to live with only 2 people!')
while len(name) != 2:
    sb = name.pop()
    if sb == 'xu minkai':
        name.insert(0, sb)
    else:
        print(sb.title() + ', please go out now :)')
print('\n')

message = 'Finally, '
for i in range(2):
    message += (name[i].title() + ' ')
    if i != 1:
        message += 'and '
    else:
        message += 'live toghter now.'
print(message + '\n')

del name[0]
del name[0]
print("All are gone.")
print(name)
