#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%

from load_data import load_participant_data

#%%

# Dataset 1 - High Alexithymics

folder_path = '/Users/user/Desktop/ACII2023_Datasets/Dataset1/HighAlexithymics/'
#%%

# Load data of participants individually
participant_11251 = load_participant_data(folder_path, '11251.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_11254 = load_participant_data(folder_path, '11254.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_12001 = load_participant_data(folder_path, '12001.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_12113 = load_participant_data(folder_path, '12113.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_12116 = load_participant_data(folder_path, '12116.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_12122 = load_participant_data(folder_path, '12122.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_12125 = load_participant_data(folder_path, '12125.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_12128 = load_participant_data(folder_path, '12128.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_12134 = load_participant_data(folder_path, '12134.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_12236 = load_participant_data(folder_path, '12236.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_12239 = load_participant_data(folder_path, '12239.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_12257 = load_participant_data(folder_path, '12257.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_21246 = load_participant_data(folder_path, '21246.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_22114 = load_participant_data(folder_path, '22114.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_22129 = load_participant_data(folder_path, '22129.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_22132 = load_participant_data(folder_path, '22132.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_22135 = load_participant_data(folder_path, '22135.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_22249 = load_participant_data(folder_path, '22249.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_22252 = load_participant_data(folder_path, '22252.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_22258 = load_participant_data(folder_path, '22258.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_31253 = load_participant_data(folder_path, '31253.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_32115 = load_participant_data(folder_path, '32115.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_32127 = load_participant_data(folder_path, '32127.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_32130 = load_participant_data(folder_path, '32130.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_32136 = load_participant_data(folder_path, '32136.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_32241 = load_participant_data(folder_path, '32241.acq', info_dict, normalise=True, downsample=True, state='Universal')
participant_32259 = load_participant_data(folder_path, '32259.acq', info_dict, normalise=True, downsample=True, state='Universal')

#%% 

# List of participants to load dataset
dataset1_high = ['32115.acq', '22258.acq', '11254.acq', '12239.ACQ', '22249.acq', '32259.acq', '11251.acq',\
                 '22114.ACQ', '12001.acq', '22129.acq', '12113.ACQ', '31253.acq', '12128.ACQ', '21246.acq',\
                 '12116.ACQ', '12125.ACQ', '12257.acq', '12134.ACQ', '12122.ACQ', '22252.acq', '32136.acq',\
                 '32241.ACQ', '22132.acq', '32127.acq', '32130.acq', '22135.acq', '12236.ACQ']