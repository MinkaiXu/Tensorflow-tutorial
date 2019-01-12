# string's .title .upper .lower functions
name = 'yI xINg rui'
print(name)
print(name.title())
print(name.upper())
print(name.lower()+'\n')

# using '+' to connect strings
name = "michael"
message = "Hello " + name.title() + ", would you like to learn some Python today?\n"
print(message)

# using '\n' and '\t' to format the print
name = " michael "
message = " deeplearning is so powerful!"
info = name.strip().title() + " says: \"" + message.strip().title() + '\"'
print(info)

# using 'str' to transfer the int or float to string
news = "the ".title() + str(33) + "rd AAAI is coming!"
print(news + '\n')

# str(), 
print(str(5+3) + '\n' + str(9-1) + '\n' + str(4*2) + '\n' + str(80//9))
