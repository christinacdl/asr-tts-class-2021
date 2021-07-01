# asr-tts-class-2021
M907

This is a team project concerning a simple ASR (Automatic Speech Recognition) system for an inclusive smart TV in the Spanish language using Kaldi toolkit. The ASR system was named "Elvina Inclusive Smart TV" as it is focused on people with Down Syndrome.  It includes navigation TV commands and Navigation in 13 Spanish TV channels (e.g., "Telecinco", "Canal Sur Andalucía") as well as increase/decrease of TV volume. 

In the folder "elvina_tv":

We created a simple grammar ("elvina_grammar_new.txt") containing Spanish words in capital letters that refer to digits, verbs, confirmation, negation, channel names and the order of these commands. The system would be activated by using the word "Elvina".  From this grammar, a wordlist was created in capital letters, which was used to map the corresponding phonemes to each word based on the Voxforge Spanish Dictionary.  We used HParse and the grammar to create a wordnet ("wdnet.txt"). A "new_lexicon_capital" was also made, which was used combined with the wordnet and HSGen to generate 100 random utterances in Spanish. The utterances were delivered by 5 speakers. 

In the directory "elvina_recipe/s5/local":

For the training and validation part, we wrote 2 python programs ("process1.py","dev_train_split.py") that derived the information from all the prompts of the "/other/data/voxforge_spanish" and created 4 files, the wav.scp, the text, the utt2spk and the spk2utt for training and development/validation respectively. 
