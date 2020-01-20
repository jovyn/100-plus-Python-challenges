'''
Write a bunch of jokes to a file and then create another file with its german translation.
in the end output the contents off both the files.
'''

import pyjokes
from googletrans import Translator

translator = Translator()
jokes = pyjokes.get_jokes()
for joke in jokes:
    with open('jokes/jokes_en.txt',mode='a') as out:
        out.write(joke + "\n")

read_jokes = open('jokes/jokes_en.txt',mode='r').readlines()

for line in read_jokes :
    german_line = translator.translate(line, dest='de')

    with open('jokes/jokes_de.txt',mode='a') as out:
        out.write(german_line.text + "\n")







