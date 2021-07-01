#!python3
#!keep idiot busy - omegalul haha omg 


import pyinputplus as pyip

while True:
  prompt = 'Want to know how to keep an idiot busy for hours?\n'
  response = pyip.inputYesNo(prompt)
  
  if response == 'no':
    break

print('Thank you. Have a nice day.')
   
  
  '''
  You can also make use of the inputYesNo() function in non-English languages by passing yesVal and noVal keyword arguments. For example, the Spanish version of this program would have these two lines:

    prompt = '¿Quieres saber cómo mantener ocupado a un idiota durante horas?\n'
    response = pyip.inputYesNo(prompt, yesVal='sí', noVal='no')
    if response == 'sí':
 '''
