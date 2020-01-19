"""
File: testUtility.py
Purpose: Contains common functions that are used to play Dominion
Refactored by: Sarah Eastwood
Date: January 18, 2020
"""
import Dominion
import random
from collections import defaultdict 

def create_players(player_names):
    #Costruct the Player objects
    players = []
    num_players = len(player_names)
    for name in player_names:
        if name[0]=="*":
            players.append(Dominion.ComputerPlayer(name[1:]))
        elif name[0]=="^":
            players.append(Dominion.TablePlayer(name[1:]))
        else:
            players.append(Dominion.Player(name))

    return players, num_players

def get_num_victory_curse(num_players):
    #number of curses and victory cards
    if num_players > 2:
        num_victory = 12
    else:
        num_victory = 8
    num_curse = -10 + 10 * num_players
        
    return num_victory, num_curse

def create_supply_order(supply):
    supply_order = defaultdict(list)
    for card in supply:
        card_cost = supply[card][0].cost
        card_name = supply[card][0].name
        supply_order[card_cost].append(card_name) 

    return supply_order
        

def create_card_box(default_num_cards, num_victory):
    #Define box
    box = {}
    box["Woodcutter"]=[Dominion.Woodcutter()]*default_num_cards
    box["Smithy"]=[Dominion.Smithy()]*default_num_cards
    box["Laboratory"]=[Dominion.Laboratory()]*default_num_cards
    box["Village"]=[Dominion.Village()]*default_num_cards
    box["Festival"]=[Dominion.Festival()]*default_num_cards
    box["Market"]=[Dominion.Market()]*default_num_cards
    box["Chancellor"]=[Dominion.Chancellor()]*default_num_cards
    box["Workshop"]=[Dominion.Workshop()]*default_num_cards
    box["Moneylender"]=[Dominion.Moneylender()]*default_num_cards
    box["Chapel"]=[Dominion.Chapel()]*default_num_cards
    box["Cellar"]=[Dominion.Cellar()]*default_num_cards
    box["Remodel"]=[Dominion.Remodel()]*default_num_cards
    box["Adventurer"]=[Dominion.Adventurer()]*default_num_cards
    box["Feast"]=[Dominion.Feast()]*default_num_cards
    box["Mine"]=[Dominion.Mine()]*default_num_cards
    box["Library"]=[Dominion.Library()]*default_num_cards
    box["Gardens"]=[Dominion.Gardens()]*num_victory
    box["Moat"]=[Dominion.Moat()]*default_num_cards
    box["Council Room"]=[Dominion.Council_Room()]*default_num_cards
    box["Witch"]=[Dominion.Witch()]*default_num_cards
    box["Bureaucrat"]=[Dominion.Bureaucrat()]*default_num_cards
    box["Militia"]=[Dominion.Militia()]*default_num_cards
    box["Spy"]=[Dominion.Spy()]*default_num_cards
    box["Thief"]=[Dominion.Thief()]*default_num_cards
    box["Throne Room"]=[Dominion.Throne_Room()]*default_num_cards

    return box

def create_card_supply(card_box, num_card_types, num_players, num_victory, num_curse):
    #Pick cards from box to be in the supply.
    box_card_list = [k for k in card_box]
    random.shuffle(box_card_list)
    supply_card_list = box_card_list[:num_card_types]
    supply = defaultdict(list,[(k,card_box[k]) for k in supply_card_list])

    #The supply always has these cards
    supply["Copper"]=[Dominion.Copper()]*(60-num_players*7)
    supply["Silver"]=[Dominion.Silver()]*40
    supply["Gold"]=[Dominion.Gold()]*30
    supply["Estate"]=[Dominion.Estate()]*num_victory
    supply["Duchy"]=[Dominion.Duchy()]*num_victory
    supply["Province"]=[Dominion.Province()]*num_victory
    supply["Curse"]=[Dominion.Curse()]*num_curse

    return supply

def print_supply(supply, supply_order):
    for value in sorted(supply_order):
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))

def play_game(players, supply, trash, turn):
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)

def print_final_scores(players):
    #Final score
    dcs=Dominion.cardsummaries(players)
    vp=dcs.loc['VICTORY POINTS']
    vpmax=vp.max()
    winners=[]
    for i in vp.index:
        if vp.loc[i]==vpmax:
            winners.append(i)
    if len(winners)>1:
        winstring= ' and '.join(winners) + ' win!'
    else:
        winstring = ' '.join([winners[0],'wins!'])

    print("\nGAME OVER!!!\n"+winstring+"\n")
    print(dcs)

