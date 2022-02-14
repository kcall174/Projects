#!python3
#this is an example of a simple chatbot

# Defining our functions
def coffee_bot():
  print('Welcome to The Coffee Shop')
  size = get_size()
  print(size)

# Defining out get_size function
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  return res


# Calling our coffee_bot 
coffee_bot()
