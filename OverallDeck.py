# -*- coding: utf-8 -*-
"""
Created on Mon May 10 15:57:02 2021

@author: Graeme
"""

import csv

Decks=[['Deck Name','Wins','Losses']]

with open('Week2.csv', newline='') as csvfile:
    alldecks = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in alldecks:
        if len(row)!=0:
            deck=[row[0],row[1],row[2]]
            deck[1]=float(deck[1])
            deck[2]=float(deck[2])
            
            deckcheck='n'
            for deckrow in Decks:
                if deck[0]==deckrow[0] and deckcheck=='n':
                    deckrow[1]=deckrow[1]+deck[1]
                    deckrow[2]=deckrow[2]+deck[2]
                    deckcheck='y'
           
            if deckcheck=='n':
               Decks.append(deck)
               
with open('Week3.csv', newline='') as csvfile:
    alldecks = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in alldecks:
        if len(row)!=0:
            deck=[row[0],row[1],row[2]]
            deck[1]=float(deck[1])
            deck[2]=float(deck[2])
            
            deckcheck='n'
            for deckrow in Decks:
                if deck[0]==deckrow[0] and deckcheck=='n':
                    deckrow[1]=deckrow[1]+deck[1]
                    deckrow[2]=deckrow[2]+deck[2]
                    deckcheck='y'
           
            if deckcheck=='n':
                Decks.append(deck)     
                



with open('OverallDecks.csv', 'w') as f:
      

    write = csv.writer(f)
    
    write.writerows(Decks)              