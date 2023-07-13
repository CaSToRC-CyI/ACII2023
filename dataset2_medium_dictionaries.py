#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%

from acii2023_functions import read_acq_file, rescale

#%%

# Dataset 2 - Medium Alexithymics

folder_path = '/Users/user/Desktop/ACII2023_Datasets/Dataset2/MediumAlexithymics/'
#%%
participant_112307 = {'112307': {'acq_data': read_acq_file(folder_path, '112307.acq',  normalise_data=True, downsample_data=True, normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[112307][0],\
                               'dataset': info_dict[112307][1]}}
    
participant_112353 = {'112353': {'acq_data': read_acq_file(folder_path, '112353.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[112353][0],\
                               'dataset': info_dict[112353][1]}}

participant_122324 = {'122324': {'acq_data': read_acq_file(folder_path, '122324.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[122324][0],\
                               'dataset': info_dict[122324][1]}}

participant_221311 = {'221311': {'acq_data': read_acq_file(folder_path, '221311.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[221311][0],\
                               'dataset': info_dict[221311][1]}}

participant_222320 = {'222320': {'acq_data': read_acq_file(folder_path, '222320.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[222320][0],\
                               'dataset': info_dict[222320][1]}}
    
participant_222323 = {'222323': {'acq_data': read_acq_file(folder_path, '222323.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[222323][0],\
                               'dataset': info_dict[222323][1]}}

participant_222332 = {'222332': {'acq_data': read_acq_file(folder_path, '222332.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[222332][0],\
                               'dataset': info_dict[222332][1]}}

participant_311367 = {'311367': {'acq_data': read_acq_file(folder_path, '311367.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[311367][0],\
                               'dataset': info_dict[311367][1]}}

participant_312355 = {'312355': {'acq_data': read_acq_file(folder_path, '312355.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[312355][0],\
                               'dataset': info_dict[312355][1]}}

participant_321349 = {'321349': {'acq_data': read_acq_file(folder_path, '321349.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[321349][0],\
                               'dataset': info_dict[321349][1]}} 