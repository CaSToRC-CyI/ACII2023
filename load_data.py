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
                        'dataset': info_dict[number][1],\
                        'TASDIF': info_dict[number][2],\
                        'TASDDF': info_dict[number][3],\
                        'TASEOT': info_dict[number][4],\
                        'TAStot':info_dict[number][5]}
             
                    
    return participant_dict


#%%


dataset1_low = ['12010.ACQ', '12004.acq', '31150.acq', '21143.acq', '12007.acq', '31156.acq', '12160.acq',\
                '32138.ACQ', '22011.acq', '11145.acq', '32006.acq', '22026.acq', '32009.acq', '32144.acq',\
                '22155.acq', '32024.acq', '32018.acq', '22008.acq', '22140.ACQ', '32147.acq', '32033.acq',\
                '22023.acq', '12031.acq', '12142.acq', '12037.ACQ', '22137.acq']

dataset1_high = ['32115.acq', '22258.acq', '11254.acq', '12239.ACQ', '22249.acq', '32259.acq', '11251.acq',\
                 '22114.ACQ', '12001.acq', '22129.acq', '12113.ACQ', '31253.acq', '12128.ACQ', '21246.acq',\
                 '12116.ACQ', '12125.ACQ', '12257.acq', '12134.ACQ', '12122.ACQ', '22252.acq', '32136.acq',\
                 '32241.ACQ', '22132.acq', '32127.acq', '32130.acq', '22135.acq', '12236.ACQ']

dataset2_low = ['222308.acq', '322334.acq', '312368.acq', '212357.acq', '322322.acq', '112301.acq',\
                '322327.acq', '122348.acq', '222343.acq', '112364.acq', '112358.acq', '112359.acq',\
                '112365.acq', '122312.acq', '122306.acq', '322345.acq', '322344.acq', '322350.acq',\
                '222346.acq', '321316.acq', '122319.acq', '321333.acq', '122318.acq', '122330.acq',\
                '112352.acq', '211351.acq', '321309.acq', '122336.acq', '122335.acq', '222329.acq',\
                '322315.acq', '312361.acq', '322328.acq', '122347.acq', '222302.acq', '312362.acq',\
                '212363.acq',  '322303.acq', '222317.acq', '212366.acq', '322310.acq', '322338.acq',\
                '222305.acq', '122342.acq']

    
dataset2_medium = ['222320.acq', '112307.acq', '312355.acq', '222323.acq', '222332.acq', '321349.acq',\
                   '311367.acq', '221311.acq', '122324.acq', '112353.acq']

dataset2_high = ['322321.acq', '222337.acq', '122313.acq', '122331.acq', '122325.acq', '211354.acq',\
                 '311356.acq', '212360.acq', '122341.acq', '322304.acq', '322339.acq']

trial = ['222320.acq', '112307.acq']

#%%

def load_dataset(folder_path, participant_list, info_dict, normalise=True, downsample=True):
    
    X = {}
    y = {}
    
    for participant in participant_list:
        
        df = load_participant_data(folder_path, participant, info_dict, normalise, downsample)

        dot_index = participant.index('.')
    
        # Extract the numerical part
        numerical_part = participant[:dot_index]
             
        X[numerical_part] = df
        
        y[numerical_part] = info_dict[int(numerical_part)][0]
    
    return X, y 
    

