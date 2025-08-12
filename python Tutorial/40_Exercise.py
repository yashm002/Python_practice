# Write a python program to translate a message into secret code language.
# Use the rules below to translate normal English into secret code language
import random

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

import random
import string

word = input("Enter the word: ")
if (len(word) < 3):
    print(word[::-1])
else:
    w1 = word[0]
    w2 = word.removeprefix(word[0])
    w3 = ""
    for i in w2:
        w3 = w2 + w1
    print(w3)
    add1 = input("enter 3 alphabets to the start: ")
    add2 = input("enter 3 alphabets to the end: ")
    add = add1 + w3 + add2
    print(add)
    # word.translate({ord(word[0]): None})