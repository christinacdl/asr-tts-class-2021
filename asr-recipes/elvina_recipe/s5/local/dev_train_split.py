#!/usr/bin/env python3
import pandas as pd
import os
from sklearn.model_selection import train_test_split

# For the train set
train_path  = "/other/users/chrichr/asr-tts-class-2021/asr-recipes/elvina_recipe/s5/data/train"
# For the dev set
dev_path = "/other/users/chrichr/asr-tts-class-2021/asr-recipes/elvina_recipe/s5/data/dev" 

df = pd.read_csv('/other/users/chrichr/asr-tts-class-2021/asr-recipes/elvina_recipe/s5/local/elvina_voxforge_train.tsv', delimiter = '\t')
train_data, dev_data = train_test_split(df, test_size = 0.20, random_state = 5)

train_data_filepath = os.path.join(train_path,'train.tsv')
dev_data_filepath = os.path.join(dev_path,'dev.tsv')

train_data.to_csv(train_data_filepath,sep='\t', index = False)
dev_data.to_csv(dev_data_filepath,sep='\t', index = False) 

train_ids = set(train_data['id'].astype(str))
dev_ids = set(dev_data['id'].astype(str))


def dev_train_data_split(train_ids,dev_ids,filename,id_index):

    train_file_path = os.path.join(train_path,filename)
    dev_file_path = os.path.join(dev_path,filename)

    train_file = open(train_file_path,'w')
    dev_file = open(dev_file_path,'w')

    file = open(filename,'r')
    data_lines = file.readlines()
    train_file.write(data_lines[0]) # include the header in the new files
    dev_file.write(data_lines[0])

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
dev_train_data_split(train_ids,dev_ids,'spk2utt',1)
