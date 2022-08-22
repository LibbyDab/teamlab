#!/usr/bin/env bash

# Change this location to somewhere where you want to put the data.
data=./corpus/

data_url=www.openslr.org/resources/31
lm_url=www.openslr.org/resources/11

. ./cmd.sh
. ./path.sh

stage=2
. utils/parse_options.sh

set -euo pipefail

mkdir -p $data

if [ $stage -le 1 ]; then
  utils/fix_data_dir.sh data/train_teamlab

  utils/fix_data_dir.sh data/dev_teamlab
fi

if [ $stage -le 2 ]; then
  mfccdir=mfcc
  for part in dev_teamlab train_teamlab; do
    steps/make_mfcc.sh --cmd "$train_cmd" --nj 1 data/$part exp/make_mfcc/$part $mfccdir
    steps/compute_cmvn_stats.sh data/$part exp/make_mfcc/$part $mfccdir
  done
fi

if [ $stage -le 8 ]; then
  # Test the tri3b system with the silprobs and pron-probs.

  # decode using the tri3b model
  utils/mkgraph.sh data/lang_test_tgsmall \
                   exp/tri3b exp/tri3b/graph_tgsmall

  # decode using the tri3b model
  for test in dev_teamlab; do
    steps/decode_fmllr.sh --nj 1 --cmd "$decode_cmd" \
                          exp/tri3b/graph_tgsmall data/$test \
                          exp/tri3b/decode_tgsmall_$test
  done
fi
echo Done; exit
