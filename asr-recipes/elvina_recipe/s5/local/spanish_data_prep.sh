#!/usr/bin/env bash

# Copyright 2021 NLP chicas
# Apache 2.0

if [ "$#" -ne 3 ]; then
  echo "Usage: $0 <src-dir> <part-info> <dst-dir>"
  echo "e.g.: $0 other/data/voxforge_spanish elvina_voxforge_train.tsv data/train"
  exit 1
fi

#arguments:
src=$1
part=$2
dst=$3

# create destination directory, else exit
mkdir -p $dst || exit 1;

# if source directory doesn't exist pop error
[ ! -d $src ] && echo "$0: no such directory $src" && exit 1;

# if these files exist, delete them and rewrite them
wav_scp=$dst/wav.scp; [[ -f "$wav_scp" ]] && rm $wav_scp
trans=$dst/text; [[ -f "$trans" ]] && rm $trans
utt2spk=$dst/utt2spk; [[ -f "$utt2spk" ]] && rm $utt2spk

# Process tsv files to extract all required information
# create a python file that processes tsv files that
# takes as input the part, the wav_scp (where it is going to store the transcriptions)
# and the utt2spk (where it is going to store the speaker's utterance)
PYTHONIOENCODING=UTF-8 python3 local/process1.py  $part $src/clips $wav_scp $trans $utt2spk
python3 local/dev_train_split.py 

spk2utt=$dst/spk2utt
utils/utt2spk_to_spk2utt.pl <$utt2spk >$spk2utt || exit 1


# Data validation
ntrans=$(wc -l <$trans)
nutt2spk=$(wc -l <$utt2spk)

! [ "$ntrans" -eq "$nutt2spk" ] && \
echo "Inconsistent #transcripts($ntrans) and #utt2spk($nutt2spk)" && exit 1;

utils/validate_data_dir.sh --no-feats $dst || exit 1;

echo "$0: successfully prepared data in $dst"

exit 0