#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%

from load_data import load_participant_data

#%%

# Dataset 2 - Low Alexithymics

folder_path = '/Users/user/Desktop/ACII2023_Datasets/Dataset2/LowAlexithymics/'
#%%

# Load data of participants individually
participant_112301 = load_participant_data(folder_path, '112301.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_112352 = load_participant_data(folder_path, '112352.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_112358 = load_participant_data(folder_path, '112358.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_112359 = load_participant_data(folder_path, '112359.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_112364 = load_participant_data(folder_path, '112364.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_112365 = load_participant_data(folder_path, '112365.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_122306 = load_participant_data(folder_path, '122306.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_122312 = load_participant_data(folder_path, '122312.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_122318 = load_participant_data(folder_path, '122318.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_122319 = load_participant_data(folder_path, '122319.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_122330 = load_participant_data(folder_path, '122330.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_122335 = load_participant_data(folder_path, '122335.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_122336 = load_participant_data(folder_path, '122336.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_122342 = load_participant_data(folder_path, '122342.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_122347 = load_participant_data(folder_path, '122347.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_122348 = load_participant_data(folder_path, '122348.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_211351 = load_participant_data(folder_path, '211351.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_212357 = load_participant_data(folder_path, '212357.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_212363 = load_participant_data(folder_path, '212363.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_212366 = load_participant_data(folder_path, '212366.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_222302 = load_participant_data(folder_path, '222302.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_222305 = load_participant_data(folder_path, '222305.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_222308 = load_participant_data(folder_path, '222308.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_222317 = load_participant_data(folder_path, '222317.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_222329 = load_participant_data(folder_path, '222329.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_222343 = load_participant_data(folder_path, '222343.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_222346 = load_participant_data(folder_path, '222346.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_312361 = load_participant_data(folder_path, '312361.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_312362 = load_participant_data(folder_path, '312362.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_312368 = load_participant_data(folder_path, '312368.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_321309 = load_participant_data(folder_path, '321309.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_321316 = load_participant_data(folder_path, '321316.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_321333 = load_participant_data(folder_path, '321333.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_322303 = load_participant_data(folder_path, '322303.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_322310 = load_participant_data(folder_path, '322310.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_322315 = load_participant_data(folder_path, '322315.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_322322 = load_participant_data(folder_path, '322322.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_322327 = load_participant_data(folder_path, '322327.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_322328 = load_participant_data(folder_path, '322328.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_322334 = load_participant_data(folder_path, '322334.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_322338 = load_participant_data(folder_path, '322338.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_322344 = load_participant_data(folder_path, '322344.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_322345 = load_participant_data(folder_path, '322345.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_322350 = load_participant_data(folder_path, '322350.acq', info_dict, normalise=True, downsample=True, state='Universal')

#%% 

# List of participants to load dataset
dataset2_low_list = ['222308.acq', '322334.acq', '312368.acq', '212357.acq', '322322.acq', '112301.acq',\
                     '322327.acq', '122348.acq', '222343.acq', '112364.acq', '112358.acq', '112359.acq',\
                     '112365.acq', '122312.acq', '122306.acq', '322345.acq', '322344.acq', '322350.acq',\
                     '222346.acq', '321316.acq', '122319.acq', '321333.acq', '122318.acq', '122330.acq',\
                     '112352.acq', '211351.acq', '321309.acq', '122336.acq', '122335.acq', '222329.acq',\
                     '322315.acq', '312361.acq', '322328.acq', '122347.acq', '222302.acq', '312362.acq',\
                     '212363.acq',  '322303.acq', '222317.acq', '212366.acq', '322310.acq', '322338.acq',\
                     '222305.acq', '122342.acq']
    
    