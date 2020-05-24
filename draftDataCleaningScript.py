#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 21:37:11 2020

@author: jacobfericy
"""

import pandas as pd
import numpy as np
import os

mlsDraft2019_Raw = pd.read_excel('/Users/jacobfericy/GitHub/MLS_Analytics/MLS_2019_Raw.xlsx')

mlsDraft2019 = mlsDraft2019_Raw.drop(mlsDraft2019_Raw[mlsDraft2019_Raw['P'] == 'P' ].index , inplace=True)
mlsDraft2019 = mlsDraft2019_Raw.drop(mlsDraft2019_Raw[mlsDraft2019_Raw['P'] == 'Round 2' ].index , inplace=True)
mlsDraft2019 = mlsDraft2019_Raw.drop(mlsDraft2019_Raw[mlsDraft2019_Raw['P'] == 'Round 3' ].index , inplace=True)
mlsDraft2019 = mlsDraft2019_Raw.drop(mlsDraft2019_Raw[mlsDraft2019_Raw['P'] == 'Round 4' ].index , inplace=True)

def cleanDraftData(filename, year):
   
    mlsDraftFrame = [Draft_2000, Draft_2001, Draft_2002, Draft_2003, Draft_2004, Draft_2005,
          Draft_2006, Draft_2007, Draft_2008, Draft_2009, Draft_2010, Draft_2011,
          Draft_2012, Draft_2013, Draft_2014, Draft_2015, Draft_2016, Draft_2017,
          Draft_2018]

    mlsDraftMerge = pd.concat(mlsDraftFrame)

Draft_Merge.to_csv('/Users/jacobfericy/Desktop/WTFP/Draft_Merge.csv', sep=',')
    return draftDataAll
