#!/usr/bin/env python

# Adapted from AI Spectrum
# Author: Taiwo Owoseni
# date: 2022-05-14

"""Downloads xls data from the web to a local filepath as csv file.
Usage: src/scrape_tweet.py --out_file=<out_file>

Options:
--out_file=<out_file>    path (including filename) to locally write the predicted sentiments
"""

from transformers import pipeline
from scipy.special import softmax
import pandas as pd
import docopt

opt = docopt(__doc__)


def main(out_file):
    classifier = pipeline("sentiment-analysis")
    # classifier.model.name_or_path

    df = pd.read_csv("preprocessed.csv")
    tweet_list = list(df["text_emoji"])

    output = classifier(tweet_list)
    df["sentiments"] = pd.Series([i["label"] for i in output])
    output_cols = df[
        ["sentiments", "players_name", "user", "tweet", "hashtag", "player"]
    ]

    # to save to csv
    output_cols.to_csv(f"{out_file}.csv")
