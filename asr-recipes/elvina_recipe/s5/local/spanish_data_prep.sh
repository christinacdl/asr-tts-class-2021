#!/usr/bin/env bash

# Copyright 2021 NLP chicas 
# Apache 2.0
# For the train/development data


PYTHONIOENCODING=UTF-8 python3 process1.py
PYTHONIOENCODING=UTF-8 python3 dev_train_split.py 

src_data=../utils
dev_dir=data/dev
train_dir=data/train

# create destination directory, else exit
mkdir -p $dev_dir || exit 1;
mkdir -p $train_dir || exit 1;

# if source directory doesn't exist pop error
[ ! -d $dev_dir ] && echo "$0: no such directory $dev_dir" && exit 1;
[ ! -d $train_dir ] && echo "$0: no such directory $train_dir" && exit 1;

# Data validation
trans_dev=$dev_dir/text
trans_train=$train_dir/text
spk2utt_dev=$dev_dir/spk2utt
utt2spk_dev=$dev_dir/utt2spk
spk2utt_train=$train_dir/spk2utt
utt2spk_train=$train_dir/utt2spk

$src_data/utt2spk_to_spk2utt.pl <$utt2spk_dev >$spk2utt_dev || exit 1
$src_data/utt2spk_to_spk2utt.pl <$utt2spk_train >$spk2utt_train || exit 1


# For the dev set
ntrans_dev=$(wc -l <$trans_dev)
nutt2spk_dev=$(wc -l <$utt2spk_dev)
! [ "$ntrans_dev" -eq "$nutt2spk_dev" ] && \
  echo ["Inconsistent #transcripts($ntrans_dev) and #utt2spk($nutt2spk_dev)"] && exit 1;

$src_data/validate_data_dir.sh --no-feats $dev_dir || exit 1;

echo "$0: successfully prepared data in $dev_dir"



# For the train set
ntrans_train=$(wc -l <$trans_train)
nutt2spk_train=$(wc -l <$utt2spk_train)
! [ "$ntrans_train" -eq "$nutt2spk_train" ] && \
  echo "Inconsistent #transcripts($ntrans_train) and #utt2spk($nutt2spk_train)" && exit 1;

$src_data/validate_data_dir.sh --no-feats $train_dir || exit 1;

echo "$0: successfully prepared data in $train_dir"

exit 0
