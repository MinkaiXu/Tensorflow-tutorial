filename = r'python\email.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()
contents = ''
for line in lines:
    print(line.rstrip())
    if(line.strip() != '\n'):
        contents += (line.strip() + ' ')
    else:
        continue
if 'Minkai' in contents:
    print('\n' + contents.replace('Minkai', '******'))
    # replace()不会对原字符串进行修改
print('\n' + contents)
print(len(contents))
