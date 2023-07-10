#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%

from acii2023_functions import create_info_dictionary

#%%

# csv file path
csv_file = '/Users/user/Desktop/ACII2023_Datasets/alexithymia_demographics_info.csv'
    
#%%

# ID would be the key column of the dictionary
key_column = 'id'

# Group and dataset labels would be the values of the dictionary
value_columns = ['group', 'dataset'] 

# Dictionary containing information for each participant
info_dict = create_info_dictionary(csv_file, key_column, value_columns)
