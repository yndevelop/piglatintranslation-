#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 21:29:18 2021

@author: user
"""

#for number in range(1, 13):
   # print(number)
#vowels = 0
#consonants = 0 
  
#for letter in "Hello":
   # if letter.lower() in "aeiou":
       # vowels = vowels + 1
   # elif letter == " ":
       # pass
    #else:
       # consonants = consonants + 1
#print("There are {} vowels".format(vowels))
#print("There are {} consonants".format(vowels))



#students = {
   # "male": ["AlYahu", "Ban"],
    ## }

#for key in students.keys():
   # for name in students[key]:
      #  if "a" in name:
           # print(name)
           # 
            
#even_number = [x for x in range(1,101) if x %2 == 0]
#print(even_numbers)

#get sentence from user

orginial = input("Please enter a sentence: ").lower().strip()

#split sentence into words
words = orginial.split()
print(words)

#loop though words and convert to pig latin

new_words = []

#if starts with vowel, just add "yay"
for word in words:
   if word[0] in "aeiou":
       new_word = word + "yay"
       new_words.append(new_word)
   else:
        vowel_pos = 0
        for letter in word:
           if letter not in "aeiou":
            vowel_pos = vowel_pos + 1
        else:
            break
        #Slice
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)

#Otherwise, move the first consonant cluster to end, and add "ay"

#stick words back together
output = " ".join(new_words)

#output the final string
print(output)