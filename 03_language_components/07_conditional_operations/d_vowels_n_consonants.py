#!/usr/bin/python3
"""
Purpose: To check whether the given character
        is vowels or consonant

        vowels - aeiou

in operator  works with any iterable object

Algorithm:
============
1) is it empty 
2) is it alphabet 
3) is it vowel or not 

NOTE: handle case-sensitivity 
"""

input_char = input("Enter the character:")
vowels = 'aeiouAEIOU'

if input_char:
    if input_char in vowels:
        print(f'The given character {input_char} is a vowel')
    else:
        print(f'The character is a constant')
else:
    print(f'Please enter a character')