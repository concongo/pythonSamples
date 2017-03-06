#title              :pangram.py
#description        :Story
#                    BA pangram is a sentence that contains every single letter of the alphabet at least once.
#                    For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because 
#                   it uses the letters A-Z at least once (case is irrelevant).

#                   Given a string, detect whether or not it is a pangram. Return True if it is, False if not. 
#                   Ignore numbers and punctuation.

#author             : Jose Fernando Gonzalez
#date               : 20170306
#version            : 0.1
#usage              : pangram.py
#notes              : Kata from codewars
#python_version     : 3.4.3

def is_pangram(s):
    
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    n = len(alphabet) # n is the numbers of letters in the alphabet
    i = 0
    for letter in alphabet:
        if s.upper().find(letter) >=0 : #if the letter is found in the sentence
            i=i+1 #add one to the counter
            s=s.upper().replace(letter,'') #remove the letter from the sentence
    return i==n   #if i equals n means that is a pangram
    

print(is_pangram("The quick, brown fo jumps over the lazy dog!"))