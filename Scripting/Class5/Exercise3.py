'''
Created on Oct 20, 2017

@author: paulo
'''

# Remove vowel from a string

#Receive the string from the user
text = input('Type the word: ')

# Replace vowels for nothing
text = text.replace('a', '')
text = text.replace('e', '')
text = text.replace('i', '')
text = text.replace('o', '')
text = text.replace('u', '')

#Print the result.
print(text)