#!/usr/bin/env bash

# Change this location to somewhere where you want to put the data.
data=./corpus/

data_url=www.openslr.org/resources/31
lm_url=www.openslr.org/resources/11

. ./cmd.sh
. ./path.sh

stage=0
. utils/parse_options.sh

set -euo pipefail

mkdir -p $data

if [ $stage -le 2 ]; then
  mfccdir=mfcc
  # spread the mfccs over various machines, as this data-set is quite large.
  if [[  $(hostname -f) ==  *.clsp.jhu.edu ]]; then
    mfcc=$(basename mfccdir) # in case was absolute pathname (unlikely), get basename.
    utils/create_split_dir.pl /export/b{07,14,16,17}/$USER/kaldi-data/egs/librispeech/s5/$mfcc/storage \
      $mfccdir/storage
  fi

  for part in dev_teamlab; do
    steps/make_mfcc.sh --cmd "$train_cmd" --nj 1 data/$part exp/make_mfcc/$part $mfccdir
    steps/compute_cmvn_stats.sh data/$part exp/make_mfcc/$part $mfccdir
  done
fi

if [ $stage -le 8 ]; then
  # Test the tri3b system with the silprobs and pron-probs.

  # decode using the tri3b model
  for test in dev_teamlab; do
    steps/decode_fmllr.sh --nj 1 --cmd "$decode_cmd" \
                          exp/tri3b/graph_tgsmall data/$test \
                          exp/tri3b/decode_tgsmall_$test
  done
fi
echo Done; exit
# Train a chain model
if [ $stage -le 9 ]; then
  local/chain2/run_tdnn.sh
fi

# local/grammar/simple_demo.sh
