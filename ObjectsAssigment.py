class Player:
    def __init__(self, player_name, player_position):
        self.player_name = player_name
        self.player_position = player_position

    def __str__(self):
        return f"{self.player_name} - {self.player_position}"


class NFLTeam:
    def __init__(self, team_name, players=[]):
        self.team_name = team_name
        self.players = players

    def add_player(self, player):
        self.players.append(player)

    def display_team(self):
        print(f"Team: {self.team_name}")
        for player in self.players:
            print(player)


player1 = Player("Joe Montana", "QB")
player2 = Player("Barry Sanders", "RB")
player3 = Player("Jerry Rice", "WR")
player4 = Player("Graham Gano", "K")


player_list = [player1, player2, player3, player4]


team = NFLTeam("Dream Team", player_list)


team.display_team()