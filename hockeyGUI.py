import tkinter
from PlayerStats import *


class hockeyGUI:
    def __init__(self, window):
        self.window = window
    
        self.header_label = tkinter.Label(window, text = "Welcome to the 2023-2024 stat book. What would you like to see?")
        self.header_label.pack()

        self.Search_Player_Button = tkinter.Button(window, text = "Player Stats", command = self.ps_clicked)
        self.Search_Player_Button.pack()
        self.Team_Button = tkinter.Button(window, text = "Team Stats", command = self.ts_clicked)
        self.Team_Button.pack()
        
        
        
        
    def ps_clicked(self):
        
        #this code should execute when the user selects the Player Stats Button
        self.header_label.config(text = "Select a Player to see Stats")
        self.Search_Player_Button.pack_forget()
        self.Team_Button.pack_forget()
        
        self.player_var = tkinter.StringVar(self.window)
        self.player_var.set("Select a Player")
        self.Player_List_Dropdown = tkinter.OptionMenu(self.window, self.player_var, *(get_players() + get_goalies()))
        self.Player_List_Dropdown.pack()
        self.player_var.trace_add("write", self.update_player_stats)
        
        self.player_stats_label1 = tkinter.Label(self.window, text = "")
        self.player_stats_label1.pack()
        self.player_stats_label2 = tkinter.Label(self.window, text = "")
        self.player_stats_label2.pack()

        
        self.Return_To_Menu_Button = tkinter.Button(self.window, text = "Main Menu", command = self.mmb_clicked_from_player)
        self.Return_To_Menu_Button.pack(side = 'left')
        
    def update_player_stats(self, *args):
        #This code should execute whenever the name in the dropdown menu changes
        selected_player = self.player_var.get()
        if selected_player in get_players():
            goals_assists = get_player_goals_and_assists(self.player_var.get())
            if goals_assists[0] == 1:
                self.player_stats_label1.config(text = f"{selected_player} has scored 1 goal in {get_games_played(selected_player)} games")
            else:
                self.player_stats_label1.config(text = f"{selected_player} has scored {goals_assists[0]} goals in {get_games_played(selected_player)} games")
            if goals_assists[1] == 1:
                self.player_stats_label2.config(text = f"{selected_player} has 1 assist in {get_games_played(selected_player)} games")
            else:
                self.player_stats_label2.config(text = f"{selected_player} has {goals_assists[1]} assists in {get_games_played(selected_player)} games")
        elif selected_player in get_goalies():
            GA_SA_SV = get_goalie_GA_SA_SA(self.player_var.get())
            if GA_SA_SV[0] == 1:
                if GA_SA_SV[1] == 1:
                    self.player_stats_label1.config(text = f"{selected_player} has allowed 1 goal in {get_games_played(selected_player)} games from 1 shot attempted.")
                else:
                    self.player_stats_label1.config(text = f"{selected_player} has allowed 1 goal in {get_games_played(selected_player)} games from {GA_SA_SV[1]} shots attempted")
            else:
                self.player_stats_label1.config(text = f"{selected_player} has allowed {GA_SA_SV[0]} goals in {get_games_played(selected_player)} games from {GA_SA_SV[1]} shots attempted")
            if GA_SA_SV[2] == 1:
                self.player_stats_label2.config(text = f"{selected_player} has made 1 save in {get_games_played(selected_player)} games")
            else:
                self.player_stats_label2.config(text = f"{selected_player} has made {GA_SA_SV[2]} saves in {get_games_played(selected_player)} games")
    def ts_clicked(self):
        #this code should execute when the user selects the Team Stats Button

        self.header_label.config(text = "Team Stats")
        self.Search_Player_Button.pack_forget()
        self.Team_Button.pack_forget()
        
        goals_for = get_team_goals_for()
        goals_against = get_team_goals_against()
        if goals_for == 1:
            self.goals_for_label = tkinter.Label(self.window, text = f"The Rangers have scored 1 goal in {get_games_played()} games")
        else:
            self.goals_for_label = tkinter.Label(self.window, text = f"The Rangers have scored {goals_for} goals in {get_games_played()} games")
        self.goals_for_label.pack()
        
        if goals_against == 1:
            self.goals_against_label = tkinter.Label(self.window, text = f"The Rangers have allowed 1 goal in {get_games_played()} games")
        else:
            self.goals_against_label = tkinter.Label(self.window, text = f"The Rangers have allowed {goals_against} goals in {get_games_played()} games")
        self.goals_against_label.pack()
        
        self.Return_To_Menu_Button = tkinter.Button(self.window, text = "Main Menu", command = self.mmb_clicked_from_team)
        self.Return_To_Menu_Button.pack(side = 'left')

    def mmb_clicked_from_player(self):
        #this code should execute when the user selects the Main Menu Button From Player Stats
        self.header_label.config(text = "Welcome to the stat book. What would you like to see?")
        self.header_label.pack()

        self.Search_Player_Button = tkinter.Button(self.window, text = "Player Stats", command = self.ps_clicked)
        self.Search_Player_Button.pack()
        self.Team_Button = tkinter.Button(self.window, text = "Team Stats", command = self.ts_clicked)
        self.Team_Button.pack()
        self.Return_To_Menu_Button.pack_forget()
        
        self.Player_List_Dropdown.pack_forget()
        self.player_stats_label1.pack_forget()
        self.player_stats_label2.pack_forget()
        
    def mmb_clicked_from_team(self):
        #this code should execute when the user selects the Main Menu Button From Team Stats
        self.header_label.config(text = "Welcome to the stat book. What would you like to see?")
        self.header_label.pack()

        self.Search_Player_Button = tkinter.Button(self.window, text = "Player Stats", command = self.ps_clicked)
        self.Search_Player_Button.pack()
        self.Team_Button = tkinter.Button(self.window, text = "Team Stats", command = self.ts_clicked)
        self.Team_Button.pack()
        self.Return_To_Menu_Button.pack_forget()
        
        self.goals_for_label.pack_forget()
        self.goals_against_label.pack_forget()



