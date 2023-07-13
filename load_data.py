#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 12:33:20 2023

@author: k19038vf
"""
#%%

from acii2023_functions import read_acq_file, rescale

#%%

def load_participant_data(folder_path, filename, info_dict, normalise=True, downsample=True):
    
    
    string = filename
    # Find the index of the dot
    dot_index = string.index('.')

    # Extract the numerical part
    numerical_part = string[:dot_index]

    # Convert the numerical part to an integer or float
    number = int(numerical_part)
    
    participant_dict = {'acq_data': read_acq_file(folder_path, filename,  normalise_data=normalise, downsample_data=downsample),\
                         'group_label': info_dict[number][0],\
                         'dataset': info_dict[number][1]}
        
        
    return participant_dict



    