# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 22:27:30 2021

@author: Graeme

"""

import csv
import requests
import time

cards=[]
creatures=[]
planeswalkers=[]
creaturementions=[]
noncreatures=[]
DFC=[]

creaturetypes=[]

gettext='https://api.scryfall.com/cards/named?exact='

with open('EveryCard.csv', newline='') as csvfile:
    allcard= csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in allcard:
        if len(row)!=0:
            cards.append(row)
            
count=0
for line in cards:
    time.sleep(0.15)
    
    cardtext=line[0]
    sendtext=gettext+cardtext

    response = requests.get(sendtext)
    print(line[0],',',response.status_code,',',count)
    count=count+1

    output=(response.json())

    cardout=[]
    cardout.append(line[0])
    line[1]=int(line[1])
    cardout.append(line[1])
    
    if 'card_faces' in output.keys():
        DFC.append(cardout)
    else:
        if 'Creature' in output['type_line']:
            typeout=[]
            typeout.append(line[0])
            typeout.append(line[1])
            typeout.append(output['type_line'])
            creaturetypes.append(typeout)
        
            if output['cmc']>3:
                Inq=0
            else:
                Inq=line[1]
            
            if 'Legendary' in output['type_line']:
                Legend=line[1]
            else:
                Legend=0
        
            if 'B' in output['colors']:
                doomblade=0
            else:
                doomblade=line[1]
            
            try:
                toughness=int(output['toughness'])
                toughnessnote='N'
                if toughness>3:
                    bolt=0
                else:
                    bolt=line[1] 
                if toughness==1:
                    oneT=line[1]
                    twoT=0
                    threeT=0
                elif toughness==2:
                    oneT=0
                    twoT=line[1]
                    threeT=0
                elif toughness==3: 
                    oneT=0
                    twoT=0
                    threeT=line[1]
                else:
                   oneT=0
                   twoT=0
                   threeT=0
                
                    
            except ValueError:
                lastgrasp='?'
                toughnessnote='Y'
  
            
            if 'indestructible' in output['oracle_text'] : 
                indes='Y'
            elif 'Indestructible' in output['oracle_text'] : 
                indes='Y' 
            else:
                indes='N'
                
            if 'Hexproof' in output['oracle_text'] : 
                hexproof='Y'
            elif 'hexproof' in output['oracle_text'] : 
                hexproof='Y'
            else:
                hexproof='N' 
            
            
            
            cardout.append(output['cmc'])    
            cardout.append(Inq) 
            cardout.append(Legend)   
            cardout.append(doomblade)
            cardout.append(bolt) 
            
            cardout.append(oneT) 
            cardout.append(twoT) 
            cardout.append(threeT) 
            
            cardout.append(indes)
            cardout.append(toughnessnote) 
            cardout.append(hexproof) 
            creatures.append(cardout)   
            
            
       
        elif 'Planeswalker' in output['type_line']: 
            if output['cmc']>3:
                Inq=0
            else:
                Inq=line[1]
                
            if 'Legendary' in output['type_line']:
                Legend=line[1]
            else:
                Legend=0    
                
            cardout.append(Inq) 
            cardout.append(Legend)   
            planeswalkers.append(cardout)
        
        elif 'creature' in output['oracle_text'] : 
            if output['cmc']>3:
                Inq=0
            else:
                Inq=line[1]
            if 'Legendary' in output['type_line']:
                Legend=line[1]
            else:
                Legend=0    
                
            cardout.append(Inq) 
            cardout.append(Legend)       
            creaturementions.append(cardout)
        else :
            if output['cmc']>3:
                Inq=0
            else:
                Inq=line[1]
            if 'Legendary' in output['type_line']:
                Legend=line[1]
            else:
                Legend=0     
                
            cardout.append(Inq) 
            cardout.append(Legend)      
            noncreatures.append(cardout)
        
with open('Creatures.csv', 'w') as f:
    write = csv.writer(f)
    write.writerows(creatures)    
    
with open('Walkers.csv', 'w') as f:
    write = csv.writer(f)
    write.writerows(planeswalkers)

with open('Mentions.csv', 'w') as f:
    write = csv.writer(f)
    write.writerows(creaturementions)    
    
with open('Noncreatures.csv', 'w') as f:
    write = csv.writer(f)
    write.writerows(noncreatures)  
    
with open('DFCs.csv', 'w') as f:
    write = csv.writer(f)
    write.writerows(DFC)   

with open('CreatureTypes.csv', 'w') as f:
    write = csv.writer(f)
    write.writerows(creaturetypes)            
    
    