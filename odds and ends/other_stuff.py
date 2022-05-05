# -*- coding: utf-8 -*-
"""
Created on Thu May  5 17:56:27 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""



import emoji

print(emoji.emojize("This library is awesome :thumbs_up:"))
print(emoji.emojize(":koala:"))
print(emoji.emojize(":adhesive_bandage:"))
print(emoji.emojize("I don't know what to do with emojis :disappointed_face:"))

## https://carpedm20.github.io/emoji

#################################################################

import colorama, random

scores = []
for i in range(12):
    scores.append(random.randint(50, 110))
    
sum = 0
for s in scores:
    sum += s
    
avg = sum / len(scores)

print(colorama.Back.CYAN)
if avg >= 90:
    grade = "A"
    col = colorama.Fore.GREEN
elif avg >= 80:
    grade = "B"
    col = colorama.Fore.GREEN
elif avg >= 70:
    grade = "C"
    col = colorama.Fore.BLUE
elif avg >= 60:
    grade = "D"
    col = colorama.Fore.BLUE
else:
    grade = "F"
    col = colorama.Fore.RED
    
print(col + f"the grade is {grade}")

print("hello world")

print(colorama.Style.RESET_ALL)

print(colorama.Fore.GREEN + "change some colors...")
print(colorama.Back.CYAN + "or maybe this...")
print(colorama.Fore.BLUE + "one more thing...")
print(colorama.Style.RESET_ALL)

print("back to normal...")


###########################################################

import wikipedia

print(wikipedia.search("GPA"))

print(wikipedia.summary("Ivy Tech", sentences=3))


results = wikipedia.search("laptop")
# for r in results:
#     print(wikipedia.summary(r, sentences=2))
#     print()
#     print()
    

#print(wikipedia.summary(results[0], sentences=8))



#########################################################



import dis


def sayHi():
    print("hello world")
    

dis.dis(sayHi)

print("\n<----------------------------->\n")

def summationUpTo(x):
    values= [i for i in range(x+1)]
    accumulator = 0
    for v in values:
        accumulator += v
    return accumulator


dis.dis(summationUpTo)









































