#!/usr/bin/env python

# Adapted from AI Spectrum
# Author: Taiwo Owoseni
# date: 2022-05-14

"""Downloads xls data from the web to a local filepath as csv file.
Usage: src/scrape_tweet.py --out_file=<out_file>

Options:
--out_file=<out_file>    Path (including filename) of where to locally write the file
"""

from docopt import docopt
import snscrape.modules.twitter as sntwitter
import pandas as pd
import datetime as dt

opt = docopt(__doc__)

tweets = []
limit = 50000
today_date = dt.date.today().strftime("%Y-%m-%d")
query_list = [
    (f"(TheCircle (#TheCircle) lang:en  since:2022-05-01 until:{today_date})"),
    (f"(theCircle (#TheCircleNetflix) lang:en  since:2022-05-01 until:{today_date})"),
    (f"(TheCircle (#TheCircleNetflix) lang:en  since:2022-05-01 until:{today_date})"),
    (f"(thecircle (#TheCircle) lang:en  since:2022-05-01 until:{today_date})"),
    (f"(the circle (#TheCircle) lang:en  since:2022-05-01 until:{today_date})"),
    (f"(the circle (#TheCircleNetflix) lang:en  since:2022-05-01 until:{today_date})"),
    (f"(The circle (#TheCircleNetflix) lang:en  since:2022-05-01 until:{today_date})"),
    (f"(The circle (#CircleFam) lang:en  since:2022-05-01 until:{today_date})"),
    (f"(TheCircle (#TheCircleUSA) lang:en  since:2022-05-01 until:{today_date})"),
]


def main(out_file):

    for query in query_list:
        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            if len(tweets) > limit:
                break
            else:
                tweets.append([tweet.date, tweet.user.username, tweet.content])

    df = pd.DataFrame(tweets, columns=["Date", "User", "Tweet"])

    # to save to csv
    df.to_csv(f"{out_file}.csv")


if __name__ == "__main__":
    main(opt["--out_file"])
