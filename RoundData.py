# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 11:02:24 2021

@author: Graeme
"""

import csv
import re


Matches=[['Deck 1','Deck 1 MWs','Deck 1 GWs','Deck 2','Deck 2 MWs','Deck 2 GWs']]

with open('Gladiator EMEA Season 3, Week 5 Round 1.csv', newline='') as csvfile:
    allmatches = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in allmatches:
        match = [row[0],row[1],row[2],row[3],row[4],row[5]]
        for n in range(len(match)):
            match[n]=match[n].strip('"')
            
        matchdata=match[5].strip(match[1])
        matchdata=matchdata.strip(match[3])
        matchrecord= [int(s) for s in re.findall(r'-?\d+\.?\d*', matchdata)]
        
        matchbye='N'
        if 'bye' in match[5]:
            matchbye='Y'
        
        
        if match[1]!='Player 1' and matchbye=='N':
            if match[1] in match[5]:
                deck1mw=1
                deck2mw=0
                deck1gw=abs(matchrecord[0])
                deck2gw=abs(matchrecord[1])
            else:
                    deck1mw=0
                    deck2mw=1
                    deck1gw=abs(matchrecord[1])
                    deck2gw=abs(matchrecord[0])

            matchcheck='N'    
            for matchrow in Matches:
                if match[2]==matchrow[0] and match[4]==matchrow[3]:
                   matchrow[1]=matchrow[1]+deck1mw
                   matchrow[2]=matchrow[2]+deck1gw
               
                   matchrow[4]=matchrow[4]+deck2mw
                   matchrow[5]=matchrow[5]+deck2gw
                   matchcheck='Y'
               
                elif match[4]==matchrow[0] and match[2]==matchrow[3]:
                    matchrow[1]=matchrow[1]+deck2mw
                    matchrow[2]=matchrow[2]+deck2gw
                
                    matchrow[4]=matchrow[4]+deck1mw
                    matchrow[5]=matchrow[5]+deck1gw
                    matchcheck='Y'
                
            if matchcheck=='N':
                output=[match[2],deck1mw,deck1gw,match[4],deck2mw,deck2gw]
                Matches.append(output)
        
with open('Gladiator EMEA Season 3, Week 5 Round 2.csv', newline='') as csvfile:
    allmatches = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in allmatches:
        match = [row[0],row[1],row[2],row[3],row[4],row[5]]
        for n in range(len(match)):
            match[n]=match[n].strip('"')
            
        matchdata=match[5].strip(match[1])
        matchdata=matchdata.strip(match[3])
        matchrecord= [int(s) for s in re.findall(r'-?\d+\.?\d*', matchdata)]
        
        matchbye='N'
        if 'bye' in match[5]:
            matchbye='Y'
        
        
        if match[1]!='Player 1' and matchbye=='N':
            if match[1] in match[5]:
                deck1mw=1
                deck2mw=0
                deck1gw=abs(matchrecord[0])
                deck2gw=abs(matchrecord[1])
            else:
                    deck1mw=0
                    deck2mw=1
                    deck1gw=abs(matchrecord[1])
                    deck2gw=abs(matchrecord[0])

            matchcheck='N'    
            for matchrow in Matches:
                if match[2]==matchrow[0] and match[4]==matchrow[3]:
                   matchrow[1]=matchrow[1]+deck1mw
                   matchrow[2]=matchrow[2]+deck1gw
               
                   matchrow[4]=matchrow[4]+deck2mw
                   matchrow[5]=matchrow[5]+deck2gw
                   matchcheck='Y'
               
                elif match[4]==matchrow[0] and match[2]==matchrow[3]:
                    matchrow[1]=matchrow[1]+deck2mw
                    matchrow[2]=matchrow[2]+deck2gw
                
                    matchrow[4]=matchrow[4]+deck1mw
                    matchrow[5]=matchrow[5]+deck1gw
                    matchcheck='Y'
                
            if matchcheck=='N':
                output=[match[2],deck1mw,deck1gw,match[4],deck2mw,deck2gw]
                Matches.append(output)    
                
with open('Gladiator EMEA Season 3, Week 5 Round 3.csv', newline='') as csvfile:
    allmatches = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in allmatches:
        match = [row[0],row[1],row[2],row[3],row[4],row[5]]
        for n in range(len(match)):
            match[n]=match[n].strip('"')
            
        matchdata=match[5].strip(match[1])
        matchdata=matchdata.strip(match[3])
        matchrecord= [int(s) for s in re.findall(r'-?\d+\.?\d*', matchdata)]
        
        matchbye='N'
        if 'bye' in match[5]:
            matchbye='Y'
        
        
        if match[1]!='Player 1' and matchbye=='N':
            if match[1] in match[5]:
                deck1mw=1
                deck2mw=0
                deck1gw=abs(matchrecord[0])
                deck2gw=abs(matchrecord[1])
            else:
                    deck1mw=0
                    deck2mw=1
                    deck1gw=abs(matchrecord[1])
                    deck2gw=abs(matchrecord[0])

            matchcheck='N'    
            for matchrow in Matches:
                if match[2]==matchrow[0] and match[4]==matchrow[3]:
                   matchrow[1]=matchrow[1]+deck1mw
                   matchrow[2]=matchrow[2]+deck1gw
               
                   matchrow[4]=matchrow[4]+deck2mw
                   matchrow[5]=matchrow[5]+deck2gw
                   matchcheck='Y'
               
                elif match[4]==matchrow[0] and match[2]==matchrow[3]:
                    matchrow[1]=matchrow[1]+deck2mw
                    matchrow[2]=matchrow[2]+deck2gw
                
                    matchrow[4]=matchrow[4]+deck1mw
                    matchrow[5]=matchrow[5]+deck1gw
                    matchcheck='Y'
                
            if matchcheck=='N':
                output=[match[2],deck1mw,deck1gw,match[4],deck2mw,deck2gw]
                Matches.append(output)
                
with open('Gladiator EMEA Season 3, Week 5 Round 4.csv', newline='') as csvfile:
    allmatches = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in allmatches:
        match = [row[0],row[1],row[2],row[3],row[4],row[5]]
        for n in range(len(match)):
            match[n]=match[n].strip('"')
            
        matchdata=match[5].strip(match[1])
        matchdata=matchdata.strip(match[3])
        matchrecord= [int(s) for s in re.findall(r'-?\d+\.?\d*', matchdata)]
        
        matchbye='N'
        if 'bye' in match[5]:
            matchbye='Y'
        
        
        if match[1]!='Player 1' and matchbye=='N':
            if match[1] in match[5]:
                deck1mw=1
                deck2mw=0
                deck1gw=abs(matchrecord[0])
                deck2gw=abs(matchrecord[1])
            else:
                    deck1mw=0
                    deck2mw=1
                    deck1gw=abs(matchrecord[1])
                    deck2gw=abs(matchrecord[0])

            matchcheck='N'    
            for matchrow in Matches:
                if match[2]==matchrow[0] and match[4]==matchrow[3]:
                   matchrow[1]=matchrow[1]+deck1mw
                   matchrow[2]=matchrow[2]+deck1gw
               
                   matchrow[4]=matchrow[4]+deck2mw
                   matchrow[5]=matchrow[5]+deck2gw
                   matchcheck='Y'
               
                elif match[4]==matchrow[0] and match[2]==matchrow[3]:
                    matchrow[1]=matchrow[1]+deck2mw
                    matchrow[2]=matchrow[2]+deck2gw
                
                    matchrow[4]=matchrow[4]+deck1mw
                    matchrow[5]=matchrow[5]+deck1gw
                    matchcheck='Y'
                
            if matchcheck=='N':
                output=[match[2],deck1mw,deck1gw,match[4],deck2mw,deck2gw]
                Matches.append(output)
                
with open('Gladiator EMEA Season 3, Week 5 Round 5.csv', newline='') as csvfile:
    allmatches = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in allmatches:
        match = [row[0],row[1],row[2],row[3],row[4],row[5]]
        for n in range(len(match)):
            match[n]=match[n].strip('"')
            
        matchdata=match[5].strip(match[1])
        matchdata=matchdata.strip(match[3])
        matchrecord= [int(s) for s in re.findall(r'-?\d+\.?\d*', matchdata)]
        
        matchbye='N'
        if 'bye' in match[5]:
            matchbye='Y'
        
        
        if match[1]!='Player 1' and matchbye=='N':
            if match[1] in match[5]:
                deck1mw=1
                deck2mw=0
                deck1gw=abs(matchrecord[0])
                deck2gw=abs(matchrecord[1])
            else:
                    deck1mw=0
                    deck2mw=1
                    deck1gw=abs(matchrecord[1])
                    deck2gw=abs(matchrecord[0])

            matchcheck='N'    
            for matchrow in Matches:
                if match[2]==matchrow[0] and match[4]==matchrow[3]:
                   matchrow[1]=matchrow[1]+deck1mw
                   matchrow[2]=matchrow[2]+deck1gw
               
                   matchrow[4]=matchrow[4]+deck2mw
                   matchrow[5]=matchrow[5]+deck2gw
                   matchcheck='Y'
               
                elif match[4]==matchrow[0] and match[2]==matchrow[3]:
                    matchrow[1]=matchrow[1]+deck2mw
                    matchrow[2]=matchrow[2]+deck2gw
                
                    matchrow[4]=matchrow[4]+deck1mw
                    matchrow[5]=matchrow[5]+deck1gw
                    matchcheck='Y'
                
            if matchcheck=='N':
                output=[match[2],deck1mw,deck1gw,match[4],deck2mw,deck2gw]
                Matches.append(output)
                
                
with open('Gladiator AM Season 3, Week 5 Round 1.csv', newline='') as csvfile:
    allmatches = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in allmatches:
        match = [row[0],row[1],row[2],row[3],row[4],row[5]]
        for n in range(len(match)):
            match[n]=match[n].strip('"')
            
        matchdata=match[5].strip(match[1])
        matchdata=matchdata.strip(match[3])
        matchrecord= [int(s) for s in re.findall(r'-?\d+\.?\d*', matchdata)]
        
        matchbye='N'
        if 'bye' in match[5]:
            matchbye='Y'
        
        
        if match[1]!='Player 1' and matchbye=='N':
            if match[1] in match[5]:
                deck1mw=1
                deck2mw=0
                deck1gw=abs(matchrecord[0])
                deck2gw=abs(matchrecord[1])
            else:
                    deck1mw=0
                    deck2mw=1
                    deck1gw=abs(matchrecord[1])
                    deck2gw=abs(matchrecord[0])

            matchcheck='N'    
            for matchrow in Matches:
                if match[2]==matchrow[0] and match[4]==matchrow[3]:
                   matchrow[1]=matchrow[1]+deck1mw
                   matchrow[2]=matchrow[2]+deck1gw
               
                   matchrow[4]=matchrow[4]+deck2mw
                   matchrow[5]=matchrow[5]+deck2gw
                   matchcheck='Y'
               
                elif match[4]==matchrow[0] and match[2]==matchrow[3]:
                    matchrow[1]=matchrow[1]+deck2mw
                    matchrow[2]=matchrow[2]+deck2gw
                
                    matchrow[4]=matchrow[4]+deck1mw
                    matchrow[5]=matchrow[5]+deck1gw
                    matchcheck='Y'
                
            if matchcheck=='N':
                output=[match[2],deck1mw,deck1gw,match[4],deck2mw,deck2gw]
                Matches.append(output)
        
with open('Gladiator AM Season 3, Week 5 Round 2.csv', newline='') as csvfile:
    allmatches = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in allmatches:
        match = [row[0],row[1],row[2],row[3],row[4],row[5]]
        for n in range(len(match)):
            match[n]=match[n].strip('"')
            
        matchdata=match[5].strip(match[1])
        matchdata=matchdata.strip(match[3])
        matchrecord= [int(s) for s in re.findall(r'-?\d+\.?\d*', matchdata)]
        
        matchbye='N'
        if 'bye' in match[5]:
            matchbye='Y'
        
        
        if match[1]!='Player 1' and matchbye=='N':
            if match[1] in match[5]:
                deck1mw=1
                deck2mw=0
                deck1gw=abs(matchrecord[0])
                deck2gw=abs(matchrecord[1])
            else:
                    deck1mw=0
                    deck2mw=1
                    deck1gw=abs(matchrecord[1])
                    deck2gw=abs(matchrecord[0])

            matchcheck='N'    
            for matchrow in Matches:
                if match[2]==matchrow[0] and match[4]==matchrow[3]:
                   matchrow[1]=matchrow[1]+deck1mw
                   matchrow[2]=matchrow[2]+deck1gw
               
                   matchrow[4]=matchrow[4]+deck2mw
                   matchrow[5]=matchrow[5]+deck2gw
                   matchcheck='Y'
               
                elif match[4]==matchrow[0] and match[2]==matchrow[3]:
                    matchrow[1]=matchrow[1]+deck2mw
                    matchrow[2]=matchrow[2]+deck2gw
                
                    matchrow[4]=matchrow[4]+deck1mw
                    matchrow[5]=matchrow[5]+deck1gw
                    matchcheck='Y'
                
            if matchcheck=='N':
                output=[match[2],deck1mw,deck1gw,match[4],deck2mw,deck2gw]
                Matches.append(output)    
                
with open('Gladiator AM Season 3, Week 5 Round 3.csv', newline='') as csvfile:
    allmatches = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in allmatches:
        match = [row[0],row[1],row[2],row[3],row[4],row[5]]
        for n in range(len(match)):
            match[n]=match[n].strip('"')
            
        matchdata=match[5].strip(match[1])
        matchdata=matchdata.strip(match[3])
        matchrecord= [int(s) for s in re.findall(r'-?\d+\.?\d*', matchdata)]
        
        matchbye='N'
        if 'bye' in match[5]:
            matchbye='Y'
        
        
        if match[1]!='Player 1' and matchbye=='N':
            if match[1] in match[5]:
                deck1mw=1
                deck2mw=0
                deck1gw=abs(matchrecord[0])
                deck2gw=abs(matchrecord[1])
            else:
                    deck1mw=0
                    deck2mw=1
                    deck1gw=abs(matchrecord[1])
                    deck2gw=abs(matchrecord[0])

            matchcheck='N'    
            for matchrow in Matches:
                if match[2]==matchrow[0] and match[4]==matchrow[3]:
                   matchrow[1]=matchrow[1]+deck1mw
                   matchrow[2]=matchrow[2]+deck1gw
               
                   matchrow[4]=matchrow[4]+deck2mw
                   matchrow[5]=matchrow[5]+deck2gw
                   matchcheck='Y'
               
                elif match[4]==matchrow[0] and match[2]==matchrow[3]:
                    matchrow[1]=matchrow[1]+deck2mw
                    matchrow[2]=matchrow[2]+deck2gw
                
                    matchrow[4]=matchrow[4]+deck1mw
                    matchrow[5]=matchrow[5]+deck1gw
                    matchcheck='Y'
                
            if matchcheck=='N':
                output=[match[2],deck1mw,deck1gw,match[4],deck2mw,deck2gw]
                Matches.append(output)
                
with open('Gladiator AM Season 3, Week 5 Round 4.csv', newline='') as csvfile:
    allmatches = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in allmatches:
        match = [row[0],row[1],row[2],row[3],row[4],row[5]]
        for n in range(len(match)):
            match[n]=match[n].strip('"')
            
        matchdata=match[5].strip(match[1])
        matchdata=matchdata.strip(match[3])
        matchrecord= [int(s) for s in re.findall(r'-?\d+\.?\d*', matchdata)]
        
        matchbye='N'
        if 'bye' in match[5]:
            matchbye='Y'
        
        
        if match[1]!='Player 1' and matchbye=='N':
            if match[1] in match[5]:
                deck1mw=1
                deck2mw=0
                deck1gw=abs(matchrecord[0])
                deck2gw=abs(matchrecord[1])
            else:
                    deck1mw=0
                    deck2mw=1
                    deck1gw=abs(matchrecord[1])
                    deck2gw=abs(matchrecord[0])

            matchcheck='N'    
            for matchrow in Matches:
                if match[2]==matchrow[0] and match[4]==matchrow[3]:
                   matchrow[1]=matchrow[1]+deck1mw
                   matchrow[2]=matchrow[2]+deck1gw
               
                   matchrow[4]=matchrow[4]+deck2mw
                   matchrow[5]=matchrow[5]+deck2gw
                   matchcheck='Y'
               
                elif match[4]==matchrow[0] and match[2]==matchrow[3]:
                    matchrow[1]=matchrow[1]+deck2mw
                    matchrow[2]=matchrow[2]+deck2gw
                
                    matchrow[4]=matchrow[4]+deck1mw
                    matchrow[5]=matchrow[5]+deck1gw
                    matchcheck='Y'
                
            if matchcheck=='N':
                output=[match[2],deck1mw,deck1gw,match[4],deck2mw,deck2gw]
                Matches.append(output)
                
with open('Gladiator AM Season 3, Week 5 Round 5.csv', newline='') as csvfile:
    allmatches = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in allmatches:
        match = [row[0],row[1],row[2],row[3],row[4],row[5]]
        for n in range(len(match)):
            match[n]=match[n].strip('"')
            
        matchdata=match[5].strip(match[1])
        matchdata=matchdata.strip(match[3])
        matchrecord= [int(s) for s in re.findall(r'-?\d+\.?\d*', matchdata)]
        
        matchbye='N'
        if 'bye' in match[5]:
            matchbye='Y'
        
        
        if match[1]!='Player 1' and matchbye=='N':
            if match[1] in match[5]:
                deck1mw=1
                deck2mw=0
                deck1gw=abs(matchrecord[0])
                deck2gw=abs(matchrecord[1])
            else:
                    deck1mw=0
                    deck2mw=1
                    deck1gw=abs(matchrecord[1])
                    deck2gw=abs(matchrecord[0])

            matchcheck='N'    
            for matchrow in Matches:
                if match[2]==matchrow[0] and match[4]==matchrow[3]:
                   matchrow[1]=matchrow[1]+deck1mw
                   matchrow[2]=matchrow[2]+deck1gw
               
                   matchrow[4]=matchrow[4]+deck2mw
                   matchrow[5]=matchrow[5]+deck2gw
                   matchcheck='Y'
               
                elif match[4]==matchrow[0] and match[2]==matchrow[3]:
                    matchrow[1]=matchrow[1]+deck2mw
                    matchrow[2]=matchrow[2]+deck2gw
                
                    matchrow[4]=matchrow[4]+deck1mw
                    matchrow[5]=matchrow[5]+deck1gw
                    matchcheck='Y'
                
            if matchcheck=='N':
                output=[match[2],deck1mw,deck1gw,match[4],deck2mw,deck2gw]
                Matches.append(output)
                
 
with open('Week5Matchups.csv', 'w') as f:
      

    write = csv.writer(f)
    
    write.writerows(Matches)               