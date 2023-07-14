#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%

import pandas as pd
import bioread
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from scipy.signal import resample_poly


from tsfresh import extract_features, select_features
from tsfresh.feature_selection.relevance import calculate_relevance_table
from tsfresh.feature_extraction import ComprehensiveFCParameters, EfficientFCParameters
from tsfresh.utilities.dataframe_functions import impute
#%%

def read_acq_file(folder_path, datafile, state='Universal', normalise_data=True, downsample_data=True):
        
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
        
    # This condition is used because of the sampling rate issue of 'phase2'
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
    
    df_T.columns = ['time','SCR', 'ECG','ORB','COR','ZYG','phase1','Arousal','Valence2',
                    'Tone1','Tone2','phase2']
        
    df_emotions_tones_phases = emotions_tones_phases(df_T)
    
    df_clean = drop_nan_values(df_emotions_tones_phases)
        
        
    if (downsample_data == True) and (normalise_data == True):
        
        df_tmp = downsample(df_clean)        
        df_final = normalise(df_tmp)

    elif (downsample_data == True) and (normalise_data == False):
        df_final = downsample(df_clean)

    elif (downsample_data == False) and (normalise_data == True):
        df_final = normalise(df_clean)
        
    elif (downsample_data == False) and (normalise_data == False):   
        
        df_final = df_clean
        
        
    if state == 'Universal':
        pass
    else:
        df_final = df_final[df_final['Emotion_Tone_Phase'] == state][['ECG', 'SCR', 'COR', 'ORB', 'ZYG', 'Emotion_Tone_Phase']]

    return df_final

#%%

# This function is used to rescale 'phase2' where necessary. 

def rescale(arr, factor):
    n = len(arr)
    return np.interp(np.linspace(0, n, factor*n+1), np.arange(n), arr)
#%%    
def emotions_tones_phases(df):
    # Baseline
    
    # Shallow
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 5) & (df['Tone1'] == 5) & (df['Tone2'] == 0) & (df['phase1'] == 0) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Fear_Shallow_Baseline"
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 0) & (df['Tone1'] == 5) & (df['Tone2'] == 0) & (df['phase1'] == 0) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Joy_Shallow_Baseline"
    df.loc[(df['Arousal'] == 0) & (df['Valence2'] == 0) & (df['Tone1'] == 5) & (df['Tone2'] == 0) & (df['phase1'] == 0) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Neutral_Shallow_Baseline"
    # Deep
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 5) & (df['Tone1'] == 0) & (df['Tone2'] == 5) & (df['phase1'] == 0) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Fear_Deep_Baseline"
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 0) & (df['Tone1'] == 0) & (df['Tone2'] == 5) & (df['phase1'] == 0) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Joy_Deep_Baseline"
    df.loc[(df['Arousal'] == 0) & (df['Valence2'] == 0) & (df['Tone1'] == 0) & (df['Tone2'] == 5) & (df['phase1'] == 0) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Neutral_Deep_Baseline"
    
    # Phase1
    
    # Shallow
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 5) & (df['Tone1'] == 5) & (df['Tone2'] == 0) & (df['phase1'] == 5) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Fear_Shallow_Phase1"
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 0) & (df['Tone1'] == 5) & (df['Tone2'] == 0) & (df['phase1'] == 5) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Joy_Shallow_Phase1"
    df.loc[(df['Arousal'] == 0) & (df['Valence2'] == 0) & (df['Tone1'] == 5) & (df['Tone2'] == 0) & (df['phase1'] == 5) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Neutral_Shallow_Phase1"
    # Deep
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 5) & (df['Tone1'] == 0) & (df['Tone2'] == 5) & (df['phase1'] == 5) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Fear_Deep_Phase1"
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 0) & (df['Tone1'] == 0) & (df['Tone2'] == 5) & (df['phase1'] == 5) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Joy_Deep_Phase1"
    df.loc[(df['Arousal'] == 0) & (df['Valence2'] == 0) & (df['Tone1'] == 0) & (df['Tone2'] == 5) & (df['phase1'] == 5) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Neutral_Deep_Phase1"

    # Phase2
    
    # Shallow
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 5) & (df['Tone1'] == 5) & (df['Tone2'] == 0) & (df['phase1'] == 0) & (df['phase2'] == 5), 'Emotion_Tone_Phase'] = "Fear_Shallow_Phase2"
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 0) & (df['Tone1'] == 5) & (df['Tone2'] == 0) & (df['phase1'] == 0) & (df['phase2'] == 5), 'Emotion_Tone_Phase'] = "Joy_Shallow_Phase2"
    df.loc[(df['Arousal'] == 0) & (df['Valence2'] == 0) & (df['Tone1'] == 5) & (df['Tone2'] == 0) & (df['phase1'] == 0) & (df['phase2'] == 5), 'Emotion_Tone_Phase'] = "Neutral_Shallow_Phase2"
    # Deep
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 5) & (df['Tone1'] == 0) & (df['Tone2'] == 5) & (df['phase1'] == 0) & (df['phase2'] == 5), 'Emotion_Tone_Phase'] = "Fear_Deep_Phase2"
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 0) & (df['Tone1'] == 0) & (df['Tone2'] == 5) & (df['phase1'] == 0) & (df['phase2'] == 5), 'Emotion_Tone_Phase'] = "Joy_Deep_Phase2"
    df.loc[(df['Arousal'] == 0) & (df['Valence2'] == 0) & (df['Tone1'] == 0) & (df['Tone2'] == 5) & (df['phase1'] == 0) & (df['phase2'] == 5), 'Emotion_Tone_Phase'] = "Neutral_Deep_Phase2"    
    
    df = df.reset_index(drop=True)
    
    return df
