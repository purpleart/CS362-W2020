# -*- coding: utf-8 -*-
"""
File: testDominion2.py
Purpose: Create test scenario in which the game over condition is incorrect and the game ends in an infinite loop
Edited by: Sarah Eastwood
Edited on: January 18, 2020
"""

import Dominion
from testUtility import *

# Get player names and create player objects
player_names = ["Annie","*Ben","*Carla","*David","*Emma","*Frank","*Gina"]
players, num_players = create_players(player_names)

num_victory, num_curse = get_num_victory_curse(num_players)

# Create box of all possible cards that can be in the game
card_box = create_card_box(10, num_victory)

# Pick cards from the box that will be in the supply for this game
supply = create_card_supply(card_box, 5, num_players, num_victory, num_curse)

# Create dictionary of cards in supply (used for printing to the screen)
supply_order = create_supply_order(supply)

# Initialize the trash
trash = []

# Play the game until gameover
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")   
    print_supply(supply, supply_order)
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    play_game(players, supply, trash, turn)

# When the game is over, print game results
print_final_scores(players)
