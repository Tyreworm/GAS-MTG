# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 12:30:22 2021

@author: Graeme
"""


import random

Checklands = ['Rootbound Crag','Hinterland Harbor','Sunpetal Grove','Clifftop Retreat','Glacial Fortress','Isolated Chapel','Drowned Catacomb','Sulfur Falls','Dragonskull Summit','Woodland Cemetery']

turn_of_interest=7
checklandcount=0
targetcheckcount=10000000
check_untapped=0
check_tapped=0
mulligans=0
totalgames=0

deck=[[['Abundant Harvest', 'Sorcery', 'N', 'N']], [['Adanto Vanguard', 'Creature — Vampire Soldier', 'N', 'N']], [['Agonizing Remorse', 'Sorcery', 'N', 'N']], [['Alpine Meadow', 'Snow Land — Mountain Plains', 'Y', 'N']], [['Arctic Treeline', 'Snow Land — Forest Plains', 'Y', 'N']], [["Assassin's Trophy", 'Instant', 'N', 'N']], [['Aurelia, Exemplar of Justice', 'Legendary Creature — Angel', 'N', 'N']], [['Baleful Mastery', 'Instant', 'N', 'N']], [['Blightstep Pathway', 'Land // Land', 'Y', 'N']], [['Blood Crypt', 'Land — Swamp Mountain', 'Y', 'N']], [["Bloodchief's Thirst", 'Sorcery', 'N', 'N']], [['Blooming Marsh', 'Land', 'Y', 'N']], [['Bonecrusher Giant', 'Creature — Giant // Instant — Adventure', 'N', 'N']], [['Brightclimb Pathway', 'Land // Land', 'Y', 'N']], [['Castle Locthwain', 'Land', 'Y', 'N']], [['Cave of the Frost Dragon', 'Land', 'Y', 'N']], [['Chandra, Torch of Defiance', 'Legendary Planeswalker — Chandra', 'N', 'N']], [['Clifftop Retreat', 'Land', 'Y', 'Y', ['Plains', 'Mountain']]], [['Cling to Dust', 'Instant', 'N', 'N']], [['Concealed Courtyard', 'Land', 'Y', 'N']], [['Cragcrown Pathway', 'Land // Land', 'Y', 'N']], [['Darkbore Pathway', 'Land // Land', 'Y', 'N']], [['Demonic Tutor', 'Sorcery', 'N', 'N']], [['Den of the Bugbear', 'Land', 'Y', 'N']], [['Dire Fleet Daredevil', 'Creature — Human Pirate', 'N', 'N']], [['Domri, Anarch of Bolas', 'Legendary Planeswalker — Domri', 'N', 'N']], [['Doom Blade', 'Instant', 'N', 'N']], [['Dragonkin Berserker', 'Creature — Human Berserker', 'N', 'N']], [['Dragonskull Summit', 'Land', 'Y', 'Y', ['Mountain', 'Swamp']]], [["Dromoka's Command", 'Instant', 'N', 'N']], [['Duress', 'Sorcery', 'N', 'N']], [['Elder Gargaroth', 'Creature — Beast', 'N', 'N']], [["Erebos's Intervention", 'Instant', 'N', 'N']], [['Fabled Passage', 'Land - Mountain Swamp Plains Forest Island', 'Y', 'N']], [['Fatal Push', 'Instant', 'N', 'N']], [['Forest', 'Basic Land — Forest', 'Y', 'N']], [['Gilded Goose', 'Creature — Bird', 'N', 'N']], [['Glint-Sleeve Siphoner', 'Creature — Human Rogue', 'N', 'N']], [['Glorybringer', 'Creature — Dragon', 'N', 'N']], [['Godless Shrine', 'Land — Plains Swamp', 'Y', 'N']], [['Gruul Spellbreaker', 'Creature — Ogre Warrior', 'N', 'N']], [['Hazoret the Fervent', 'Legendary Creature — God', 'N', 'N']], [['Highland Forest', 'Snow Land — Mountain Forest', 'Y', 'N']], [['Immersturm Predator', 'Creature — Vampire Dragon', 'N', 'N']], [['Indatha Triome', 'Land — Plains Swamp Forest', 'Y', 'N']], [['Inquisition of Kozilek', 'Sorcery', 'N', 'N']], [['Inspiring Vantage', 'Land', 'Y', 'N']], [['Isolated Chapel', 'Land', 'Y', 'Y', ['Plains', 'Swamp']]], [['Ketria Triome', 'Land — Forest Island Mountain', 'Y', 'N']], [['Klothys, God of Destiny', 'Legendary Enchantment Creature — God', 'N', 'N']], [['Knight of Autumn', 'Creature — Dryad Knight', 'N', 'N']], [['Knight of the Ebon Legion', 'Creature — Vampire Knight', 'N', 'N']], [["Kolaghan's Command", 'Instant', 'N', 'N']], [['Kunoros, Hound of Athreos', 'Legendary Creature — Dog', 'N', 'N']], [['Legion Warboss', 'Creature — Goblin Soldier', 'N', 'N']], [['Lightning Bolt', 'Instant', 'N', 'N']], [['Lightning Helix', 'Instant', 'N', 'N']], [['Lightning Strike', 'Instant', 'N', 'N']], [['Lotus Cobra', 'Creature — Snake', 'N', 'N']], [['Maelstrom Pulse', 'Sorcery', 'N', 'N']], [['Minsc, Beloved Ranger', 'Legendary Creature — Human Ranger', 'N', 'N']], [['Mountain', 'Basic Land — Mountain', 'Y', 'N']], [['Mythos of Nethroi', 'Instant', 'N', 'N']], [['Once Upon a Time', 'Instant', 'N', 'N']], [['Orcus, Prince of Undeath', 'Legendary Creature — Demon', 'N', 'N']], [['Overgrown Tomb', 'Land — Swamp Forest', 'Y', 'N']], [['Paradise Druid', 'Creature — Elf Druid', 'N', 'N']], [['Plains', 'Basic Land — Plains', 'Y', 'N']], [['Questing Beast', 'Legendary Creature — Beast', 'N', 'N']], [['Radha, Heart of Keld', 'Legendary Creature — Elf Warrior', 'N', 'N']], [['Ranger Class', 'Enchantment — Class', 'N', 'N']], [['Rankle, Master of Pranks', 'Legendary Creature — Faerie Rogue', 'N', 'N']], [['Reidane, God of the Worthy', 'Legendary Creature — God // Legendary Artifact', 'N', 'N']], [['Rip Apart', 'Sorcery', 'N', 'N']], [['Robber of the Rich', 'Creature — Human Archer Rogue', 'N', 'N']], [['Rootbound Crag', 'Land', 'Y', 'Y', ['Mountain', 'Forest']]], [['Rotting Regisaur', 'Creature — Zombie Dinosaur', 'N', 'N']], [['Sacred Foundry', 'Land — Mountain Plains', 'Y', 'N']], [['Savai Triome', 'Land — Mountain Plains Swamp', 'Y', 'N']], [['Scavenging Ooze', 'Creature — Ooze', 'N', 'N']], [['Sedgemoor Witch', 'Creature — Human Warlock', 'N', 'N']], [['Shatterskull Smashing', 'Sorcery // Land', 'Y', 'N']], [['Shock', 'Instant', 'N', 'N']], [['Showdown of the Skalds', 'Enchantment — Saga', 'N', 'N']], [['Snowfield Sinkhole', 'Snow Land — Plains Swamp', 'Y', 'N']], [['Soul Shatter', 'Instant', 'N', 'N']], [['Stomping Ground', 'Land — Mountain Forest', 'Y', 'N']], [['Sulfurous Mire', 'Snow Land — Swamp Mountain', 'Y', 'N']], [['Sunpetal Grove', 'Land', 'Y', 'Y', ['Plains', 'Forest']]], [['Swamp', 'Basic Land — Swamp', 'Y', 'N']], [['Swords to Plowshares', 'Instant', 'N', 'N']], [['Tainted Pact', 'Instant', 'N', 'N']], [['Temple Garden', 'Land — Forest Plains', 'Y', 'N']], [['Thoughtseize', 'Sorcery', 'N', 'N']], [['Valentin, Dean of the Vein', 'Legendary Creature — Vampire Warlock // Legendary Creature — Human Druid', 'N', 'N']], [['Valki, God of Lies', 'Legendary Creature — God // Legendary Planeswalker — Tibalt', 'N', 'N']], [['Vanishing Verse', 'Instant', 'N', 'N']], [['Woodland Cemetery', 'Land', 'Y', 'Y', ['Swamp', 'Forest']]], [['Woodland Chasm', 'Snow Land — Swamp Forest', 'Y', 'N']], [['Zagoth Triome', 'Land — Swamp Forest Island', 'Y', 'N']]]
    
    
def draw():
    return active_deck.pop(random.randint(0, len(active_deck)-1))[0]
    

while checklandcount<targetcheckcount:
    totalgames=totalgames+1  
    
    print(checklandcount)
    
    valid_hand='N'

    while valid_hand=='N':
        active_deck=deck.copy()
        hand_lands=0
        hand=[]
        for opening_draw in range(7):
            card=draw()
            hand.append(card)
            if 'Land' in card[1]:
                hand_lands=hand_lands+1
                
            
        if hand_lands>2 and hand_lands<5:    
            valid_hand='Y'
        else:
            mulligans=mulligans+1
    
    lands_in_play=[]
    lands_in_play_names=[]
    
    for turn in range(turn_of_interest):
        nonchecklands_in_hand=[]
        checklands_in_hand=[]
        targettypes=[]
        land_played='N'
        new_card=draw()
        hand.append(new_card)
        hand.sort(key = lambda x: x[2])
        for card in hand:
            if card[2]=='Y':
                if card[3]=='Y':
                    checklands_in_hand.append(card)
                    targettypes.append(card[4][0])
                    targettypes.append(card[4][1])
                else:
                    nonchecklands_in_hand.append(card)
                    
        if turn==(turn_of_interest-1):
            if len(checklands_in_hand)!=0:
                for land in checklands_in_hand:
                    typecheck=land[4]
                    for landtype in typecheck:
                        for playedtype in lands_in_play:
                            if landtype in playedtype and land_played=='N':
                                playedcard=land
                                hand.remove(playedcard)
                                typecheck=playedcard[4]
                                lands_in_play.append(playedcard[1])
                                lands_in_play_names.append(playedcard[0])
                                land_played='Y'  
                                check_untapped=check_untapped+1
                                checklandcount=checklandcount+1
                                
                if land_played=='N':
                    playedcard=checklands_in_hand.pop(0) 
                    hand.remove(playedcard)
                    typecheck=playedcard[4]
                    lands_in_play.append(playedcard[1])
                    lands_in_play_names.append(playedcard[0])
                    check_tapped=check_tapped+1
                    checklandcount=checklandcount+1
            # else:
            #      print('No Check Drawn')
                
        else:
            if len(nonchecklands_in_hand)!=0:
               for land in nonchecklands_in_hand:
                   
                   if len(targettypes)!=0:
                       for landtype in targettypes:
                           if landtype in land[1]:
                             playedcard=land
                             land_played='Y'  
                   else:    
                       if land_played=='N':
                           if 'Forest' in land[1] or 'Mountain' in land[1] or 'Plains' in land[1] or 'Island' in land[1] or 'Swamp' in land[1] or land[0]=='Fabled Passage':
                               playedcard=land
                               land_played='Y'
                               
               if land_played=='N': 
                   playedcard=nonchecklands_in_hand.pop(0) 
                   land_played='Y'
                   
               hand.remove(playedcard)
               if playedcard[0]=='Fabled Passage':
                   playedcard[1]= 'Land - Mountain Swamp Plains Forest Island'
               lands_in_play.append(playedcard[1])
               lands_in_play_names.append(playedcard[0])
        
        
        
        
        
        
        