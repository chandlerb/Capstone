import requests, gzip
import pandas as pd
from bs4 import BeautifulSoup

class Player: 
    def __init__(self, name=False, attribute=False, player_page=False):
        self.name = name 
        self.attribute = attribute
        self.player_page = player_page

    def __repr__(self):
        st = self.name + self.attribute
        return self.name

class GetPlayerData:
    
    def __init__(self):
        self.players_db = []

    def parse_players(self, c, RPM=False):
        soup = BeautifulSoup(c, 'lxml') # Parse the HTML as a string
        playername = soup.findAll("tr", {"class": ['evenrow', 'oddrow']})
        playerstat = soup.findAll("td", {"class": 'sortcell'})
        if RPM:
            start = 1
        else: 
            start = 0 
        for i in range(len(playername)): 
            self.players_db.append(Player(str(playername[i]).rsplit('</a>', 1)[0].rsplit(">", 1)[1], str(playerstat[i+start]).split(">")[1][:-4], 
            str(playername[i]).rsplit('<a href="', 1)[1].split('">')[0]))
        
    def get_players(self):
        return_list = []
        for player in self.players_db:
            return_list.append([player.name, float(player.attribute), player.player_page])
        return return_list

def get_page(url):
        return requests.get(url).text

def main():
    points = get_page('http://www.espn.com/nba/statistics/player/_/stat/scoring-per-game/sort/avgPoints/year/2018/seasontype/2')
    rebounds = get_page('http://www.espn.com/nba/statistics/player/_/stat/rebounds/sort/avgRebounds/year/2018/seasontype/2')
    assists = get_page('http://www.espn.com/nba/statistics/player/_/stat/assists/sort/avgAssists/year/2018/seasontype/2')
    blocks = get_page('http://www.espn.com/nba/statistics/player/_/stat/blocks/sort/avgBlocks/year/2018/seasontype/2')
    fg_percentage = get_page('http://www.espn.com/nba/statistics/player/_/stat/field-goals/sort/fieldGoalPct/year/2018/seasontype/2')
    steals = get_page('http://www.espn.com/nba/statistics/player/_/stat/steals/sort/avgSteals/year/2018/seasontype/2')
    minutes = get_page('http://www.espn.com/nba/statistics/player/_/stat/minutes')
    plus_minus = get_page('http://www.espn.com/nba/statistics/rpm/_/sort/RPM')
    rookies = get_page('http://www.espn.com/nba/statistics/player/_/stat/scoring-per-game/sort/avgPoints/seasontype/2/position/rookies')
    games_played = get_page('http://www.espn.com/nba/statistics/player/_/stat/minutes/sort/gamesPlayed/seasontype/2/qualified/false/split/127/count/161')
    
    games_played_leaders = GetPlayerData()
    games_played_leaders.parse_players(games_played)

    rookie_leaders = GetPlayerData()
    rookie_leaders.parse_players(rookies)

    point_leaders = GetPlayerData()
    point_leaders.parse_players(points)

    rebound_leaders = GetPlayerData()
    rebound_leaders.parse_players(rebounds)

    assist_leaders = GetPlayerData()
    assist_leaders.parse_players(assists)

    blocks_leaders = GetPlayerData()
    blocks_leaders.parse_players(blocks)

    fg_percentage_leaders = GetPlayerData()
    fg_percentage_leaders.parse_players(fg_percentage)

    steal_leaders = GetPlayerData()
    steal_leaders.parse_players(steals)

    minute_leaders = GetPlayerData()
    minute_leaders.parse_players(minutes)

    plus_minus_leaders = GetPlayerData()
    plus_minus_leaders.parse_players(plus_minus, True)

    
    data_base = {}
    data_base["games_played"] = games_played_leaders.get_players()
    data_base["points"] = point_leaders.get_players()
    data_base["rebounds"] = rebound_leaders.get_players()
    data_base["assists"] = assist_leaders.get_players()
    data_base["blocks"] = blocks_leaders.get_players()
    data_base["fg_percentage"] = fg_percentage_leaders.get_players()
    data_base["steals"] = steal_leaders.get_players()
    data_base["minutes"] = minute_leaders.get_players()
    data_base["plus_minus"] = plus_minus_leaders.get_players()
    data_base["rookie"] = rookie_leaders.get_players()
    return data_base
main()