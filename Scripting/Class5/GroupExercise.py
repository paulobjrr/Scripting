'''
Created on Oct 20, 2017

@author: paulo
'''

import random

def createDeck():
    deck = []
    suits = ['s','h','d','c']
    values = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    for i in values:
        for j in suits:
            deck.append(i + j)
    return deck

def shuffle(deck):
    temp = ''
    rand = 0
    for i in range(0,51):
        rand = random.randint(0,51)
        temp = deck[i]
        deck[i] = deck[rand]
        deck[rand] = temp
    return deck
        
    

mydeck = createDeck()

print(mydeck)

shuffledeck = shuffle(mydeck)

print(shuffledeck)
