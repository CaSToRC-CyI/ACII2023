#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%

from load_data import load_participant_data

#%%

# Dataset 1 - Low Alexithymics

folder_path = '/Users/user/Desktop/ACII2023_Datasets/Dataset1/LowAlexithymics/'
#%%

# Load data of participants individually
participant_11145 = load_participant_data(folder_path, '11145.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_12004 = load_participant_data(folder_path, '12004.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_12007 = load_participant_data(folder_path, '12007.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_12010 = load_participant_data(folder_path, '12010.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_12031 = load_participant_data(folder_path, '12031.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_12160 = load_participant_data(folder_path, '12160.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_21143 = load_participant_data(folder_path, '21143.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_22008 = load_participant_data(folder_path, '22008.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_22011 = load_participant_data(folder_path, '22011.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_22023 = load_participant_data(folder_path, '22023.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_22026 = load_participant_data(folder_path, '22026.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_22137 = load_participant_data(folder_path, '22137.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_22140 = load_participant_data(folder_path, '22140.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_22155 = load_participant_data(folder_path, '22155.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_31150 = load_participant_data(folder_path, '31150.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_31156 = load_participant_data(folder_path, '31156.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_32006 = load_participant_data(folder_path, '32006.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_32009 = load_participant_data(folder_path, '32009.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_32018 = load_participant_data(folder_path, '32018.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_32024 = load_participant_data(folder_path, '32024.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_32033 = load_participant_data(folder_path, '32033.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_32138 = load_participant_data(folder_path, '32138.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_32144 = load_participant_data(folder_path, '32144.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_32147 = load_participant_data(folder_path, '32147.acq', info_dict, normalise=True, downsample=True, state='Universal')

#%% 

# List of participants to load dataset
dataset1_low_list = ['12010.ACQ', '12004.acq', '31150.acq', '21143.acq', '12007.acq', '31156.acq', '12160.acq',\
                     '32138.ACQ', '22011.acq', '11145.acq', '32006.acq', '22026.acq', '32009.acq', '32144.acq',\
                     '22155.acq', '32024.acq', '32018.acq', '22008.acq', '22140.ACQ', '32147.acq', '32033.acq',\
                     '22023.acq', '12031.acq', '12142.acq', '12037.ACQ', '22137.acq']

