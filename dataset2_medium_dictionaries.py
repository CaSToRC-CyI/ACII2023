#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%

from load_data import load_participant_data

#%%

# Dataset 2 - Medium Alexithymics

folder_path = '/Users/user/Desktop/ACII2023_Datasets/Dataset2/MediumAlexithymics/'
#%%
participant_112307 = load_participant_data(folder_path, '112307.acq', info_dict, normalise=True, downsample=True)
participant_112353 = load_participant_data(folder_path, '112353.acq', info_dict, normalise=True, downsample=True)
participant_122324 = load_participant_data(folder_path, '122324.acq', info_dict, normalise=True, downsample=True)
participant_221311 = load_participant_data(folder_path, '221311.acq', info_dict, normalise=True, downsample=True)
participant_222320 = load_participant_data(folder_path, '222320.acq', info_dict, normalise=True, downsample=True)
participant_222323 = load_participant_data(folder_path, '222323.acq', info_dict, normalise=True, downsample=True)
participant_222332 = load_participant_data(folder_path, '222332.acq', info_dict, normalise=True, downsample=True)
participant_311367 = load_participant_data(folder_path, '311367.acq', info_dict, normalise=True, downsample=True)
participant_312355 = load_participant_data(folder_path, '312355.acq', info_dict, normalise=True, downsample=True)
participant_321349 = load_participant_data(folder_path, '321349.acq', info_dict, normalise=True, downsample=True)
