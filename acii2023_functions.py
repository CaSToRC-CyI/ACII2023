#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%

import pandas as pd
import bioread
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from scipy.signal import resample_poly


from tsfresh import extract_features
from tsfresh.feature_selection.relevance import calculate_relevance_table
from tsfresh.feature_extraction import EfficientFCParameters
from tsfresh.utilities.dataframe_functions import impute
#%%

def read_acq_file(folder_path, datafile, state='Universal', normalise_data=True, downsample_data=True):
    """
    This function reads an acquisition file and performs various operations on the data.
    
    Parameters:
    - folder_path (str): Path to the folder containing the data file.
    - datafile (str): Name of the data file.
    - state (str, optional): State parameter to filter the data. Default is 'Universal'. The other options are:
        * 'Fear_Shallow_Phase1'
        * 'Fear_Deep_Phase1'
        * 'Fear_Shallow_Phase2'
        * 'Fear_Deep_Phase2'
        * 'Joy_Shallow_Phase1'
        * 'Joy_Deep_Phase1'
        * 'Joy_Shallow_Phase2'
        * 'Joy_Deep_Phase2'
        * 'Neutral_Shallow_Phase1'
        * 'Neutral_Deep_Phase1'
        * 'Neutral_Shallow_Phase2'
        * 'Neutral_Deep_Phase2'
    - normalise_data (bool, optional): Flag to indicate whether to normalise the data. Default is True.
    - downsample_data (bool, optional): Flag to indicate whether to downsample the data. Default is True.
    
    Returns:
    - df_final (pandas.DataFrame): Processed data in a DataFrame format.
    """
    
    # Read the acquisition file
    data = bioread.read(folder_path + datafile)

    # Extract relevant data channels from the acquisition file
    # (time, SCR, phase1, arousal, valence2, tone1, tone2, phase2, ECG BPM, ORB, COR, ZYG)
    """
    data.time_index # time
    data.channels[1].data # SCR
    data.channels[6].data # phase 1
    data.channels[7].data # arousal
    data.channels[9].data # valence 2
    data.channels[11].data # tone 1
    data.channels[12].data # tone 2
    data.channels[13].data # phase 2
    data.channels[17].data # ECG BPM
    data.channels[19].data # ORB
    data.channels[20].data # COR
    data.channels[21].data # ZYG
    """
        
    # Check if 'phase2' channel has the correct sampling rate
    if int(data.channels[13].samples_per_second) == 1000:
        # If the sampling rate is correct, create a DataFrame using the data channels
        df = pd.DataFrame([data.time_index, data.channels[1].data, data.channels[17].data,
                            data.channels[19].data, data.channels[20].data, data.channels[21].data,
                            data.channels[6].data, data.channels[7].data, data.channels[9].data,
                            data.channels[11].data, data.channels[12].data, data.channels[13].data])
    else: 
        # If the sampling rate is incorrect, scale up the 'phase2' channel and create a DataFrame
        phase_2_scaleup = rescale(data.channels[13].data, 8)
    
        df = pd.DataFrame([data.time_index, data.channels[1].data, data.channels[17].data,
                            data.channels[19].data, data.channels[20].data, data.channels[21].data,
                            data.channels[6].data, data.channels[7].data, data.channels[9].data,
                            data.channels[11].data, data.channels[12].data, phase_2_scaleup])
   
    # Transpose the DataFrame and assign column names
    df_T = df.transpose()
    df_T.columns = ['time','SCR', 'ECG','ORB','COR','ZYG','phase1','Arousal','Valence2',
                    'Tone1','Tone2','phase2']
        
    # Perform operations on the DataFrame
    df_emotions_tones_phases = emotions_tones_phases(df_T)
    df_clean = drop_nan_values(df_emotions_tones_phases)
    
    
    list_modified_files = ['12113.acq', '12116.acq', '12125.acq', '12236.acq', '32115.acq', '12001.acq'\
                           '12004.acq', '12010.acq', '32138.acq', '122306.acq', '122347.acq']
    if datafile in list_modified_files:
        df_modified = manual_processing_data(datafile, df_clean)
                        
    else:
        df_modified = df_clean
    
    # Downsample and/or normalize the data based on the input flags        
    if (downsample_data == True) and (normalise_data == True):       
        df_tmp = downsample(df_modified)        
        df_final = normalise(df_tmp)
    elif (downsample_data == True) and (normalise_data == False):
        df_final = downsample(df_modified)
    elif (downsample_data == False) and (normalise_data == True):
        df_final = normalise(df_modified)
    elif (downsample_data == False) and (normalise_data == False):   
        df_final = df_modified
        
    # Filter the data based on the 'state' parameter if provided
    if state == 'Universal':
        pass
    else:
        df_final = df_final[df_final['Emotion_Tone_Phase'] == state][['ECG', 'SCR', 'COR', 'ORB', 'ZYG', 'Emotion_Tone_Phase']]

    return df_final

