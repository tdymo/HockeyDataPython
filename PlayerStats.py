import csv
from typing import List, Tuple
def get_games_played(player_or_team: str = "TEAM") -> int:
    """
    This function takes in a string as input and returns an integer.
    The String must be from the player or goalie list.
    If no input is provided, the parameter is defaulted to "TEAM".
    
    The function reads through Rangers Game Stats.txt in order to count the games played by the team or player.
    It returns an integer value for games_played  
    """
    games_played = 0
    infile = open('Rangers Game Stats.txt', 'r')
    if player_or_team == "TEAM":
        for line in infile:
            if line.startswith("Game "):
                games_played += 1
    elif player_or_team in get_players():
        for line in infile:
            if line.startswith(f"Player: {player_or_team}"):
                games_played += 1
    elif player_or_team in get_goalies():
        for line in infile:
            if line.startswith(f"Goalie: {player_or_team}"):
                games_played += 1
    
    infile.close()
    return games_played

def get_team_goals_for() -> int:
    """
    This function takes in no input
    The function reads through Rangers Game Stats.txt in order to count the goals scored for
    It returns this value as an integer.
    """
    Goals_For = 0
    infile = open('Rangers Game Stats.txt', 'r')
    for line in infile:
        if line.startswith("Game "):
            elements = line.split()
            string = elements[3]
            goals = int(string[1])
            Goals_For += goals
    infile.close()
    return Goals_For

def get_team_goals_against() -> int:
    """
    This function takes in no input
    The function reads through Rangers Game Stats.txt in order to count the goals scored against
    It returns this value as an integer.
    """
    Goals_Against = 0
    infile = open('Rangers Game Stats.txt', 'r')
    for line in infile:
        if line.startswith("Game "):
            elements = line.split()
            string = elements[-1]
            goals = int(string[1])
            Goals_Against += goals
    infile.close()
    return Goals_Against

def get_players() -> List[str]:
    """
    This function takes in no input
    The function reads through Rangers Game Stats.txt in order to create a list containing all of the players
    The function adds names to the list Players and returns this list.
    """
    Players = []
    infile = open('Rangers Game Stats.txt', 'r')
    for line in infile:
        if line.startswith("Player: "):
            elements = line.split()
            name = elements[1] + " " + elements[2]
            if name not in Players:
                Players.append(name)       
    infile.close()
    return Players

def get_goalies() -> List[str]:
    """
    This function takes in no input
    The function reads through Rangers Game Stats.txt in order to create a list containing all of the goalies
    The function adds names to the list Goalies and returns this list.
    """
    Goalies = []
    infile = open('Rangers Game Stats.txt', 'r')
    for line in infile:
        if line.startswith("Goalie: "):
            elements = line.split()
            name = elements[1] + " " + elements[2]
            if name not in Goalies:
                Goalies.append(name)        
    infile.close()
    return Goalies

def get_player_goals_and_assists(player: str) -> Tuple[int, int]:
    """
    This function takes in a player (string) as input.
    The function reads through Rangers Game Stats.txt in order to count the goals and assists by that player.
    The function returns a Tuple with integer values in the form (season_goals, season_assists).
    """
    
    season_goals = 0
    season_assists = 0
    infile = open('Rangers Game Stats.txt', 'r')
    for line in infile:
        if line.startswith("Player: "):
            elements = line.split()
            name = elements[1] + " " + elements[2]
            if name == player:
                goal_string = elements[4]
                assist_string = elements[-1]
                goals = int(goal_string[-1])
                assists = int(assist_string[-1])
                season_goals += goals
                season_assists += assists
    infile.close()
    return season_goals, season_assists

def get_goalie_GA_SA_SV(goalie: str) -> Tuple[int, int, int]:
    """
    This function takes in a goalie (string) as input.
    The function reads through Rangers Game Stats.txt in order to count the goals against, shots against, and saves made by that goalie.
    The function returns a Tuple with integer values in the form (season_GA, season_SA, season_SV).
    """
    
    season_GA = 0
    season_SA = 0
    season_SV = 0
    infile = open('Rangers Game Stats.txt', 'r')
    for line in infile:
        if line.startswith("Goalie: "):
            elements = line.split()
            name = elements[1] + " " + elements[2]
            if name == goalie:
                GA_string = elements[5]
                SA_string = elements[8]
                SV_string = elements[-1]
                GA = int(GA_string[8:])
                SA = int(SA_string[8:])
                SV = int(SV_string[6:])
                season_GA += GA
                season_SA += SA
                season_SV += SV
    infile.close()
    return season_GA, season_SA, season_SV


