# asr-tts-class-2021
M907

Team members:
Vaia Adamopoulou (vaiaada)
Elli Kafritsa (ellikaf)
Christina Christodoulou (chrichr)

1. Speech Recognition System

a) The task

This is a team project concerning a simple ASR (Automatic Speech Recognition) system for an inclusive smart TV in the Spanish language using Kaldi toolkit. The ASR system was named "Elvina Inclusive Smart TV" as it is focused on people with Down Syndrome.  It includes power commands (turn on/turn off TV), navigation TV commands and navigation in 13 Spanish TV channels (e.g., "Telecinco", "Canal Sur Andalucía") as well as increase/decrease of TV volume. 

b) The process to collect the data and customize the system

In the directory "asr-recipes/elvina_tv":

We wrote a python program called "create_specific_lexicon_final.py" to create a simple grammar ("elvina_grammar_new.txt") containing Spanish words in capital letters that refer to digits, verbs, confirmation, negation, channel names and the order of these commands. The system would be activated by using the trigger word "Elvina". From this grammar, a wordlist was created in small("elvina_wordlist_small_letters.txt") and capital letters("elvina_wordlist_capital.txt"). The wordlist in capital letters was used to map the corresponding phonemes to each word based on the Voxforge Spanish Dictionary. We attempted to use the tool phonemize to collect the pronunciations for each word, yet the results were not sufficient. That's why, we created the pronunciations manually based on the Spanish Voxforge. We then used HParse and the grammar to create a wordnet ("wdnet.txt"). A "new_lexicon_capital" was also made, which was used combined with the wordnet and HSGen to generate 100 random utterances in Spanish. The utterances were delivered by 7 speakers. The speakers recorded the utterances using Audacity, 1(mono) recording channel, 16000HZ, wav format. 7 sub-folders were created for each speaker containing the wav sound files and their prompts ("PROMPTS.txt"). The names of the audio files resemble the names of the sound files in Voxforge Spanish (e.g "es-001.wav"). The test audio files are located in other/users/asr-recipes/elvina_tv/elvina_all_speakers

In the directory "asr-recipes/elvina_recipe/s5/local":

For the training and validation part, we wrote 2 python programs ("process1.py","dev_train_split.py") that derived the information from all the prompts of the "/other/data/voxforge_spanish" and created a general tsv file with the columns "utterance_id", "speaker_id", "wav_path", "utterance" as well as the 4 files based on the information from the tsv, the wav.scp, the text, the utt2spk and the spk2utt. The "utterance_id" was made using the unique speaker's id combined with the wav's id. We included these python programs into spanish_data_prep.sh to create the 4 files, the wav.scp, the text, the utt2spk and the spk2utt for training and development/validation respectively in the folders "data/train" and "data/dev". Unfortunately, we encountered many difficulties editing the spanish_data_prep.sh as many errors came up concerning the way the 4 files were written, for example the form of the utt2spk files needed sorting. Although we had already sorted the files in ascending order, another kind of sorting needed to be applied by using the utils/fix_data_dir.sh. 

2) Text to Speech Synthesis

a) We generated 5 project-related phrases in English using the merlin_tts engine and the slt_arctic recipe. We ran the "demo voice" and the "full_voice". 

b) The phrases synthesized in English resemble the commands used for the "Elvina Inclusive Smart TV":
elvina turn on and put nova channel
elvina switch to antena three channel
elvina increase the volume and go to the next channel
elvina decrease the volume
elvina decrease the volume and turn off

For the DEMO:
The 5 English sentences are located in other/users/tts-recipes/egs/slt_arctic/s1/experiments/slt_arctic_demo/test_synthesis/txt
The generated audio files are located in other/users/tts-recipes/egs/slt_arctic/s1/experiments/slt_arctic_demo/test_synthesis/wav 

For the Full Voice:
The 5 English sentences are located in other/users/tts-recipes/egs/slt_arctic/s1/experiments/slt_arctic_full/test_synthesis/txt
The generated audio files are located in other/users/tts-recipes/egs/slt_arctic/s1/experiments/slt_arctic_full/test_synthesis/wav 

c) Evaluation with regard to intelligibility and naturalness:

DEMO VOICE
I. Intelligibility
| Member    | Sentence1 | Sentence2 | Sentence3 | Sentence4 | Sentence5 |
|-----------|-----------|-----------|-----------|-----------|-----------|
| Vaia      | 1         | 1         | 3         | 4         | 4         |
| Elli      | 1         | 2         | 4         | 4         | 5         |
| Christina | 1         | 1         | 3         | 3         | 4         |
												
II. Naturalness 
| Member    | Sentence1 | Sentence2 | Sentence3 | Sentence4 | Sentence5 |
|-----------|-----------|-----------|-----------|-----------|-----------|
| Vaia      | 1         | 1         | 1         | 1         | 2         |
| Elli      | 1         | 1         | 2         | 2         | 3         |
| Christina | 1         | 1         | 2         | 2         | 2         |

Mean Opinion Score for Naturalness:            
Mean Opinion Score for Intelligibility:

FULL VOICE
I. Intelligibility
| Member    | Sentence1 | Sentence2 | Sentence3 | Sentence4 | Sentence5 |
|-----------|-----------|-----------|-----------|-----------|-----------|
| Vaia      | 4         | 5         | 5         | 5         | 5         |
| Elli      | 3         | 4         | 5         | 5         | 5         |
| Christina | 4         | 4         | 5         | 5         | 5         |
												
II. Naturalness 
| Member    | Sentence1 | Sentence2 | Sentence3 | Sentence4 | Sentence5 |
|-----------|-----------|-----------|-----------|-----------|-----------|
| Vaia      | 3         | 3         | 3         | 3         | 4         |
| Elli      | 3         | 3         | 3         | 4         | 4         |
| Christina | 3         | 4         | 4         | 4         | 4         |

Mean Opinion Scores for Naturalness:           
Mean Opinion Score for Intelligibility:
