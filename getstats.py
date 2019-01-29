import pandas as pd
from pandas.io.json import json_normalize
import base64
import requests
# keep this in a safe place.
from templates.apikey import apikey_token


url='https://api.mysportsfeeds.com/v2.0/pull/mlb/2018-regular/team_stats_totals.json'

teams=['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CWS', 'CIN',
'CLE', 'COL', 'DET', 'MIA', 'HOU', 'KC', 'LAA',
'LAD', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI',
'PIT', 'SD', 'SF', 'SEA', 'STL', 'TB', 'TEX', 'TOR', 'WAS']

# Get team-level statistics for the 2018 MLB season

class Baseball:

    def __init__(self, team):
        self.url='https://api.mysportsfeeds.com/v2.0/pull/mlb/2018-regular/team_stats_totals.json'
        self.team=team
        self.apikey_token=apikey_token # defined outside of the class for security reasons.
        self.errors=[]
        self.results={}
        if self.team in teams:
            try:
                response = requests.get(
                    url=self.url,
                    params={
                        "team": self.team,
                    },
                    headers={
                        "Authorization": "Basic " + base64.b64encode('{}:{}'.format(apikey_token,'MYSPORTSFEEDS').encode('utf-8')).decode('ascii')
                    }
                )
                self.response = response.json()
                self.name =     self.response['teamStatsTotals'][0]['team']['name']
                self.city =     self.response['teamStatsTotals'][0]['team']['city']
                self.ballpark = self.response['teamStatsTotals'][0]['team']['homeVenue']['name']
                self.win_pct =  self.response['teamStatsTotals'][0]['stats']['standings']['winPct']
                self.results['Name']=self.name
                self.results['City']=self.city
                self.results['Ballpark']=self.ballpark
                self.results['Win Pct']=self.win_pct
            except requests.exceptions.RequestException:
                self.errors.append('HTTP Request failed')
                print(self.errors[0])
        else:
            self.errors.append('Please select from the following team abbreviations: {}'.format(', '.join(teams)))
            print(self.errors[0])

    # Batting statistics
    def batting_stats(self, *args):
        option='batting'
        stats_dict = {}
        for arg in args:
            if arg not in list(self.response['teamStatsTotals'][0]['stats'][option].keys()):
                self.errors.append('Please request from the following statistics: {}'.format(
                    ', '.join(list(self.response['teamStatsTotals'][0]['stats'][option].keys()))))
                print(self.errors[0])
            else:
                statvalue = self.response['teamStatsTotals'][0]['stats'][option][arg]
                stats_dict[arg]=statvalue
                self.results.update(stats_dict)
        return self.results

    # Pitching statistics
    def pitching_stats(self, *args):
        option='pitching'
        stats_dict = {}
        for arg in args:
            if arg not in list(self.response['teamStatsTotals'][0]['stats'][option].keys()):
                self.errors.append('Please request from the following statistics: {}'.format(
                    ', '.join(list(self.response['teamStatsTotals'][0]['stats'][option].keys()))))
                print(self.errors[0])
            else:
                statvalue = self.response['teamStatsTotals'][0]['stats'][option][arg]
                stats_dict[arg]=statvalue
                self.results.update(stats_dict)
        return self.results

    # Fielding statistics
    def fielding_stats(self, *args):
        option='fielding'
        stats_dict = {}
        for arg in args:
            if arg not in list(self.response['teamStatsTotals'][0]['stats'][option].keys()):
                self.errors.append('Please request from the following statistics: {}'.format(
                    ', '.join(list(self.response['teamStatsTotals'][0]['stats'][option].keys()))))
                print(self.errors[0])
            else:
                statvalue = self.response['teamStatsTotals'][0]['stats'][option][arg]
                stats_dict[arg]=statvalue
                self.results.update(stats_dict)
        return self.results

    # Overall statistics
    def overall_stats(self, *args):
        option='standings'
        stats_dict = {}
        for arg in args:
            if arg not in list(self.response['teamStatsTotals'][0]['stats'][option].keys()):
                self.errors.append('Please request from the following statistics: {}'.format(
                    ', '.join(list(self.response['teamStatsTotals'][0]['stats'][option].keys()))))
                print(self.errors[0])
            else:
                statvalue = self.response['teamStatsTotals'][0]['stats'][option][arg]
                stats_dict[arg]=statvalue
                self.results.update(stats_dict)
        return self.results