#%%
def rescale(arr, factor):
    """
    Rescale an array by a given factor using linear interpolation.
    
    Parameters:
    - arr (numpy.ndarray): The input array to be rescaled.
    - factor (int): The scaling factor.
    
    Returns:
    - rescaled_arr (numpy.ndarray): The rescaled array.
    """
    #  Get the length of the input array
    n = len(arr)
    
    # Generate a new array with factor times more points using linear interpolation
    return np.interp(np.linspace(0, n, factor*n+1), np.arange(n), arr)
#%%    
def emotions_tones_phases(df):
    """
    Assign emotion, tone, and phase labels to a DataFrame based on specific conditions.
    
    Parameters:
    - df (pandas.DataFrame): The input DataFrame containing the data.
    
    Returns:
    - df (pandas.DataFrame): The updated DataFrame with the 'Emotion_Tone_Phase' column added.
    """
    
    # Baseline    
    # Shallow baseline emotions
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 5) & (df['Tone1'] == 5) & (df['Tone2'] == 0) & (df['phase1'] == 0) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Fear_Shallow_Baseline"
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 0) & (df['Tone1'] == 5) & (df['Tone2'] == 0) & (df['phase1'] == 0) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Joy_Shallow_Baseline"
    df.loc[(df['Arousal'] == 0) & (df['Valence2'] == 0) & (df['Tone1'] == 5) & (df['Tone2'] == 0) & (df['phase1'] == 0) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Neutral_Shallow_Baseline"
    
    # Deep baseline emotions
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 5) & (df['Tone1'] == 0) & (df['Tone2'] == 5) & (df['phase1'] == 0) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Fear_Deep_Baseline"
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 0) & (df['Tone1'] == 0) & (df['Tone2'] == 5) & (df['phase1'] == 0) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Joy_Deep_Baseline"
    df.loc[(df['Arousal'] == 0) & (df['Valence2'] == 0) & (df['Tone1'] == 0) & (df['Tone2'] == 5) & (df['phase1'] == 0) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Neutral_Deep_Baseline"
    
    # Phase1  
    # Shallow phase1 emotions
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 5) & (df['Tone1'] == 5) & (df['Tone2'] == 0) & (df['phase1'] == 5) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Fear_Shallow_Phase1"
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 0) & (df['Tone1'] == 5) & (df['Tone2'] == 0) & (df['phase1'] == 5) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Joy_Shallow_Phase1"
    df.loc[(df['Arousal'] == 0) & (df['Valence2'] == 0) & (df['Tone1'] == 5) & (df['Tone2'] == 0) & (df['phase1'] == 5) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Neutral_Shallow_Phase1"
    
    # Deep phase1 emotions
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 5) & (df['Tone1'] == 0) & (df['Tone2'] == 5) & (df['phase1'] == 5) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Fear_Deep_Phase1"
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 0) & (df['Tone1'] == 0) & (df['Tone2'] == 5) & (df['phase1'] == 5) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Joy_Deep_Phase1"
    df.loc[(df['Arousal'] == 0) & (df['Valence2'] == 0) & (df['Tone1'] == 0) & (df['Tone2'] == 5) & (df['phase1'] == 5) & (df['phase2'] == 0), 'Emotion_Tone_Phase'] = "Neutral_Deep_Phase1"

    # Phase2   
    # Shallow phase2 emotions
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 5) & (df['Tone1'] == 5) & (df['Tone2'] == 0) & (df['phase1'] == 0) & (df['phase2'] == 5), 'Emotion_Tone_Phase'] = "Fear_Shallow_Phase2"
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 0) & (df['Tone1'] == 5) & (df['Tone2'] == 0) & (df['phase1'] == 0) & (df['phase2'] == 5), 'Emotion_Tone_Phase'] = "Joy_Shallow_Phase2"
    df.loc[(df['Arousal'] == 0) & (df['Valence2'] == 0) & (df['Tone1'] == 5) & (df['Tone2'] == 0) & (df['phase1'] == 0) & (df['phase2'] == 5), 'Emotion_Tone_Phase'] = "Neutral_Shallow_Phase2"
    # Deep phase2 emotions
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 5) & (df['Tone1'] == 0) & (df['Tone2'] == 5) & (df['phase1'] == 0) & (df['phase2'] == 5), 'Emotion_Tone_Phase'] = "Fear_Deep_Phase2"
    df.loc[(df['Arousal'] == 5) & (df['Valence2'] == 0) & (df['Tone1'] == 0) & (df['Tone2'] == 5) & (df['phase1'] == 0) & (df['phase2'] == 5), 'Emotion_Tone_Phase'] = "Joy_Deep_Phase2"
    df.loc[(df['Arousal'] == 0) & (df['Valence2'] == 0) & (df['Tone1'] == 0) & (df['Tone2'] == 5) & (df['phase1'] == 0) & (df['phase2'] == 5), 'Emotion_Tone_Phase'] = "Neutral_Deep_Phase2"    
    
    df = df.reset_index(drop=True)
    
    return df

