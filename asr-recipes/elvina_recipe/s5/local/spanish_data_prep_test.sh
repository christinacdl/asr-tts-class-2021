#!/usr/bin/env bash

# Copyright 2021 NLP chicas 
# Apache 2.0
# For the test data


PYTHONIOENCODING=UTF-8 python3 process1.py
PYTHONIOENCODING=UTF-8 python3 dev_train_split.py 

src_data=../utils
test_dir=data/test


# create destination directory, else exit
mkdir -p $test_dir || exit 1;


# if source directory doesn't exist pop error
[ ! -d $test_dir ] && echo "$0: no such directory $test_dir" && exit 1;


# Data validation
trans_test=$test_dir/text
utt2spk_test=$test_dir/utt2spk
spk2utt_test=$test_dir/spk2utt

$src_data/utt2spk_to_spk2utt.pl <$utt2spk_test >$spk2utt_test || exit 1


# For the test data
ntrans_test=$(wc -l <$trans_test)
utt2spk_test=$(wc -l <$utt2spk_test)
! [ "$ntrans_test" -eq "$utt2spk_test" ] && \
  echo "Inconsistent #transcripts($ntrans_test) and #utt2spk($utt2spk_test)" && exit 1;

$src_data/validate_data_dir.sh --no-feats $test_dir || exit 1;

echo "$0: successfully prepared data in $test_dir"
