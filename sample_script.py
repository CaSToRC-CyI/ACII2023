#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 15:00:39 2023

@author: k19038vf
"""

#%%
from load_data import load_dataset
from csv_dictionary import create_info_dictionary
import pandas as pd
from sklearn.model_selection import train_test_split
from acii2023_functions import feature_extraction
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
#%%

folder_path_dataset1_low = '/Users/user/Desktop/ACII2023_Datasets/Dataset1/LowAlexithymics/'
dataset1_low_list = ['12010.ACQ', '12004.acq', '31150.acq', '21143.acq']

folder_path_dataset1_high = '/Users/user/Desktop/ACII2023_Datasets/Dataset1/HighAlexithymics/'
dataset1_high_list = ['32115.acq', '22258.acq', '11254.acq', '12239.ACQ']

#%%
# csv file path
csv_file = '/Users/user/Desktop/ACII2023_Datasets/alexithymia_demographics_info.csv'

# Dictionary containing information for each participant
info_dict = create_info_dictionary(csv_file, 'id', ['group', 'dataset', 'TASDIF', 'TASDDF', 'TASEOT', 'TAStot'])

                 
#%%

# Load the dataset for low-level participants
X_1_low, y_1_low = load_dataset(folder_path_dataset1_low, dataset1_low_list, info_dict,\
                                normalise=True, downsample=True,\
                                state='Neutral_Deep_Phase1', tsfresh=True)

# Load the dataset for high-level participants
X_1_high, y_1_high = load_dataset(folder_path_dataset1_high,\
                                  dataset1_high_list, info_dict,\
                                  normalise=True, downsample=True,\
                                  state='Neutral_Deep_Phase1', tsfresh=True)
    
    
# Concatenate the X data frames vertically
df_X = pd.concat([X_1_low, X_1_high], axis=0)    
    
# Concatenate the dictionaries for y labels
dict_y = dict(y_1_low, **y_1_high)
df_y = pd.Series(dict_y)

# Perform feature extraction
features, relevance_table = feature_extraction(df_X, df_y, 'Universal', scale_features=True)

# Select the top 10 relevant features
top_features_table = relevance_table["feature"].head(10)
top_features = features[top_features_table]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(top_features, df_y, test_size=0.33, random_state=42)


# Instantiate the logistic regression model
logreg = LogisticRegression()

# Train the logistic regression model
logreg.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = logreg.predict(X_test)

# Calculate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Calculate the F1-score (assuming label 2 as the positive class when no medium group is included)
f1 = f1_score(y_test, y_pred, pos_label=2) 
print("F1-Score:", f1)
