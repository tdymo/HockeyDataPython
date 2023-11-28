import csv

def get_games_played(player_or_team = "TEAM"):
    #This defaults to team in order to give games played by the team.
    #If a player or goalie is input, it will only give the number of games they have played in.
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

def get_team_goals_for():
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

def get_team_goals_against():
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

def get_players():
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
def get_goalies():
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

def get_player_goals_and_assists(player):
    #Using a player name as the parameter, the function returns the list [goals, assists]
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

def get_goalie_GA_SA_SA(goalie):
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