#%%
def drop_nan_values(df):
    
    df = df[df['Emotion_Tone_Phase'].notna()] 
    
    df = df.reset_index(drop=True)

    return df
#%%
def normalise(dataframe):
    
    states = dataframe['Emotion_Tone_Phase'].unique()
    normalised_data = []
    
    min_max_scaler = MinMaxScaler()
    
    for state in states:
        
        state_data = dataframe[dataframe['Emotion_Tone_Phase'] == state]
        
        normalised_state = min_max_scaler.fit_transform(state_data[['SCR', 'ECG', 'ORB','COR', 'ZYG']])
        normalised_df_tmp = pd.DataFrame(normalised_state, columns=['SCR', 'ECG', 'ORB', 'COR', 'ZYG'])
        
        normalised_df_tmp['Emotion_Tone_Phase'] = state
        
        normalised_data.append(normalised_df_tmp)
    
    normalised_df = pd.concat(normalised_data)
    
    return normalised_df        
    
 
#%%
def downsample(dataframe):
    
    states = dataframe['Emotion_Tone_Phase'].unique()

    downsampled_data = []
    
    N = 300
  
    for state in states:
        
        state_data = dataframe[dataframe['Emotion_Tone_Phase'] == state]  # Filter rows based on the current state
              
        downsampled_state = resample_poly(x=state_data[['SCR', 'ECG', 'ORB', 'COR', 'ZYG']], up=1, down=N, axis=0, padtype="mean")
        
        downsampled_df_tmp = pd.DataFrame(downsampled_state, columns=['SCR', 'ECG', 'ORB', 'COR', 'ZYG'])
        
        downsampled_df_tmp['Emotion_Tone_Phase'] = state
        
        downsampled_data.append(downsampled_df_tmp)
    
    downsampled_df = pd.concat(downsampled_data)
    
    return downsampled_df


#%%

def create_info_dictionary(csv_file, key_column, value_columns):
    data = pd.read_csv(csv_file)
    info_dict = {}

    for _, row in data.iterrows():
        key = row[key_column]
        values = [row[col] for col in value_columns]
        info_dict[key] = values

    return info_dict


#%%    
def feature_extraction(X, y, state, scale_features=True):
    
    # Extracting the first items (data frames) from each sub-dictionary
    dfs = [value['acq_data'] for value in X.values()]
    
    dfs = []
    keys = []
    
    # Iterate over each sub-dictionary
    for key, value in X.items():
        df = value['acq_data']  # Extract the data frame
        dfs.append(df)    # Append the data frame to the list
        keys.extend([key] * len(df))  # Add the key for each row
    
    # Concatenate the data frames
    concat_df = pd.concat(dfs)
    
    # Add the key column to the big DataFrame
    concat_df['id'] = keys
    
    
    data_x = concat_df[['ECG', 'SCR', 'COR', 'ORB', 'ZYG', 'id']]

    extraction_settings = EfficientFCParameters()
    X_extracted = extract_features(data_x, column_id='id',
                          default_fc_parameters=extraction_settings,
                          # we impute = remove all NaN features automatically
                          impute_function=impute, show_warnings=False)
    
    if scale_features == True: 
    
        min_max_scaler = MinMaxScaler()
        X_extracted_norm_tmp = min_max_scaler.fit_transform(X_extracted)
        X_extracted_norm = pd.DataFrame(X_extracted_norm_tmp, 
                                        index=X_extracted.index,
                                        columns=X_extracted.columns)
    else: 
        pass
    
    data_y = pd.Series(y)
    
    
    # This table is used to identify the top features for classification based on p_value 
    if scale_features == True:
        relevance_table_clf = calculate_relevance_table(X_extracted_norm, data_y)
    else:    
        relevance_table_clf = calculate_relevance_table(X_extracted, data_y)
    
    relevance_table_clf.sort_values("p_value", inplace=True)
    relevance_table_clf
    
    top_features = relevance_table_clf["feature"]
 
    if scale_features == True:
        x_features = X_extracted_norm[top_features]
    else:    
        x_features = X_extracted[top_features]  
    


    return x_features, relevance_table_clf
    
