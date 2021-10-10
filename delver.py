# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 12:30:22 2021

@author: Graeme
"""


import random

Lands=38
Flip_Spells=40
NonFlip_Spells=(99-Lands)-Flip_Spells

deck=["Delver"]

for n in range(Lands):
    deck.append("Land")

for n in range(Flip_Spells):
    deck.append("FlipSpell")

for n in range(NonFlip_Spells):
    deck.append("NonFlipSpell")
    
    
def draw():
    return active_deck.pop(random.randint(0, len(active_deck)-1))

Target_Sims=10000000
turn_of_interest=4
Flip_storage=[0,0,0]
No_Flip_storage=[0,0,0]


Completed_Sims=0
Flips=0
No_Flips=0
mulligans=0
totalgames=0

while Completed_Sims<Target_Sims:
     
    print(round(((Completed_Sims/Target_Sims)*100),2))
    
    valid_hand='N'   
    while valid_hand=='N':
        DelverHand='N'
        active_deck=deck.copy()
        hand_lands=0
        hand=[]
        for opening_draw in range(7):
            card=draw()
            hand.append(card)
            if 'Land' in card:
                hand_lands=hand_lands+1
            if 'Delver' in card:
                DelverHand='Y'   
        
        if hand_lands>1 and hand_lands<5 and DelverHand=='Y':    
            valid_hand='Y'    
        else:
            mulligans=mulligans+1
    
    flipped='N'
    
    for turn in range(turn_of_interest):
        
        new_card=draw()
        hand.append(new_card)
        
        if turn!=0:
            if new_card=="FlipSpell" or flipped=='Y':
              Flip_storage[turn-1]=Flip_storage[turn-1]+1
              flipped='Y'
            else:
               No_Flip_storage[turn-1]=No_Flip_storage[turn-1]+1
    
               
    Completed_Sims=Completed_Sims+1       
            

        
        
        
        
        
        
        