#%%
def trial_order(df):
    
    # Create a dictionary to store the indices where the values change for each column in the DataFrame.
    changes = {}
    
    # Iterate through each column in the DataFrame.
    for col in df.columns:
        # Calculate the indices where the values in the column change and store them in a list.
        # The zip function pairs up consecutive elements, and the enumerate function provides the index.
        # The condition "i != j" checks if the current element is different from the next one (indicating a change).
        # The list comprehension creates a list of indices with 1 added to each index (to account for the shift caused by zip).
        # The first element is set to 0 to represent the first row, which is always considered as a change (to capture the baseline).
        changes[col] = [0] + [idx for idx, (i, j) in enumerate(zip(df[col], df[col][1:]), 1) if i != j]
        
    # Extract the list of indices where changes occurred in the "Emotion_Tone_Phase" column.
    list_ETP_changes = []
    for i in changes["Emotion_Tone_Phase"]:
        list_ETP_changes.append(i)
     
    # Extract the names corresponding to the indices where changes occurred in the "Emotion_Tone_Phase" column.
    list_ETP_changes_names = []
    for i in list_ETP_changes:
        list_ETP_changes_names.append(df["Emotion_Tone_Phase"][i])
               
    # Calculate the differences between consecutive elements in the list of changes.
    list_ETP_changes_diff = [x - list_ETP_changes[i - 1] for i, x in enumerate(list_ETP_changes)][1:]

    # Combine the differences, indices, and names into a list of tuples.    
    list_ETP_changes_ = list(zip(list_ETP_changes_diff, list_ETP_changes, list_ETP_changes_names))
   
    # Create a list of ranges, where each range consists of two consecutive elements from the list of changes.
    # Note: The first range is ignored as it represents the baseline.
    ranges_list = []
    for i, v in enumerate(list_ETP_changes):
        ranges_list.append([list_ETP_changes[i-1], list_ETP_changes[i]])
        
    # Remove the first range from the list (as it represents the baseline).
    ranges_list = ranges_list[1:]

    # Return the list of tuples containing changes and the list of ranges.
    return list_ETP_changes_, ranges_list

