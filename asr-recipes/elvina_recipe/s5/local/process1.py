#!/usr/bin/env python3
import sys
import os
import csv
import scipy.io.wavfile
import re
import glob
import numpy as np


r_dir = '/data/voxforge_spanish/audio/*/wav' 
pr_path = '../etc/PROMPTS' 


output_file = open('elvina_voxforge_train.tsv','w') # the general tsv file
output_file.write('utterance_id\tspeaker_id\twav_path\tutterance\n')

wav_scp_file = open('wav.scp','w') # the wav.scp
wav_scp_file.write('utterance_id\twav_path\n')

text_file = open('text','w') # the text
text_file.write('utterance_id\tutterance\n')

utt2spk_file = open('utt2spk','w') # the uut2spk
utt2spk_file.write('utterance_id\tspeaker_id\n')

#spk2utt_file = open('spk2utt','w') # the spk2utt
#spk2utt_file.write('speaker_id\tutterance_id\n')



index = 1

for files in glob.glob(r_dir,recursive=True):
    
    for root, sub, files in os.walk(files):        
        files = sorted(files)
        prompts_path = os.path.join(root, pr_path)
        read_prompts = open(prompts_path, 'r')
        
        for wav_path in files:
            
            prompts_file_data = read_prompts.readline() # read each line of the PROMPTS file
            
            utterance_id =  prompts_file_data.split('/')[0] + '-' + wav_path.split('.wav')[0] # speaker's id as prefix with wav id
            
            speaker_id =  prompts_file_data.split('/')[0] # get the speaker id (first part)
            utterance = prompts_file_data.split(' ',1)[1].rstrip("\n") # get the utterance (second part)
            
            row =  "{}\t{}\t{}\t{}\n".format(utterance_id,speaker_id,wav_path,utterance) # create headers id,speaker_id,wav_path,utterance        
            output_file.write(row)

            create_wav_scp = "{}\t{}\n".format(utterance_id,wav_path) # create the wav.scp 1          
            wav_scp_file.write(create_wav_scp) 

            create_text = "{}\t{}\n".format(utterance_id,utterance) # create the text 2          
            text_file.write(create_text)
            
            create_uut2spk = "{}\t{}\n".format(utterance_id,speaker_id) # create the uut2spk 3
            utt2spk_file.write(create_uut2spk)

            #create_spk2utt = "{}\t{}\n".format(speaker_id,utterance_id) # create the spk2uut 4
            #spk2utt_file.write(create_spk2utt) 

            index += 1

        read_prompts.close()

output_file.close()
wav_scp_file.close()
text_file.close()
utt2spk_file.close()
#spk2utt_file.close()
