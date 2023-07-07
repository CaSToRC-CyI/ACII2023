#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%

from acii2023_functions import create_info_dictionary

#%%

# csv file path
csv_file = '/Users/user/Desktop/ACII2023_Datasets/alexithymia_demographics_info.csv'
    
#%%

key_column = 'id'
value_columns = ['group', 'dataset'] # Replace with your desired column names

info_dict = create_info_dictionary(csv_file, key_column, value_columns)
