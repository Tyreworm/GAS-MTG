# -*- coding: utf-8 -*-
"""
Created on Mon May 10 16:27:14 2021

@author: Graeme
"""
import csv

Matches=[['Deck 1','Deck 1 MWs','Deck 1 GWs','Deck 2','Deck 2 MWs','Deck 2 GWs']]

with open('Week2Matchups.csv', newline='') as csvfile:
    allmatches = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in allmatches:
        if len(row)!=0 and row[0]!='Deck 1':
            match = [row[0],row[1],row[2],row[3],row[4],row[5]]
            match[1]=float(match[1])
            match[2]=float(match[2])
            match[4]=float(match[4])
            match[5]=float(match[5])
            
            matchcheck='N'    
            for matchrow in Matches:
                if match[1]==matchrow[0] and match[3]==matchrow[3]:
                   matchrow[1]=matchrow[1]+match[1]
                   matchrow[2]=matchrow[2]+match[2]
               
                   matchrow[4]=matchrow[4]+match[4]
                   matchrow[5]=matchrow[5]+match[5]
                   matchcheck='Y'
               
                elif match[3]==matchrow[0] and match[1]==matchrow[3]:
                    matchrow[1]=matchrow[1]+match[4]
                    matchrow[2]=matchrow[2]+match[5]
                
                    matchrow[4]=matchrow[4]+match[1]
                    matchrow[5]=matchrow[5]+match[2]
                    matchcheck='Y'
                
            if matchcheck=='N':
                output=[match[0],match[1],match[2],match[3],match[4],match[5]]
                Matches.append(output)
                
                
with open('Week3Matchups.csv', newline='') as csvfile:
    allmatches = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in allmatches:
        if len(row)!=0 and row[0]!='Deck 1':
            match = [row[0],row[1],row[2],row[3],row[4],row[5]]
            match[1]=float(match[1])
            match[2]=float(match[2])
            match[4]=float(match[4])
            match[5]=float(match[5])
            
            matchcheck='N'    
            for matchrow in Matches:
                if match[0]==matchrow[0] and match[3]==matchrow[3]:
                   matchrow[1]=matchrow[1]+match[1]
                   matchrow[2]=matchrow[2]+match[2]
               
                   matchrow[4]=matchrow[4]+match[4]
                   matchrow[5]=matchrow[5]+match[5]
                   matchcheck='Y'
               
                elif match[3]==matchrow[0] and match[0]==matchrow[3]:
                    matchrow[1]=matchrow[1]+match[4]
                    matchrow[2]=matchrow[2]+match[5]
                
                    matchrow[4]=matchrow[4]+match[1]
                    matchrow[5]=matchrow[5]+match[2]
                    matchcheck='Y'
                
            if matchcheck=='N':
                output=[match[0],match[1],match[2],match[3],match[4],match[5]]
                Matches.append(output)             
                
                
with open('OverallMatchups.csv', 'w') as f:
      

    write = csv.writer(f)
    
    write.writerows(Matches)                      
                
