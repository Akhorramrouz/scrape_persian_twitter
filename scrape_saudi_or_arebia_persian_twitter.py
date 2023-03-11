# pip install snscrape

import snscrape.modules.twitter as sntwitter
import pandas as pd


tweets = []
c = 0

query = f'(عربستان OR سعودی) lang:fa since:2013-01-01 -filter:links'
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    tweets.append({'date' : tweet.date,
    'text' : tweet.rawContent,
    'Id' : tweet.id,
    'hashtags' : tweet.hashtags,
    'mentionedUsers' : tweet.mentionedUsers,
    'sourceLabel' : tweet.sourceLabel,
    'sourceUrl' : tweet.sourceUrl,
    'lang' : tweet.lang,
    'likeCount' : tweet.likeCount,
    'retweetCount' : tweet.retweetCount,
    'replyCount' : tweet.replyCount,
    'Username' : tweet.user.username,
    "User_id" : tweet.user.id,
    'User_description' : tweet.user.renderedDescription,
    "User_created" : tweet.user.created,
    "UserfollowersCount" : tweet.user.followersCount,
    "Userlocation" : tweet.user.location,
    'UserprofileBannerUrl' : tweet.user.profileBannerUrl,
    "UserprofileBannerUrl" : tweet.user.profileBannerUrl,
    "USermediaCount" : tweet.user.mediaCount,
    "UserfollowingCount" : tweet.user.friendsCount})
    c += 1
    if c%10000 == 9999:
        print(c)
        print(tweet.date)
        df = pd.DataFrame(tweets)
        df.to_csv(f"saudi_or_arebia_persian_twitter_index_{c}.csv")
        tweets = []
    


df = pd.DataFrame(tweets)
df.to_csv(f"saudi_or_arebia_persian_twitter_index_{c}_last.csv")