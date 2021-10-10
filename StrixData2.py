# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:32:29 2021

@author:
"""


import csv
import re

EUdata=[]
WinData=[]
NAdata=[]
EUWinData=[]
Tolerance=0.1

with open('The Great Big Gladiator Games.csv', newline='') as csvfile:
    alldecks = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in alldecks:
        deck = [row[0],row[1],row[2],row[3],row[4],row[5]]
        output=[]
        for n in range(len(deck)):
            deck[n]=deck[n].strip('"')
               
        
        if deck[0]!='Rank':
            
            deckdata= [float(s) for s in re.findall(r'-?\d+\.?\d*', deck[4])]
                  
            deckwin= deckdata[0] 
            deckloss =abs(deckdata[1] )
            
            deckperc=deck[5].strip('%')
            deckperc=float(deckperc)
            
            PercCheck=(deckwin/(deckwin+deckloss))*100
            
            
            
            while PercCheck>(deckperc+Tolerance) or PercCheck<(deckperc-Tolerance):
                deckwin=deckwin-1
                deckloss = deckloss-1
                PercCheck=(deckwin/(deckwin+deckloss))*100
                
            deck.append(deckwin)     
            deck.append(deckloss)     
            deck.append(deckperc) 
            deck.append(PercCheck) 
            output=[deck[1],deck[6],deck[7]]
            
        NAdata.append(deck) 
        
        WinData.append(output)    


WinData.pop(0)  

             
with open('GBGG.csv', 'w') as f:
      

    write = csv.writer(f)
    
    write.writerows(WinData)