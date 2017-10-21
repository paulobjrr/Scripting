'''
Created on Oct 20, 2017

@author: paulo
'''


# Reverse a String

# Get the string from the user
word = input('Enter the word to be reversed: ')

# Define an empty variable
reverse = ''

#iterate through the string from the end to the beginning
for i in range(len(word)):
    reverse = reverse + word[len(word) - i - 1]
    
# Print the reversed string
print(reverse)
