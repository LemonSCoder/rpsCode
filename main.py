######
# CSE Project 3.2.5 Strategy Game: PS Rock
#
# Execute this file mainy.py to play a tournament.
# psrock.py implements the round robin tournament of rock paper scissors
# 
# Prior to execution:
# Line 22: Type each team's module name (the file name, but without the py) 
# on the import statement,
# Lines 27-30: Create a reload() statement for each module, and
# Original line 36: Place each module name as an arugment to the function 
# psrock.round_robin().
# Each player should have their own .py file containing 
# a function called move(my_history, their_history)
# These filenames (without the .py extension) are passed to the 
# round_robin() function as the 2nd, 3rd, etc. arguments.
#
#######

import psrock
import importlib
importlib.reload(psrock)

import team1, team2, team3, team4, team5, LightningMcQueen, TomBombadil, amituff, belligol, bestplan, cake_is_great, creed, gambling, w_strat, guppie_the_great, justinfu, letsseeifthisworks, lowEffortCode, lwkytho, neymarjr, psrock, r_p_s, rps_code, wearecooked, welp_I_tried, winner, wonkynotpredictablesmh # These are file names in this folder
# The reload() statement is needed for each team because import 
# will only compile source code once to create the pyc file and store in memory.
# Without reload(), changes to the .py file will be ignored unless the pyc 
# file is deleted and the kernel restarted. 
importlib.reload(team1) 
importlib.reload(team2)
importlib.reload(team3)
importlib.reload(team4)
importlib.reload(team5)
importlib.reload(LightningMcQueen)
importlib.reload(TomBombadil)
importlib.reload(amituff)
importlib.reload(belligol)
importlib.reload(bestplan)
importlib.reload(cake_is_great)
importlib.reload(creed)
importlib.reload(gambling)
importlib.reload(guppie_the_great)
importlib.reload(justinfu)
importlib.reload(letsseeifthisworks)
importlib.reload(lowEffortCode)
importlib.reload(lwkytho)
importlib.reload(neymarjr)
importlib.reload(r_p_s)
importlib.reload(rps_code)
importlib.reload(wearecooked)
importlib.reload(welp_I_tried)
importlib.reload(winner)
importlib.reload(wonkynotpredictablesmh) 
importlib.reload(wearecooked)
importlib.reload(winningstrat)
importlib.reload(w_strat)

# The first argument of round_robin() specifies the number of 
# rounds to be played by each pair of strategies. 
# Change the other arguments to use more teams, fewer teams, or different teams
short_report, long_report = psrock.round_robin(20, team1, team2, team3, team4, team5, LightningMcQueen, TomBombadil, amituff, belligol, bestplan, cake_is_great, creed, gambling, guppie_the_great, justinfu, letsseeifthisworks, lowEffortCode, lwkytho, neymarjr, r_p_s, rps_code, wearecooked, welp_I_tried, winner, wonkynotpredictablesmh)

for team in long_report:
    print('-'*80)
    print(long_report[team])
    
print(short_report)
