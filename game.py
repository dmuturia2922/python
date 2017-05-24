#usr/bin/python
'''
This is a guessing game
Author: Dennis Muturia
version: 1.0.0
This is an improvement version
'''
import random
print "Please enter your name"
name = input()
entries = 0
def printouts():
     true_val = random.randrange(0, 20)#guesses numbers from 0 to 20
     for i in range(0, 5):
          entries =+ 1
          print"Please enter the value" + " "+ name
          my_value = int(input())#input your value

          if my_value <= true_val:
               print"Your value is low"
               print"Retry"
          elif my_value >= true_val:
               print"Your value is high"
               print"Retry"
          elif my_value == true_val:
               print"Correct. You guessed it correct. You have entered"+" "+str(entries)
               break
          else:
               print "Invalid input"
def main():
     #main function
     print "This is my guessing game"
     print "Enter the value your value"
     printouts()

if __name__ == '__main__':
     main()
