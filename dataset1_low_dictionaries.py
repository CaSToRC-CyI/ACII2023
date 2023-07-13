#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%

from acii2023_functions import read_acq_file, rescale

#%%

# Dataset 1 - Low Alexithymics

folder_path = '/Users/user/Desktop/ACII2023_Datasets/Dataset1/LowAlexithymics/'
#%%
participant_11145 = {'11145': {'acq_data': read_acq_file(folder_path, '11145.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[11145][0],\
                               'dataset': info_dict[11145][1]}}
    
participant_12004 = {'12004': {'acq_data': read_acq_file(folder_path, '12004.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[12004][0],\
                               'dataset': info_dict[12004][1]}}
    
participant_12007 = {'12007': {'acq_data': read_acq_file(folder_path, '12007.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[12007][0],\
                               'dataset': info_dict[12007][1]}}

participant_12010 = {'12010': {'acq_data': read_acq_file(folder_path, '12010.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[12010][0],\
                               'dataset': info_dict[12010][1]}}

participant_12031 = {'12031': {'acq_data': read_acq_file(folder_path, '12031.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[12031][0],\
                               'dataset': info_dict[12031][1]}}
    
participant_12160 = {'12160': {'acq_data': read_acq_file(folder_path, '12160.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[12160][0],\
                               'dataset': info_dict[12160][1]}}
    
participant_21143 = {'21143': {'acq_data': read_acq_file(folder_path, '21143.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[21143][0],\
                               'dataset': info_dict[21143][1]}}

participant_22008 = {'22008': {'acq_data': read_acq_file(folder_path, '22008.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[22008][0],\
                               'dataset': info_dict[22008][1]}}
    
participant_22011 = {'22011': {'acq_data': read_acq_file(folder_path, '22011.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[22011][0],\
                               'dataset': info_dict[22011][1]}}

participant_22023 = {'22023': {'acq_data': read_acq_file(folder_path, '22023.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[22023][0],\
                               'dataset': info_dict[22023][1]}}
     
participant_22026 = {'22026': {'acq_data': read_acq_file(folder_path, '22026.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[22026][0],\
                               'dataset': info_dict[22026][1]}}

participant_22137 = {'22137': {'acq_data': read_acq_file(folder_path, '22137.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[22137][0],\
                               'dataset': info_dict[22137][1]}}

participant_22140 = {'22140': {'acq_data': read_acq_file(folder_path, '22140.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[22140][0],\
                               'dataset': info_dict[22140][1]}}
     
participant_22155 = {'22155': {'acq_data': read_acq_file(folder_path, '22155.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[22155][0],\
                               'dataset': info_dict[22155][1]}}
     
participant_31150 = {'31150': {'acq_data': read_acq_file(folder_path, '31150.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[31150][0],\
                               'dataset': info_dict[31150][1]}}

participant_31156 = {'31156': {'acq_data': read_acq_file(folder_path, '31156.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[31156][0],\
                               'dataset': info_dict[31156][1]}}   
    
participant_32006 = {'32006': {'acq_data': read_acq_file(folder_path, '32006.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[32006][0],\
                               'dataset': info_dict[32006][1]}}
    
participant_32009 = {'32009': {'acq_data': read_acq_file(folder_path, '32009.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[32009][0],\
                               'dataset': info_dict[32009][1]}}
    
participant_32018 = {'32018': {'acq_data': read_acq_file(folder_path, '32018.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[32018][0],\
                               'dataset': info_dict[32018][1]}}

participant_32024 = {'32024': {'acq_data': read_acq_file(folder_path, '32024.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[32024][0],\
                               'dataset': info_dict[32024][1]}}

participant_32033 = {'32033': {'acq_data': read_acq_file(folder_path, '32033.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[32033][0],\
                               'dataset': info_dict[32033][1]}}
    
participant_32138 = {'32138': {'acq_data': read_acq_file(folder_path, '32138.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[32138][0],\
                               'dataset': info_dict[32138][1]}}
    
participant_32144 = {'32144': {'acq_data': read_acq_file(folder_path, '32144.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[32144][0],\
                               'dataset': info_dict[32144][1]}}

participant_32147= {'32147': {'acq_data': read_acq_file(folder_path, '32147.acq',  normalise_data=True, downsample_data=True),\
                               'group_label': info_dict[32147][0],\
                               'dataset': info_dict[32147][1]}}

