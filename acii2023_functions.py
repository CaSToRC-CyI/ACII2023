#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%

import pandas as pd
import bioread
import numpy as np

#%%

def read_acq_file(folder_path, datafile):
        
    data = bioread.read(folder_path + datafile)
    
    # """
    # data.time_index # time
    # data.channels[1].data # SCR
    # data.channels[6].data # phase 1
    # data.channels[7].data # arousal
    # data.channels[9].data # valence 2
    # data.channels[11].data # tone 1
    # data.channels[12].data # tone 2
    # data.channels[13].data # phase 2
    # data.channels[17].data # ECG BPM
    # data.channels[19].data # ORB
    # data.channels[20].data # COR
    # data.channels[21].data # ZYG
    # """
        
    # This condition is used because of the sampling rate issue of "phase2"
    if int(data.channels[13].samples_per_second) == 1000:
        # print("phase2 is okay")
        df = pd.DataFrame([data.time_index, data.channels[1].data, data.channels[17].data,
                            data.channels[19].data, data.channels[20].data, data.channels[21].data,
                            data.channels[6].data, data.channels[7].data, data.channels[9].data,
                            data.channels[11].data, data.channels[12].data, data.channels[13].data])
    else: 
        # print("phase2 needs scale up")
        phase_2_scaleup = rescale(data.channels[13].data, 8)
    
        df = pd.DataFrame([data.time_index, data.channels[1].data, data.channels[17].data,
                            data.channels[19].data, data.channels[20].data, data.channels[21].data,
                            data.channels[6].data, data.channels[7].data, data.channels[9].data,
                            data.channels[11].data, data.channels[12].data, phase_2_scaleup])
   
    df_T = df.transpose()
    
    df_T.columns = ["time","SCR", "ECG","ORB","COR","ZYG","phase1","Arousal","Valence2",
                    "Tone1","Tone2","phase2"]
    
    return df_T

#%%

# This function is used to rescale "phase2" where necessary. 

def rescale(arr, factor):
    n = len(arr)
    return np.interp(np.linspace(0, n, factor*n+1), np.arange(n), arr)

#%%

def create_info_dictionary(csv_file, key_column, value_columns):
    data = pd.read_csv(csv_file)
    info_dict = {}

    for _, row in data.iterrows():
        key = row[key_column]
        values = [row[col] for col in value_columns]
        info_dict[key] = values

    return info_dict


