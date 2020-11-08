# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 18:46:31 2020


@author: B Hoover
"""

from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc

from basketball_reference_scraper.players import get_stats, get_game_logs, get_player_headshot

from basketball_reference_scraper.shot_charts import get_shot_chart

import os
#Get team roster stats
bulls_2020 = get_roster_stats('CHI', 2020)

#Select individual player
bulls_2020[bulls_2020.PLAYER == "Coby White"]

''' Get individual players 

name - Player full name (e.g. 'LaMarcus Aldridge')
stat_type - One of 'PER_GAME', 'PER_MINUTE', 'PER_POSS', 'ADVANCED'
playoffs - Whether to return Playoff stats or not. One of True|False. Default value is False
career - Whether to return career stats or not. One of True|False. Default value is False

'''

coby = get_stats("Coby White", stat_type='ADVANCED', playoffs=False, career=False)
coby.head(10)

d = get_player_headshot('Coby White')

d = get_shot_chart('2019-12-28', 'TOR', 'BOS')


#Import college players
from sportsreference.ncaab.roster import Player as pl

player_ncaa = pl('kenyon-martin-1')
#get available object variables
dir(player_ncaa)
player_ncaa.dataframe.iloc[-2,:]


import glob
import pandas as pd
draft_files = glob.glob("*")
len(draft_files)
df = pd.read_csv(draft_files[10])
# df

# player_ad_nba = get_stats("Kenyon Martin", stat_type='ADVANCED', playoffs=False, career=False)
# career = player_ad_nba.iloc[0,:]
# career
# player_ad_nba['PER']


##########Combine draft info into one dataframe######################################################

import glob
import pandas as pd
draft_files = glob.glob("*.txt")

#1. create empty list
draft_df = []

#2. Iterate through the draft files. Read them in and append to list. 
for filename in draft_files:
    df = pd.read_csv(filename, index_col=None, header=1)
    draft_df.append(df)

#3 Create data frame of all players and their draft
draft_df = pd.concat(draft_df, axis=0, ignore_index=True)

#4. Split players to player name and code
draft_df[['Player_name','Code']] = draft_df.Player.str.split("\\", expand=True)
#4 Drop duplicate player column
draft_df = draft_df.drop(['Player'], axis=1)

#5. Manipulate string to get name code for input in sportsreference player code. 
draft_df.Player_name.str.lower().replace(' ', '-', regex=True) + "-1"
draft_df.Player_name
draft_df['Code']

#6 Manipulate string to get name for ncaa data
draft_df['NCAA_code'] = draft_df['Player_name'].str.replace(" ", "-") + "-1"
draft_df['NCAA_code'] = draft_df['NCAA_code'].str.lower()

#7 Pull NCAA data for each NBA draftee
# Create NCAA code dupicate for future merge. 
# ncaa_df = pd.DataFrame()
# for i in draft_df['NCAA_code']:
#     try: 
#         player_ncaa = pl(i)
#     except Exception:
#         pass
        
#     test = player_ncaa.dataframe.iloc[len(player_ncaa.dataframe) - 1, :]
#     test['NCAA_code'] = i
#     ncaa_df = ncaa_df.append( test, ignore_index=True)
    
# ncaa_df.to_csv("college_stats.csv")

#8 Saved the ncaa dataframe to file, so don't have to keep pulling the data
ncaa_df = pd.read_csv('college_stats.csv')

'''There are now two data frame. We need to pull the advance stats for each player'''
ncaa_df

draft_df.columns

ncaa_df.drop_duplica

from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc

from basketball_reference_scraper.players import get_stats, get_game_logs, get_player_headshot

from basketball_reference_scraper.shot_charts import get_shot_chart


player = get_stats(draft_df.Player_name[0], stat_type='ADVANCED', playoffs=False, career=False)
player.PER.mean()