#%%

def manual_processing_data(datafile, df):
    
    df_order = trial_order(df)
    
    if datafile == '12113.acq':
        df.loc[df_order[1][28][0]:df_order[1][28][1]-1, "Emotion_Tone_Phase"] = 'Joy_Deep_Baseline' 
        df.loc[df_order[1][29][0]:df_order[1][29][1]-1, "Emotion_Tone_Phase"] = 'Joy_Deep_Phase1'
        df.loc[df_order[1][30][0]:df_order[1][30][1]-1, "Emotion_Tone_Phase"] = 'Joy_Deep_Phase2'
        df.loc[df_order[1][31][0]:df_order[1][31][1]-1, "Emotion_Tone_Phase"] = 'Joy_Shallow_Baseline'
        df.loc[df_order[1][32][0]:df_order[1][32][1]-1, "Emotion_Tone_Phase"] = 'Joy_Shallow_Phase1'
        
    elif datafile == '12116.acq':
        df.loc[df_order[1][5][0]:df_order[1][5][1]-1, "Emotion_Tone_Phase"] = 'Joy_Shallow_Phase2'
        df.loc[df_order[1][7][0]:df_order[1][7][1]-1, "Emotion_Tone_Phase"] = 'Joy_Shallow_Phase2'
        
    elif datafile == '12125.acq':
        df.loc[df_order[1][22][0]:df_order[1][22][1]-1, "Emotion_Tone_Phase"] = 'Joy_Deep_Phase1'
        df.loc[df_order[1][24][0]:df_order[1][24][1]-1, "Emotion_Tone_Phase"] = 'Joy_Deep_Phase2'
        
    elif datafile == '12236.acq':
        df = df.loc[df_order[1][56][0]:df.shape[0]-1]

    elif datafile == '32115.acq':
        df.loc[df_order[1][8][0]:df_order[1][8][1]-1, "Emotion_Tone_Phase"] = 'Joy_Deep_Baseline'
        df.loc[df_order[1][9][0]:df_order[1][9][1]-1, "Emotion_Tone_Phase"] = 'Joy_Deep_Phase1'
        df.loc[df_order[1][10][0]:df_order[1][10][1]-1, "Emotion_Tone_Phase"] = 'Joy_Deep_Phase2'
        df.loc[df_order[1][12][0]:df_order[1][12][1]-1, "Emotion_Tone_Phase"] = 'Joy_Deep_Phase2'
        df.loc[df_order[1][13][0]:df_order[1][13][1]-1, "Emotion_Tone_Phase"] = 'Joy_Shallow_Baseline'
        df.loc[df_order[1][14][0]:df_order[1][14][1]-1, "Emotion_Tone_Phase"] = 'Joy_Shallow_Phase1'
        df.loc[df_order[1][15][0]:df_order[1][15][1]-1, "Emotion_Tone_Phase"] = 'Joy_Shallow_Phase2'
        
    elif datafile == '12001.acq':
        df = df.loc[df_order[1][107][0]:df.shape[0]-1]

        
    elif datafile == '12004.acq':
        df = df.loc[df_order[1][1][0]:df.shape[0]-1]

    elif datafile == '12010.acq':
        df.loc[df_order[1][0][0]:df_order[1][0][1]-1, "Emotion_Tone_Phase"] = 'Joy_Shallow_Baseline'
        df.loc[df_order[1][1][0]:df_order[1][1][1]-1, "Emotion_Tone_Phase"] = 'Joy_Shallow_Phase1'
        
    elif datafile == '32138.acq':
        df = df.loc[df_order[1][1][0]:df.shape[0]-1]


    elif datafile == '122306.acq':
        df = df.loc[df_order[1][1][0]:df.shape[0]-1]
     
    elif datafile == '122347.acq':
        df = df.loc[df_order[1][1][0]:df.shape[0]-1]

    return df

