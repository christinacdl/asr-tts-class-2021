# Read tsv files
import pandas as pd 
import sys 

# NEEDS MODIFICATION 
# local/process_tsv_file.py $part $wav_scp $trans $uut2spk
part_file = sys.arg[1]
audio_data_dir = sys.arg[2]
wav_acp_file = sys.arg[3]
trans_file = sys.arg[4]
uut2spk_file = sys.arg[5]

df = pd.read_csv(part_file, delimiter = '\t')
#audio_data_dir = 

# strip the .wav format in the end to keep the id of the sound file
df['id'] = df['path'].str.replace('.wav','') 

#----- Create wav.scp file -----
# get the path
df['abs_path'] = audio_data_dir + '/' + df['path']

# write to wav_acp_file.csv
df[['id','abs_path']].to_csv(wav_acp_file, sep = '', index = False)

#----- Create trans_file -----

# we want to remove punctuations
df['sentence'] = df['sentence'].str.replace('[^\w\s','')

# get id and sentence side by side and write to trans_file.csv
df[['id','sentence']].to_csv(trans_file, sep = '\t', index = False)

#----- Create uut2spk -----
df[['id','client_id']].to_csv(uut2spk_file, sep = '\t', index = False)



