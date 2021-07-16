#!/usr/bin/env python3
import pandas as pd
import os
from sklearn.model_selection import train_test_split


# For the train set
train_path  = "data/train"

# If the folder does not exist, create it 
if not os.path.exists(train_path):
    os.mkdir(train_path)

# For the dev set
dev_path = "data/dev"

# If the folder does not exist, create it 
if not os.path.exists(dev_path):
    os.mkdir(dev_path) 


df = pd.read_csv('elvina_voxforge_train.tsv', delimiter = '\t')
sorted_df = df.sort_values(by=['utterance_id'], ascending=True)

train_d, dev_d = train_test_split(sorted_df, test_size = 0.20,train_size = 0.80, random_state = 5)

train_data = train_d.sort_values(by=['utterance_id'], ascending=True)
dev_data = dev_d.sort_values(by=['utterance_id'], ascending=True)

train_data_filepath = os.path.join(train_path,'train.tsv')
dev_data_filepath = os.path.join(dev_path,'dev.tsv')

train_data.to_csv(train_data_filepath,sep='\t', index = False, header = True)
dev_data.to_csv(dev_data_filepath,sep='\t', index = False, header = True ) 

train_ids = set(train_data['utterance_id'].astype(str))
dev_ids = set(dev_data['utterance_id'].astype(str))



def dev_train_data_split(train_ids,dev_ids,filename,id_index):

    train_file_path = os.path.join(train_path,filename)
    dev_file_path = os.path.join(dev_path,filename)

    train_file = open(train_file_path,'w')
    dev_file = open(dev_file_path,'w')
    print(dev_file_path)

    file = open(filename,'r')
    data_lines = sorted(file.readlines()) # sort the lines alphabetically 
    train_file.write(data_lines[1]) # not include the header in the new files
    dev_file.write(data_lines[1])

    for data_line in data_lines:
        line = data_line.rstrip('\n')
        id = line.split('\t')[id_index]
       
        if id in train_ids:
            train_file.write(data_line)
        elif id in dev_ids:
            dev_file.write(data_line)

    train_file.close()
    dev_file.close()
    file.close()

dev_train_data_split(train_ids,dev_ids,'wav.scp',0)
dev_train_data_split(train_ids,dev_ids,'text',0)
dev_train_data_split(train_ids,dev_ids,'utt2spk',0)
#dev_train_data_split(train_ids,dev_ids,'spk2utt',1) 
