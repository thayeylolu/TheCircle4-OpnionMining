import string
import emoji

import pandas as pd
import numpy as np
import json

from collections import Counter

# from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re, string, unicodedata

import nltk
from nltk import word_tokenize, sent_tokenize, FreqDist
from nltk.corpus import stopwords


ps = nltk.PorterStemmer()
w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()

nltk.download
nltk.download("wordnet")
nltk.download("stopwords")
nltk.download("omw-1.4")
from nltk.tokenize import TweetTokenizer

stop_words = set(stopwords.words("english"))


player_info = pd.read_csv("players_info.csv")
tweets_data = pd.read_csv("tweet_combo_all.csv")
tweets_data = tweets_data.sample(10)

player_set = {
    "playeron",
    "playertwo",
    "playerthre",
    "playerfour",
    "playerf",
    "playersix",
    "playrseven",
    "playereight",
    "playernin",
    "playerten",
    "playereleven",
    "playertwelv",
}


def main():

    player_dict = dict(zip(list(player_info.player), list(player_info.playerno)))
    player_list = list(player_info.player)
    plural_player = [player + "s" for player in player_list]
    plural_player_dict = dict(zip(plural_player, list(player_info.playerno)))

    tweets_data = tweets_data.rename(columns=str.lower)
    tweets = tweets_data["tweet"]

    def clean_text(text):
        text_lc = "".join(
            [word.lower() for word in text if word not in string.punctuation]
        )  # remove puntuation
        text_rc = re.sub("[0-9]+", "", text_lc)
        tokens = re.split("\W+", text_rc)  # tokenization
        text = [(lemmatizer.lemmatize(w)) for w in w_tokenizer.tokenize((text))]
        text = [
            ps.stem(word) for word in tokens if word not in stop_words
        ]  # remove stopwords
        # text  = [lemmatizer.lemmatize(w) for w in w_tokenizer.tokenize(text)] #lemmatize
        return text

    def preprocessing_text(text):
        # Make lowercase
        text = text.str.lower().str.replace("\n", " ")
        text = text.str.lower().str.replace("john/carol", "playerfour")
        text = text.str.lower().str.replace("john", "playerfour")
        text = text.str.lower().str.replace("emerson", "playerelven")
        text = text.str.lower().str.replace("rachel", "playernine")
        text = text.str.lower().str.replace("wu", "playertwo")
        text = text.str.lower().str.replace("yu", "playertwo")
        text = text.str.lower().str.replace("yin", "playertwo")
        text = text.str.lower().str.replace("carissa", "playerthre")
        text = text.str.lower().str.replace("trevor", "playertwelve")
        text = text.str.lower().str.replace("spice", "playereight")
        text = text.str.lower().str.replace("girl", "playereight")
        text = text.str.lower().str.replace("mel", "playereight")
        text = text.str.lower().str.replace("emma", "playereight")
        text = text.str.lower().str.replace("mel b", "playereight")
        text = text.str.lower().str.replace("melb", "playereight")
        text = text.str.lower().str.replace("alex", "playerten")

        return text

    def plural_replace_names(text):
        for key, value in plural_player_dict.items():
            text = text.lower().replace(key.lower(), value)
        return text

    def singular_replace_names(text):
        for key, value in player_dict.items():
            text = text.lower().replace(key.lower(), value)
        return text

    def extract_emojis(s):
        return "".join(c for c in s if c in emoji.UNICODE_EMOJI["en"])

    tweets_data["hashtag"] = tweets.apply(lambda x: re.findall(r"#(\w+)", x))
    tweets_data["hashtag"] = tweets.apply(lambda x: re.findall(r"#(\w+)", x))
    tweets_data["mention"] = tweets.apply(lambda x: re.findall(r"@(\w+)", x))
    tweets_data["emojis"] = tweets.apply(lambda x: extract_emojis(x))

    clean_tweet = tweets.str.encode("ascii", "ignore").str.decode("ascii")
    clean_tweet = preprocessing_text(clean_tweet)
    clean_tweet = clean_tweet.apply(lambda x: re.sub("[0-9]+", " ", x))
    clean_tweet = clean_tweet.apply(lambda x: re.sub("@[A-Za-z0-9_].", " user ", x))

    clean_tweet = clean_tweet.apply(lambda x: re.sub("#[A-Za-z0-9_]+", " ", x))
    clean_tweet = clean_tweet.apply(lambda x: re.sub("http\S+", " link ", x))
    clean_tweet = clean_tweet.apply(lambda x: re.sub("^&[[A-Za-z0-9_]+;$", " ", x))

    clean_tweet = clean_tweet.apply(lambda x: singular_replace_names(x))
    clean_tweet = clean_tweet.apply(lambda x: plural_replace_names(x))
    clean_tweet = clean_tweet.apply(lambda x: clean_text(x))

    clean_tweet = clean_tweet.apply(lambda x: " ".join(x))
    tweets_data["text_emoji"] = +clean_tweet + tweets_data["emojis"]
    tweets_data["text_break"] = clean_tweet.str.split()
    tweets_data["text_break_emoji"] = tweets_data["text_emoji"].str.split()
    tweets_data["player"] = list(
        tweets_data["text_break"].apply(
            lambda x: set(list(x)) & set(player_dict.values())
        )
    )
    tweets_data["clean_tweet"] = clean_tweet

    pass
