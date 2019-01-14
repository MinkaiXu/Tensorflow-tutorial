filename = 'python\message.txt'

with open(filename, 'w') as file_object:
    while True:
        message = input('Type in the message and write in the file: ')
        if message == 'quit':
            print('Quit the typing program now~')
            break
        else:
            file_object.write(message + '\n')
