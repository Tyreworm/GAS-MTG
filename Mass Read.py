# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 21:01:58 2021

@author: Graeme
"""

import re
import csv
import os 

Everycard=[]


for file in os.listdir('D:/Users/Graeme/Documents/Python/GBGG/Top Decks'):
    if file.startswith('EveryCard')==False:
        if file.endswith('.txt'):
            with open(file) as f:
                deck = f.readlines()
                
    
                if deck[0]=='Deck\n':
                    deck.pop(0)    
    
                count=0    
                for line in deck:
                    line=line.strip('\n')
                    number=re.findall('\d+', line )
                    number=number[0]
                    card=line.replace(number, '')
                    card=card.strip()
                    number=int(number)
                    
                    deck[count]=[card,number]
                    
                    output='N'
                    for allcardline in Everycard:
                        if card==allcardline[0]:
                            allcardline[1]=allcardline[1]+number
                            output='Y'
    
                    if output=='N':
                        Everycard.append(deck[count])


                    count=count+1

with open('EveryCard.csv', 'w') as f:
    write = csv.writer(f)
    write.writerows(Everycard)