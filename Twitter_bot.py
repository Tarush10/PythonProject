import tweepy

#Get all the API keys/tokens by creating an App in the twitter developer accounts
token = "<Replace with TOKEN>"
api_Key = '<Replace with API-KEY>'
api_secret = '<Replace with API-SECRET>'
access_token = '<Replace with ACCESS-TOKEN>'
access_token_secret = '<REplace with ACCESS-TOKEN-SECRET>'

client = tweepy.Client(token, api_Key, api_secret, access_token, access_token_secret)
results = []
tweet_ids = []
followers_list = []
following_list = []


# Getting users own user_id
def get_my_id():
    print(client.get_me().data['name'])


# Getting the homepage of my Twitter
def get_homepage():
    public_tweets = client.get_home_timeline()
    print(public_tweets)


# Get followers of any user
def get_follower(user_id):
    follower = client.get_users_followers(user_id)
    for followers in follower.data:
        print(followers)

def get_following(user_id):
    following = client.get_users_following(user_id)
    for followings in following.data:
        print(followings)

# Get tweets having a particular string
def tweet_search(search_string):
    tweet = client.search_recent_tweets(search_string)
    tweet_data = tweet.data
    if not tweet_data is None and len(tweet_data) > 0:
        for tweet in tweet_data:
            obj = {'id': tweet.id, 'text': tweet.text}
            results.append(obj)
    print(results)

# Use after the get_follower/get_following function
def get_data(param):
    for i in results:
        ids = i[param]
        tweet_ids.append(ids)
    print(tweet_ids)