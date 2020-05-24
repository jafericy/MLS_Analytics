#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 13:00:29 2020

@author: jacobfericy
"""

import pandas as pd
import numpy as np
import os

mlsStandingsdict = pd.read_excel('/Users/jacobfericy/GitHub/MLS_Analytics/MLS_Standings.xlsx', sheet_name=None)

mlsStandings = pd.DataFrame()
for name, sheet in mlsStandingsdict.items():
    sheet['Sheet'] = name
    sheet = sheet.rename(columns=lambda x: x.split('\n')[-1])
    mlsStandings = mlsStandings.append(sheet)

mlsStandings.reset_index(inplace=True, drop=True)

mlsStandings = mlsStandings.drop(['WIR','LIR','Sheet'],axis=1)

old_name_list = ['Kansas City Wiz','Kansas City Wizards','Columbus Crew', 'MetroStars','Dallas Burn','Los Angeles Galaxy','NY/NJ MetroStars']
new_name_list = ['Sporting Kansas City','Sporting Kansas City','Columbus Crew SC', 'New York Red Bulls','FC Dallas','LA Galaxy','New York Red Bulls']

name_dict = dict(zip(old_name_list, new_name_list))

mlsStandings.replace(name_dict, inplace=True)

minlist = pd.DataFrame()
for i in range(1998,2019):
    minlist[i] = mlsStandings[mlsStandings["POINTS"]]
    
    mlsStandings[]= minlist.append[i]


team_count = len(mlsStandings.TEAM.unique())

team_df = pd.DataFrame(mlsStandings.TEAM.unique())

mlsStandings.to_csv (r'/Users/jacobfericy/GitHub/MLS_Analytics/fullMLSStandings.csv', index = None, header=True)

