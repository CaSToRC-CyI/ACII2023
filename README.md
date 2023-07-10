# ACII2023: Alexithymia Database Instructions

# Description
The Alexithymia Database consists of two datasets that include five physiological signals and several digital channels associated with the experiment state. It is designed to provide insights into the emotios of people with alexithymia. This readme file aims to guide users on how to effectively use and understand the datasets. 

# File Structure
The dataset files are provided in two formats: ACQ files and a comma-separated values (CSV) format file for demographics information.

- ACQ files: The datasets are stored in ACQ files, which are data graph files created by AcqKnowledge. Each ACQ file represents data for a single participant. These files contain the recorded physiological signals and various digital channels related to the state of the experiment.
- Demographics CSV file: In addition to the ACQ files, a separate CSV file is available to access demographics information about the participants. This file provides details such as ID, age, gender, group label, etc. It complements the ACQ files by providing additional contextual information about the participants.

# Dataset Columns
## ACQ files
0. Channel ECG
1. Channel SCR
2. Channel ORB
3. Channel COR
4. Channel ZYG
5. Channel Sound
6. Channel phase1
7. Channel Arousal
8. Channel Valence1
9. Channel Valence2
10. Channel Probe ON
11. Channel Tone1
12. Channel Tone2
13. Channel phase2
14. Channel ORB Filter
15. Channel COR Filter
16. Channel ZYG Filter
17. Channel ECG BPM
18. Channel Trial counter
19. Channel ORB Int
20. Channel COR Int
21. Channel ZYG Int
22. Channel ECG R-R
23. Channel Pulse Rate

We are interested into specific columns, therefore follow the instructions below to extract only the necessary data. 

## CSV file
- id:
- gender
- age
- TASDIF
- TASDDF
- TASEOT
- TAStot
- group
- dataset

# Data Usage Instructions
1. Fork the GitHub repository containing the Alexithymia Database Instructions to your own GitHub account. This will create a copy of the repository under your account.
2. Clone the forked repository to your local machine using Git. Open a terminal or command prompt and run the following command:
```sh
git clone https://github.com/CaSToRC-CyI/ACII2023.git
```
Replace `your-username` with your actual GitHub username.
3. Navigate to the cloned repository on your local machine:
```sh
cd ACII2023
```
4. Ensure that you have Python installed on your system. You can download Python from the official website be clicking [here](https://www.python.org/downloads/)
5. Install the necessary libraries by running the following command in your command prompt or terminal:
```sh
pip install bioread
pip install pandas
pip install numpy
```
6. Load the files using the scripts found in the following links:
- Dataset 1:
  - [Low alexithymics](https://github.com/CaSToRC-CyI/ACII2023/blob/main/dataset1_low_dictionaries.py)
  - [High alexithymics](https://github.com/CaSToRC-CyI/ACII2023/blob/main/dataset1_high_dictionaries.py)
- Dataset 2:
  - [Low alexithymics](https://github.com/CaSToRC-CyI/ACII2023/blob/main/dataset2_low_dictionaries.py)
  - [Medium alexithymics](https://github.com/CaSToRC-CyI/ACII2023/blob/main/dataset2_medium_dictionaries.py)
  - [High alexithymics](https://github.com/CaSToRC-CyI/ACII2023/blob/main/dataset2_high_dictionaries.py)

How to load data: 
#### Step 1:
Read the csv file which contains the group label and the dataset label.
```sh
# Import librarires
from acii2023_functions import create_info_dictionary

# CSV file path
csv_file = '/Users/user/Desktop/ACII2023_Datasets/alexithymia_demographics_info.csv'

# ID would be the key column of the dictionary
key_column = 'id'

# Group and dataset labels would be the values of the dictionary
value_columns = ['group', 'dataset'] 

# Dictionary containing information for each participant
info_dict = create_info_dictionary(csv_file, key_column, value_columns)
```
Replace `csv_file` with your actual csv path.

#### Step 2:
Load data of specific participant from dataset 1 with high alexithymia:. 
```sh
# Import librarires
from acii2023_functions import read_acq_file, rescale

# Folder path
folder_path = '/Users/user/Desktop/ACII2023_Datasets/Dataset1/HighAlexithymics/'

# Dictionary of participant 11251
participant_11251 = {'11251': {'acq_data': read_acq_file(folder_path, '11251.acq'),\
                               'group_label': info_dict[11251][0],\
                               'dataset': info_dict[11251][1]}}
```
Replace `folder_path` with your actual path.

> Note: The **phase2** channel has been sampled at 125 Hz. In the above code, **phase2** has been rescaled to be 1000 Hz as the other columns. 



| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |
