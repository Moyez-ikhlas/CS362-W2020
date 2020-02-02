# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 15:42:42 2020

@author: Moyez Ikhlas
"""

import Dominion
import random
from collections import defaultdict
import testUtility as tu


#Get player names
# player_names = tu.get_player_names()
player_names = ["Annie"]


#number of curses and victory cards
nC, nV = tu.get_nc_nv(player_names)

#Define box
box = tu.get_box(nV)

supply_order = tu.get_supply_order()

#Pick 10 cards from box to be in the supply.
supply10 = tu.pick_cards(box)

# The supply always has these cards
supply = tu.supply_cards_mandatory(supply10, nC, nV, player_names)


#initialize the trash
trash = tu.init_trash()


#Costruct the Player objects
players = tu.player_objects(player_names)

#Play the game
tu.play_game(supply, supply_order, players, trash)