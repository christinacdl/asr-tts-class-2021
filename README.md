# asr-tts-class-2021
M907

The task

This is a team project concerning a simple ASR (Automatic Speech Recognition) system for an inclusive smart TV in the Spanish language using Kaldi toolkit. The ASR system was named "Elvina Inclusive Smart TV" as it is focused on people with Down Syndrome.  It includes power commands (turn on/turn off TV), navigation TV commands and navigation in 13 Spanish TV channels (e.g., "Telecinco", "Canal Sur Andalucía") as well as increase/decrease of TV volume. 

In the folder "elvina_tv":

We wrote a python program called "create_specific_lexicon_final.py" to create a simple grammar ("elvina_grammar_new.txt") containing Spanish words in capital letters that refer to digits, verbs, confirmation, negation, channel names and the order of these commands. The system would be activated by using the trigger word "Elvina". From this grammar, a wordlist was created in small("elvina_wordlist_small_letters.txt") and capital letters("elvina_wordlist_capital.txt"). The wordlist in capital letters was used to map the corresponding phonemes to each word based on the Voxforge Spanish Dictionary. We attempted to use the tool phonemize to collect the pronunciations for each word, yet the results were not sufficient. That's why, we created the pronunciations manually based on the Spanish Voxforge. We then used HParse and the grammar to create a wordnet ("wdnet.txt"). A "new_lexicon_capital" was also made, which was used combined with the wordnet and HSGen to generate 100 random utterances in Spanish. The utterances were delivered by 7 speakers. The speakers recorded the utterances using Audacity, 1(mono) recording channel, 16000HZ, wav format. 7 sub-folders were created for each speaker containing the wav sound files and their prompts ("PROMPTS.txt"). The name of the wav files resembles the name of the sound files in Voxforge Spanish (e.g "es-001.wav").

In the directory "elvina_recipe/s5/local":

For the training and validation part, we wrote 2 python programs ("process1.py","dev_train_split.py") that derived the information from all the prompts of the "/other/data/voxforge_spanish" and created 4 files, the wav.scp, the text, the utt2spk and the spk2utt for training and development/validation respectively. We included these python programs into spanish_data_prep.sh for data validation, but we encountered many difficulties regarding the form of the utt2spk files as they needed to be sorted. 
