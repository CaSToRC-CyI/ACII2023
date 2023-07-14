#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%

from load_data import load_participant_data

#%%

# Dataset 2 - High Alexithymics

folder_path = '/Users/user/Desktop/ACII2023_Datasets/Dataset2/HighAlexithymics/'
#%%

# Load data of participants individually
participant_122313 = load_participant_data(folder_path, '122313.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_122325 = load_participant_data(folder_path, '122325.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_122331 = load_participant_data(folder_path, '122331.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_122341 = load_participant_data(folder_path, '122341.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_211354 = load_participant_data(folder_path, '211354.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_212360 = load_participant_data(folder_path, '212360.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_212360 = load_participant_data(folder_path, '212360.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_222337 = load_participant_data(folder_path, '222337.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_311356 = load_participant_data(folder_path, '311356.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_322304 = load_participant_data(folder_path, '322304.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_322321 = load_participant_data(folder_path, '322321.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_322339 = load_participant_data(folder_path, '322339.acq', info_dict, normalise=True, downsample=True, state='Universal')
  
#%% 

# List of participants to load dataset
dataset2_high = ['322321.acq', '222337.acq', '122313.acq', '122331.acq', '122325.acq', '211354.acq',\
                 '311356.acq', '212360.acq', '122341.acq', '322304.acq', '322339.acq']