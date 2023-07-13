#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%

from acii2023_functions import read_acq_file, rescale

#%%

# Dataset 1 - High Alexithymics

folder_path = '/Users/user/Desktop/ACII2023_Datasets/Dataset1/HighAlexithymics/'
#%%
participant_11251 = {'11251': {'acq_data': read_acq_file(folder_path, '11251.acq', normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[11251][0],\
                               'dataset': info_dict[11251][1]}}
    
participant_11254 = {'11254': {'acq_data': read_acq_file(folder_path, '11254.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[11254][0],\
                               'dataset': info_dict[11254][1]}}

participant_12001 = {'12001': {'acq_data': read_acq_file(folder_path, '12001.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[12001][0],\
                               'dataset': info_dict[12001][1]}}

participant_12113 = {'12113': {'acq_data': read_acq_file(folder_path, '12113.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[12113][0],\
                               'dataset': info_dict[12113][1]}}

participant_12116 = {'12116': {'acq_data': read_acq_file(folder_path, '12116.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[12116][0],\
                               'dataset': info_dict[12116][1]}}
    
participant_12122 = {'12122': {'acq_data': read_acq_file(folder_path, '12122.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[12122][0],\
                               'dataset': info_dict[12122][1]}}

participant_12125 = {'12125': {'acq_data': read_acq_file(folder_path, '12125.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[12125][0],\
                               'dataset': info_dict[12125][1]}}

participant_12128 = {'12128': {'acq_data': read_acq_file(folder_path, '12128.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[12128][0],\
                               'dataset': info_dict[12128][1]}}
    
participant_12134 = {'12134': {'acq_data': read_acq_file(folder_path, '12134.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[12134][0],\
                               'dataset': info_dict[12134][1]}}
    
participant_12236 = {'12236': {'acq_data': read_acq_file(folder_path, '12236.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[12236][0],\
                               'dataset': info_dict[12236][1]}}

participant_12239 = {'12239': {'acq_data': read_acq_file(folder_path, '12239.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[12239][0],\
                               'dataset': info_dict[12239][1]}}

participant_12257 = {'12257': {'acq_data': read_acq_file(folder_path, '12257.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[12257][0],\
                               'dataset': info_dict[12257][1]}}

participant_21246 = {'21246': {'acq_data': read_acq_file(folder_path, '21246.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[21246][0],\
                               'dataset': info_dict[21246][1]}}
    
participant_22114 = {'22114': {'acq_data': read_acq_file(folder_path, '22114.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[22114][0],\
                               'dataset': info_dict[22114][1]}}

participant_22129 = {'22129': {'acq_data': read_acq_file(folder_path, '22129.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[22129][0],\
                               'dataset': info_dict[22129][1]}}

participant_22132 = {'22132': {'acq_data': read_acq_file(folder_path, '22132.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[22132][0],\
                               'dataset': info_dict[22132][1]}}
    
participant_22135 = {'22135': {'acq_data': read_acq_file(folder_path, '22135.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[22135][0],\
                               'dataset': info_dict[22135][1]}}
    
participant_22249 = {'22249': {'acq_data': read_acq_file(folder_path, '22249.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[22249][0],\
                               'dataset': info_dict[22249][1]}}

participant_22252 = {'22252': {'acq_data': read_acq_file(folder_path, '22252.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[22252][0],\
                               'dataset': info_dict[22252][1]}}

participant_22258 = {'22258': {'acq_data': read_acq_file(folder_path, '22258.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[22258][0],\
                               'dataset': info_dict[22258][1]}}

participant_31253 = {'31253': {'acq_data': read_acq_file(folder_path, '31253.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[31253][0],\
                               'dataset': info_dict[31253][1]}}
    
participant_32115 = {'32115': {'acq_data': read_acq_file(folder_path, '32115.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[32115][0],\
                               'dataset': info_dict[32115][1]}}

participant_32127 = {'32127': {'acq_data': read_acq_file(folder_path, '32127.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[32127][0],\
                               'dataset': info_dict[32127][1]}}

participant_32130 = {'32130': {'acq_data': read_acq_file(folder_path, '32130.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[32130][0],\
                               'dataset': info_dict[32130][1]}}
    
participant_32136 = {'32136': {'acq_data': read_acq_file(folder_path, '32136.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[32136][0],\
                               'dataset': info_dict[32136][1]}}

participant_32241 = {'32241': {'acq_data': read_acq_file(folder_path, '32241.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[32241][0],\
                               'dataset': info_dict[32241][1]}}

participant_32259 = {'32259': {'acq_data': read_acq_file(folder_path, '32259.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[32259][0],\
                               'dataset': info_dict[32259][1]}}    
