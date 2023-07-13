#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%

from acii2023_functions import create_info_dictionary

#%%

# csv file path
csv_file = '/Users/user/Desktop/ACII2023_Datasets/alexithymia_demographics_info.csv'

# Dictionary containing information for each participant
info_dict = create_info_dictionary(csv_file, 'id', ['group', 'dataset', 'TASDIF', 'TASDDF', 'TASEOT', 'TAStot'])