#%%
def drop_nan_values(df):
    """
    Drop rows with NaN values in the 'Emotion_Tone_Phase' column and reset the index.
    
    Parameters:
    - df (pandas.DataFrame): The input DataFrame containing the data.
    
    Returns:
    - df (pandas.DataFrame): The updated DataFrame with NaN rows removed and the index reset.
    """

    # Drop rows with NaN values in the 'Emotion_Tone_Phase' column    
    df = df[df['Emotion_Tone_Phase'].notna()] 
    
    # Reset the index of the DataFrame
    df = df.reset_index(drop=True)

    return df
#%%
def normalise(dataframe):
    """
    Normalize the data in the DataFrame based on the 'Emotion_Tone_Phase' column.
    
    Parameters:
    - dataframe (pandas.DataFrame): The input DataFrame containing the data.
    
    Returns:
    - normalised_df (pandas.DataFrame): The normalized DataFrame.
    """
    
    # Get unique values in the 'Emotion_Tone_Phase' column
    states = dataframe['Emotion_Tone_Phase'].unique()
    
    # List to store normalized data
    normalised_data = []
    # Create a MinMaxScaler object for normalizat
    min_max_scaler = MinMaxScaler()
    
    
    for state in states:
        # Select data for a specific state
        state_data = dataframe[dataframe['Emotion_Tone_Phase'] == state]
        # Normalize selected columns (SCR, ECG, ORB, COR, ZYG) using MinMaxScaler
        normalised_state = min_max_scaler.fit_transform(state_data[['SCR', 'ECG', 'ORB','COR', 'ZYG']])
        # Create a DataFrame from the normalized state data with column names
        normalised_df_tmp = pd.DataFrame(normalised_state, columns=['SCR', 'ECG', 'ORB', 'COR', 'ZYG'])
        # Add 'Emotion_Tone_Phase' column to the normalized DataFrame and assign the state value
        normalised_df_tmp['Emotion_Tone_Phase'] = state
        # Append the normalized DataFrame to the list of normalized data
        normalised_data.append(normalised_df_tmp)
        
    # Concatenate all the normalized DataFrames into a single DataFrame
    normalised_df = pd.concat(normalised_data)
    
    return normalised_df        
    
 
#%%
def downsample(dataframe):
    """
    Downsample the data in the DataFrame based on the 'Emotion_Tone_Phase' column.
    
    Parameters:
    - dataframe (pandas.DataFrame): The input DataFrame containing the data.
    
    Returns:
    - downsampled_df (pandas.DataFrame): The downsampled DataFrame.
    """
    # Get unique values in the 'Emotion_Tone_Phase' column
    states = dataframe['Emotion_Tone_Phase'].unique()
    
    # List to store downsampled data
    downsampled_data = []  
    
    # Number of samples for downsmapling window
    N = 300
  
    for state in states:
        # Select data for a specific state
        state_data = dataframe[dataframe['Emotion_Tone_Phase'] == state]  # Filter rows based on the current state
        # Downsample selected columns (SCR, ECG, ORB, COR, ZYG) using resample_poly
        downsampled_state = resample_poly(x=state_data[['SCR', 'ECG', 'ORB', 'COR', 'ZYG']], up=1, down=N, axis=0, padtype="mean")
        # Create a DataFrame from the downsampled state data with column names
        downsampled_df_tmp = pd.DataFrame(downsampled_state, columns=['SCR', 'ECG', 'ORB', 'COR', 'ZYG'])
        # Add 'Emotion_Tone_Phase' column to the downsampled DataFrame and assign the state value
        downsampled_df_tmp['Emotion_Tone_Phase'] = state
        # Append the downsampled DataFrame to the list of downsampled data
        downsampled_data.append(downsampled_df_tmp)
    
    # Concatenate all the downsampled DataFrames into a single DataFrame
    downsampled_df = pd.concat(downsampled_data)
    
    return downsampled_df


