while True:
    formula = input('Please input the formula: ')
    if formula == 'quit':
        break
    characters = formula.split()
    try:
        print(str(int(characters[0]) + int(characters[2])) + 
            ' = ' + str(int(characters[0])) + ' ' + 
            characters[1] + ' ' + str(int(characters[2])))
    except:
        print('Somthing wrong happened!')


'''
import webbrowser
try:
    a = 1/0
except Exception as e:
    webbrowser.open('https://stackoverflow.com/search?q=' + e.__str__())
'''
