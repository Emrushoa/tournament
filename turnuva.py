# This is a simple program that simulates a tournament of 4 teams


from itertools import combinations
from random import randint

class Team:
    def __init__(self, team_name, game_played, game_won, game_lost, game_draw, goal_scored, goal_conceded):
        self.team_name = team_name
        self.game_played = game_played
        self.game_won = game_won
        self.game_lost = game_lost
        self.game_draw = game_draw
        self.goal_scored = goal_scored
        self.gol_conceded = goal_conceded
def team_aver(goal_scored,goal_conceded):
    team_aver = goal_scored - goal_conceded

#Başlangıç Parametreleri
game_played = 0
game_won = 0
game_lost = 0
game_draw = 0
goal_scored = 0
goal_conceded = 0
team_number = 0
team_list=[]


# Team Generation
print('Please Define 4 Teams for the Mimi Tournament:')
while team_number <4:
    team_name=input('Input a Team Name: ')
    team_number += 1
    team_var=Team(team_name,game_played,game_won,game_lost,game_draw,goal_conceded,goal_conceded)
    team_list.append(team_name)
else:
    print('Below are the 4 teams that attend Mimi Tournament:')
    print(team_list)
    print('Matchs are Starting')
    print('First Leg Games & Results')

# Games with Combination & Results with Random

game_list = combinations(team_list,2)
for game in game_list:
    score = randint(0,5),randint(0,5)
    print(game)
    print(score)
else:
    print('maçlar sona erdi')

    