'''
Write a program to take 2 nos as input and the program will return a prompt to guess a value.
if the no. matches the random generated no. we get a point.
'''

import random
import sys

val = random.randint(int(sys.argv[1]),int(sys.argv[2]))
#print(val)  # Cheating
print("Guess a no. between "+ sys.argv[1] + " and " + sys.argv[2] )
while True:
    guess = input("> ")
    if val == int(guess):
        print(f"Perfect! ")
        break
    else:
        print("Try again !!")




