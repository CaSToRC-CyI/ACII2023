#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%

from acii2023_functions import read_acq_file, rescale

#%%

# Dataset 2 - High Alexithymics

folder_path = '/Users/user/Desktop/ACII2023_Datasets/Dataset2/HighAlexithymics/'
#%%
participant_122313 = {'122313': {'acq_data': read_acq_file(folder_path, '122313.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[122313][0],\
                               'dataset': info_dict[122313][1]}}
    
participant_122325 = {'122325': {'acq_data': read_acq_file(folder_path, '122325.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[122325][0],\
                               'dataset': info_dict[122325][1]}}

participant_122331 = {'122331': {'acq_data': read_acq_file(folder_path, '122331.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[122331][0],\
                               'dataset': info_dict[122331][1]}}

participant_122341 = {'122341': {'acq_data': read_acq_file(folder_path, '122341.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[122341][0],\
                               'dataset': info_dict[122341][1]}}

participant_211354 = {'211354': {'acq_data': read_acq_file(folder_path, '211354.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[211354][0],\
                               'dataset': info_dict[211354][1]}}
    
participant_212360 = {'212360': {'acq_data': read_acq_file(folder_path, '212360.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[212360][0],\
                               'dataset': info_dict[212360][1]}}

participant_212360 = {'212360': {'acq_data': read_acq_file(folder_path, '212360.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[212360][0],\
                               'dataset': info_dict[212360][1]}}

participant_222337 = {'222337': {'acq_data': read_acq_file(folder_path, '222337.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[222337][0],\
                               'dataset': info_dict[222337][1]}}
    
participant_311356 = {'311356': {'acq_data': read_acq_file(folder_path, '311356.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[311356][0],\
                               'dataset': info_dict[311356][1]}}
    
participant_322304 = {'322304': {'acq_data': read_acq_file(folder_path, '322304.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[322304][0],\
                               'dataset': info_dict[322304][1]}}

participant_322321 = {'322321': {'acq_data': read_acq_file(folder_path, '322321.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[322321][0],\
                               'dataset': info_dict[322321][1]}}

participant_322339 = {'322339': {'acq_data': read_acq_file(folder_path, '322339.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[322339][0],\
                               'dataset': info_dict[322339][1]}}    
    
    
 