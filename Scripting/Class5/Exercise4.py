'''
Created on Oct 20, 2017

@author: paulo
'''

letters='abcdefghijklmnopqrstuvwxyz'

phrase = input('Type a long string: ')

for c in letters:
    print('%s occurs %d times' % c, phrase.count("a"))