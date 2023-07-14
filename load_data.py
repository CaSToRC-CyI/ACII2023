#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 12:33:20 2023

@author: k19038vf
"""
#%%

from acii2023_functions import read_acq_file, feature_extraction

#%%

def load_participant_data(folder_path, filename, info_dict, normalise=True, downsample=True, state='Universal'):
    """
    Load participant data from a file and return a dictionary containing the data and associated information.
    
    Parameters:
    - folder_path (str): The path to the folder containing the data file.
    - filename (str): The name of the data file.
    - info_dict (dict): The dictionary containing information about participants.
    - normalise (bool): Flag indicating whether to normalize the data.
    - downsample (bool): Flag indicating whether to downsample the data.
    - state (str): The state for filtering the data.
    
    Returns:
    - participant_dict (dict): A dictionary containing the participant data and associated information.
    """
    
    string = filename
    
    dot_index = string.index('.')  # Find the index of the dot in the filename
    numerical_part = string[:dot_index]  # Extract the numerical part of the filename
    number = int(numerical_part) # Convert the numerical part to an integer
    
    # Create a dictionary to store participant data and associated information
    participant_dict = {'acq_data': read_acq_file(folder_path, filename, state, normalise_data=normalise, downsample_data=downsample),\
                        'group_label': info_dict[number][0],\
                        'dataset': info_dict[number][1],\
                        'TASDIF': info_dict[number][2],\
                        'TASDDF': info_dict[number][3],\
                        'TASEOT': info_dict[number][4],\
                        'TAStot':info_dict[number][5]}
             
    return participant_dict


#%%

def load_dataset(folder_path, participant_list, info_dict, normalise=True, downsample=True, tsfresh=False, state='Universal', scale_features=True):
    """
    Load a dataset consisting of participant data and their corresponding labels.
    
    Parameters:
    - folder_path (str): The path to the folder containing the data files.
    - participant_list (list): A list of participant filenames.
    - info_dict (dict): The dictionary containing information about participants.
    - normalise (bool): Flag indicating whether to normalise the data.
    - downsample (bool): Flag indicating whether to downsample the data.
    - tsfresh (bool): Flag indicating whether to perform feature extraction using tsfresh.
    - state (str): The state for filtering the data. Default is 'Universal'. The other options are:
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
    - scale_features (bool): Flag indicating whether to scale the extracted features.
    
    Returns:
    Only returned if tsfresh is False
    - X (dict): A dictionary containing the participant data, where each key corresponds to a participant ID.
    - y (dict): A dictionary containing the participant labels, where each key corresponds to a participant ID.
      
    Only returned if tsfresh is True.
    - features (pandas.DataFrame): Extracted features using tsfresh. 
    - relevance_table (pandas.DataFrame): The relevance table for the extracted features.
    """
    
    X = {} # Dictionary to store participant data
    y = {} # Dictionary to store participant labels
    
    for participant in participant_list:
        # Load participant data
        df = load_participant_data(folder_path, participant, info_dict, normalise, downsample, state)
        dot_index = participant.index('.') # Find the index of the dot in the participant filename
        numerical_part = participant[:dot_index] # Extract the numerical part of the participant filename
        X[numerical_part] = df # Store the participant data in the X dictionary
        y[numerical_part] = info_dict[int(numerical_part)][0] # Store the participant label in the y dictionary
                  
    if tsfresh == False: 
        return X, y # Return the participant data (X) and labels (y)
    elif tsfresh == True:
        features, relevance_table = feature_extraction(X, y, state, scale_features) # Perform feature extraction using tsfresh
        
        return features, relevance_table # Return the extracted features and the relevance table

    



