#!python3
#! multiplicationQuiz.py - Make a timed multiplication quiz. 

'''
PyInputPlus’s features can be useful for creating a timed multiplication quiz. 
By setting the allowRegexes, blockRegexes, timeout, and limit keyword argument to pyip.inputStr(), 
you can leave most of the implementation to PyInputPlus. The less code you need to write, the faster 
you can write your programs. Let’s create a program that poses 10 multiplication problems to the user, 
where the valid input is the problem’s correct answer. Open a new file editor tab and save the file as multiplicationQuiz.py.

First, we’ll import pyinputplus, random, and time. We’ll keep track of how many questions the program asks and how many correct answers the user gives with the variables numberOfQuestions and correctAnswers. A for loop will repeatedly pose a random multiplication problem 10 times:
'''

import pyinputplus as pyip 
import random, time 


numberOfQuestions = 10 
correctAnswers = 0 
for questionNumber in range(numberOfQuestions):

'''
Inside the for loop, the program will pick two single-digit numbers to multiply. We'll use these numbers to create a #Q: N x N = prompt for the user, where Q is the question number (1 to 10) and N are the two numbers to multiply. 
'''

#Pick two random numbers:
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)


prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)


'''
The pyip.inputStr() function will handle most of the features of this quiz program. The argument we pass for allowRegexes is a list with the regex string '^%s$', where %s is replaced with the correct answer. The ^ and % characters ensure that the answer begins and ends with the correct number, though PyInputPlus trims any whitespace from the start and end of the user’s response first just in case they inadvertently pressed the spacebar before or after their answer. The argument we pass for blocklistRegexes is a list with ('.*', 'Incorrect!'). The first string in the tuple is a regex that matches every possible string. Therefore, if the user response doesn’t match the correct answer, the program will reject any other answer they provide. In that case, the 'Incorrect!' string is displayed and the user is prompted to answer again. Additionally, passing 8 for timeout and 3 for limit will ensure that the user only has 8 seconds and 3 tries to provide a correct answer:
'''
