#!python3
#this is an example of a simple chatbot

# Defining coffee_bot function:
def coffee_bot():
  print('Welcome to The Coffee Shop')
  size = get_size()
  print(size)

# Defining get_size function:
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    return get_size()

# Calling our coffee_bot: 
coffee_bot()
