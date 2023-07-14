#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 12:33:20 2023

@author: k19038vf
"""
#%%

from acii2023_functions import read_acq_file, feature_extraction

#%%

def load_participant_data(folder_path, filename, info_dict, normalise=True, downsample=True, state='Universal'):
    
    
    string = filename
    # Find the index of the dot
    dot_index = string.index('.')

    # Extract the numerical part
    numerical_part = string[:dot_index]

    # Convert the numerical part to an integer or float
    number = int(numerical_part)
    

    participant_dict = {'acq_data': read_acq_file(folder_path, filename, state, normalise_data=normalise, downsample_data=downsample),\
                        'group_label': info_dict[number][0],\
                        'dataset': info_dict[number][1],\
                        'TASDIF': info_dict[number][2],\
                        'TASDDF': info_dict[number][3],\
                        'TASEOT': info_dict[number][4],\
                        'TAStot':info_dict[number][5]}
             
                    
    return participant_dict


#%%

def load_dataset(folder_path, participant_list, info_dict, normalise=True, downsample=True, tsfresh=False, state='Universal', scale_features=True):
    
    X = {}
    y = {}
    
    for participant in participant_list:
        
        df = load_participant_data(folder_path, participant, info_dict, normalise, downsample, state)

        dot_index = participant.index('.')
    
        # Extract the numerical part
        numerical_part = participant[:dot_index]
             
        X[numerical_part] = df
        
        y[numerical_part] = info_dict[int(numerical_part)][0]
               
    
    if tsfresh == False: 
        return X, y 
    
    elif tsfresh == True:
        features, relevance_table = feature_extraction(X, y, state, scale_features)
        
        return features, relevance_table

    