#%%

def create_info_dictionary(csv_file, key_column, value_columns):
    """
    Create a dictionary from a CSV file where the key is taken from a specified column and the values are taken from
    specified columns in each row of the CSV file.
    
    Parameters:
    - csv_file (str): The path to the CSV file.
    - key_column (str): The column name to be used as the key in the dictionary.
    - value_columns (list): A list of column names to be used as values in the dictionary.
    
    Returns:
    - info_dict (dict): The created dictionary where each key is associated with a list of corresponding values.
    """
    
    # Read the CSV file into a DataFrame
    data = pd.read_csv(csv_file)
    
    # Initialise an empty dictionary to store the information
    info_dict = {}

    # Iterate over each row in the DataFrame
    for _, row in data.iterrows():
        key = row[key_column]  # Get the value from the specified key column
        values = [row[col] for col in value_columns]  # Extract the values from the specified value columns for the current row
        info_dict[key] = values  # Assign the values to the key in the dictionary

    return info_dict


#%%    
def feature_extraction(X, y, state, scale_features=True):
    """
    Perform feature extraction from the given input data (X) and target labels (y).
    
    Parameters:
    - X (dict): The input data in the form of a dictionary, where each key corresponds to a sample ID and
                each value is a dictionary containing the 'acq_data' DataFrame.
    - y (array-like): The target labels associated with the input data.
    - state (str): The state for which feature extraction is performed.
    - scale_features (bool): Flag indicating whether to scale the extracted features.
    
    Returns:
    - x_features (pandas.DataFrame): The extracted features.
    - relevance_table_clf (pandas.DataFrame): The relevance table for the extracted features based on p-values.
    """
    
    # Select relevant columns for feature extraction
    data_x = X[['ECG', 'SCR', 'COR', 'ORB', 'ZYG', 'id']]
    
    extraction_settings = EfficientFCParameters() # Define the feature extraction settings
    X_extracted = extract_features(data_x, column_id='id',  # Perform feature extraction
                          default_fc_parameters=extraction_settings,
                          # we impute = remove all NaN features automatically
                          impute_function=impute, show_warnings=False)
    
    # Excluding any label that its id might not be present in the extracted features
    idx_data = y.index
    idx_features = X_extracted.index 
    idx_difference = idx_data.difference(idx_features)
    
    # Selecting the labels for either classification or regression
    y_data = y.drop(index=idx_difference, axis=0)
    # y_data = y_data['Alexithymic_Vs_Control'].squeeze()
    
    if scale_features == True: 
    
        min_max_scaler = MinMaxScaler() # Create a MinMaxScaler object
        X_extracted_norm_tmp = min_max_scaler.fit_transform(X_extracted)  # Scale the extracted features
        X_extracted_norm = pd.DataFrame(X_extracted_norm_tmp, # Create a DataFrame from the scaled features
                                        index=X_extracted.index,
                                        columns=X_extracted.columns)
    else: 
        pass # If scaling is not required, do nothing
    
    # Calculate the relevance table for the extracted features based on p-values
    if scale_features == True:
        relevance_table_clf = calculate_relevance_table(X_extracted_norm, y_data)
    else:    
        relevance_table_clf = calculate_relevance_table(X_extracted, y_data)
    
    # Sort the relevance table by p-values
    relevance_table_clf.sort_values('p_value', inplace=True)
    
    if scale_features == True:
        x_features = X_extracted_norm
    else:    
        x_features = X_extracted 
    
    return x_features, relevance_table_clf
    
