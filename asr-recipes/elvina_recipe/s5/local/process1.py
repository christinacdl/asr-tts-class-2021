#!/usr/bin/env python3
import sys
import os
import csv
import scipy.io.wavfile
import re
import glob
import numpy as np


r_dir = '/other/data/voxforge_spanish/audio/*/wav'

output_file = open('elvina_voxforge_train.tsv','w') # the general tsv file
output_file.write('id\tspeaker_id\twav_path\tutterance\n')

wav_scp_file = open('wav.scp','w') # the wav.scp
wav_scp_file.write('id\twav_path\n')

text_file = open('text','w') # the text
text_file.write('id\tutterance\n')

utt2spk_file = open('utt2spk','w') # the uut2spk
utt2spk_file.write('id\tspeaker_id\n')

spk2utt_file = open('spk2utt','w') # the spk2utt
spk2utt_file.write('speaker_id\tid\n')



index = 1

for files in glob.glob(r_dir,recursive=True):
    
    for root, sub, files in os.walk(files):        
        files = sorted(files)
        prompts_path = os.path.join(root, '../etc/PROMPTS')
        read_prompts = open(prompts_path, 'r')
        
        for wav_path in files:
            
            prompts_file_data = read_prompts.readline() # read each line of the PROMPTS file
            
            speaker_id =  prompts_file_data.split('/')[0] # get the speaker id (first part)
            utterance = prompts_file_data.split(' ',1)[1].rstrip("\n") # get the utterance (second part)
            row =  f"{index}\t{speaker_id}\t{wav_path}\t{utterance}\n" # create headers id,speaker_id,wav_path,utterance
            output_file.write(row)

            create_wav_scp = f"{index}\t{wav_path}\n" # create the wav.scp 1
            wav_scp_file.write(create_wav_scp) 

            create_text = f"{index}\t{utterance}\n" # create the text 2
            text_file.write(create_text)

            create_uut2spk = f"{index}\t{speaker_id}\n" # create the uut2speak 3
            utt2spk_file.write(create_uut2spk)

            create_spk2utt = f"{speaker_id}\t{index}\n" # create the spk2uut 4 
            spk2utt_file.write(create_spk2utt) 

            index += 1

        read_prompts.close()

output_file.close()
wav_scp_file.close()
text_file.close()
utt2spk_file.close()
spk2utt_file.close()
