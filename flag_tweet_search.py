import os
import sys
import config
from time import sleep
from requests_oauthlib import OAuth1Session
import configparser
import json

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

CONSUMER_KEY = config_ini['DEFAULT']['TW_CONSUMER_KEY']
CONSUMER_SECRET = config_ini['DEFAULT']['TW_CONSUMER_SECRET']
ACCESS_TOKEN = config_ini['DEFAULT']['TW_ACCESS_TOKEN']
ACCESS_SECRET = config_ini['DEFAULT']['TW_ACCESS_SECRET']

twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)


url = "https://api.twitter.com/1.1/tweets/search/fullarchive/flag.json"

#paramsに検索ワードや件数、日付などを入力
params = {"query":"@flag__chan 今日の動画は", "maxResults":100}

#上記で設定したパラメーターをget関数を使い指定URLから取得
res = twitter.get(url, params = params)

#ステータスコードが正常値（200）だった場合の処理
if res.status_code == 200:

    #後でpandasで処理するためリスト化
    created_at = []
    text = []
    retweet_count = []
    favorite_count = []
    
    name = []
    followers_count = []
    friends_count = []
    statuses_count = []    

    #100件を超えるデータ用に繰り返し処理で対応
    while True:
        res = twitter.get(url, params = params)
        tweets = json.loads(res.text)
        tweet_list = tweets["results"]
        
        for tweet in tweet_list:
            #created_at.append(tweet["created_at"]) #投稿日時
            #text.append(tweet["text"]) #投稿本文
            #retweet_count.append(tweet["retweet_count"]) #リツイート数
            #favorite_count.append(tweet["favorite_count"]) #いいね数
            #user = tweet["user"]
            #name.append(user["name"]) #名前
            #followers_count.append(user["followers_count"]) #フォロワー数
            #friends_count.append(user["friends_count"]) #フォロー数
            #statuses_count.append(user["statuses_count"]) #投稿数
            result_json = json.dumps(tweet, ensure_ascii=False)
            print(result_json)

        #対象Tweetが101件以上となりnextページがある場合
        if "next"  in tweets.keys():
           #nextの値をパラメータに追加する
            params['next'] =  tweets["next"]
            #print(params)
            tweet_list = tweets["results"]
        
        #nextページがない場合（100件以内の場合と最終ページ用）
        else:
            #print("最終ページなので取得終了")
            break 
            
else:
    print("ERROR: %d" % res.status_code)
