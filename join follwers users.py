import glob
import os
import pandas as pd

path_to_json = 'D:/json/' ## your folder location

json_pattern = os.path.join(path_to_json,'*.json')
file_list = glob.glob(json_pattern)

dfs = [] # an empty list to store the data frames
for file in file_list:
    data = pd.read_json(file) # read data frame from json file
    dfs.append(data) # append the data frame to the list

temp = pd.concat(dfs, ignore_index=True) # concatenate all the data frames in the list.

temp.to_csv('FollowersCheck.csv')