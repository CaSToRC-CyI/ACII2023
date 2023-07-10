# ACII2023: Alexithymia Database Instructions

# Description
The Alexithymia Database consists of two datasets that include five physiological signals and several digital channels associated with the experiment state. It is designed to provide insights into the emotios of people with alexithymia. This readme file aims to guide users on how to effectively use and understand the datasets. 

# File Structure
The dataset files are provided in two formats: ACQ files and a comma-separated values (CSV) format file for demographics information.

- ACQ files: The datasets are stored in ACQ files, which are data graph files created by AcqKnowledge. Each ACQ file represents data for a single participant. These files contain the recorded physiological signals and various digital channels related to the state of the experiment.
- Demographics CSV file: In addition to the ACQ files, a separate CSV file is available to access demographics information about the participants. This file provides details such as ID, age, gender, group label, etc. It complements the ACQ files by providing additional contextual information about the participants.

# Dataset Columns
## ACQ files
0. Channel ECG: Ignore
1. Channel SCR: Skin conductance response level
2. Channel ORB: Ignore 
3. Channel COR: Ignore
4. Channel ZYG: Ignore
5. Channel Sound: Ignore
6. Channel phase1: Digital channel indicating first imagery period
7. Channel Arousal: Digital channel indicating low/high arousal of emotion
8. Channel Valence1: Ignore
9. Channel Valence2: Digital channel indicating the presence of negative emotion
10. Channel Probe ON: Ignore
11. Channel Tone1: Digital channel indicating shallow depth of processing
12. Channel Tone2: Digital channel indicating deep depth of processing
13. Channel phase2: Digital channel indicating second imagery period
14. Channel ORB Filter: Ignore
15. Channel COR Filter: Ignore
16. Channel ZYG Filter: Ignore
17. Channel ECG BPM: Electrocardiogram
18. Channel Trial counter: Ignore
19. Channel ORB Int: Electromyography of orbicularis
20. Channel COR Int: Electromyography of corrugator
21. Channel ZYG Int: Electromyography of zygomaticus
22. Channel ECG R-R: Ignore
23. Channel Pulse Rate: Ignore

We are interested into specific columns, therefore follow the instructions below to extract only the necessary data. 

### Digital channels
**Emotions**
The relationship between arousal and valence can help interpret emotional states in the dataset. Based on the provided mappings, the following associations can be made:
- When Arousal = 5 and Valence2 = 0, it corresponds to the emotion of _Joy_.
- When Arousal = 0 and Valence2 = 0, it corresponds to a _Neutral_ emotional state.
- When Arousal = 5 and Valence2 = 5, it corresponds to the emotion of _Fear_.

These mappings can provide insights into the emotional experiences represented in the dataset.

**Phases**
The data collection protocol consisted of three distinct phases: a 20-second baseline, a 60-second phase 1, and a 40-second phase 2. Each participant completed a total of 10 trials, resulting in a cumulative data duration of 1200 seconds for each participant.

To identify and extract the relevant data for analysis, it is important to focus on the specific digital channels corresponding to the Baseline, Phase1, and Phase2 periods. The data collected between these phases should be disregarded as it does not pertain to the targeted experimental periods.

By filtering the dataset using the digital channels associated with the Baseline, Phase1, and Phase2, you can ensure that only the desired segments of data are considered for further analysis.
- When Phase1 = 0 and Phase2 = 0, it corresponds to the phase of _Baseline_.
- When Phase1 = 5 and Phase2 = 0, it corresponds to the phase of _Phase1_.
- When Phase1 = 0 and Phase2 = 5, it corresponds to the phase of _Phase2_.

These mappings can provide insights into the phase of the experiment in the dataset.

**Depth of processing**
By filtering the dataset using the digital channels associated with the Tone1 and Tone2, you can ensure that only the desired segments of data are considered for further analysis.
- When Tone1 = 5 and Tone2 = 0, it corresponds to the phase of _Shallow_.
- When Tone1 = 0 and Tone2 = 5, it corresponds to the phase of _Deep_.

These mappings can provide insights into the depth of processing of the experiment in the dataset.

## CSV file
- id: Participant ID
- gender: Gender of participant
- age: Age of participant
- TASDIF: TAS sub-score for difficulty identifying feelings  
- TASDDF: TAS sub-score for difficulty describing feelings
- TASEOT: TAS sub-score for external-oriented thinking
- TAStot: TAS total score
- group: Label of alexithymia; low (0), medium (1), high (2)
- dataset: Label of dataset; dataset1 (1) and dataset2 (2)

# Data Usage Instructions
1. Fork the GitHub repository containing the Alexithymia Database Instructions to your own GitHub account. This will create a copy of the repository under your account.
2. Clone the forked repository to your local machine using Git. Open a terminal or command prompt and run the following command:
```sh
git clone https://github.com/CaSToRC-CyI/ACII2023.git
```
3. Navigate to the cloned repository on your local machine, for example:
```sh
cd /Users/user/Documents/GitHub/ACII2023
```
4. Ensure that you have Python installed on your system. You can download Python from the official website be clicking [here](https://www.python.org/downloads/)
5. Install the necessary libraries by running the following command in your command prompt or terminal:
```sh
pip install bioread
pip install pandas
pip install numpy
```
6. Download the datasets upon request and save them in the directory in a folder called _ACII2023_Datasets_. Contact X for further instructions. 

Structure of the _ACII2023_Datasets_ folder:
- Dataset 1:
  - LowAlexithymics
  - HighAlexithymics
- Dataset 2:
  - LowAlexithymics
  - MediumAlexithymics
  - HighAlexithymics

7. Load the files using the scripts found in the following links:
- Dataset 1:
  - [Low alexithymics](https://github.com/CaSToRC-CyI/ACII2023/blob/main/dataset1_low_dictionaries.py)
  - [High alexithymics](https://github.com/CaSToRC-CyI/ACII2023/blob/main/dataset1_high_dictionaries.py)
- Dataset 2:
  - [Low alexithymics](https://github.com/CaSToRC-CyI/ACII2023/blob/main/dataset2_low_dictionaries.py)
  - [Medium alexithymics](https://github.com/CaSToRC-CyI/ACII2023/blob/main/dataset2_medium_dictionaries.py)
  - [High alexithymics](https://github.com/CaSToRC-CyI/ACII2023/blob/main/dataset2_high_dictionaries.py)

Load the datasets:

#### Step 1:
Read the csv file which contains the group label and the dataset label.
```sh
# Import librarires
from acii2023_functions import create_info_dictionary

# CSV file path
csv_file = '/Users/user/Desktop/ACII2023/ACII2023_Datasets/alexithymia_demographics_info.csv'

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
folder_path = '/Users/user/Desktop/ACII2023/ACII2023_Datasets/Dataset1/HighAlexithymics/'

# Dictionary of participant 11251
participant_11251 = {'11251': {'acq_data': read_acq_file(folder_path, '11251.acq'),\
                               'group_label': info_dict[11251][0],\
                               'dataset': info_dict[11251][1]}}
```
Replace `folder_path` with your actual path.

> Note: The **phase2** channel has been sampled at 125 Hz. In the above code, **phase2** has been rescaled to be 1000 Hz as the other columns.


