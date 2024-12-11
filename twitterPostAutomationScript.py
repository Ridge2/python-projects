import os
import time
import tweepy
import requests
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Twitter API credentials
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
#TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# NewsAPI key
NEWSAPI_KEY = os.getenv('NEWSAPI_KEY')

# Initialize Tweepy client
auth = tweepy.OAuth1UserHandler(
    TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, #TWITTER_ACCESS_TOKEN_SECRET
)
twitter_client = tweepy.API(auth)

# Function to fetch top headlines from NewsAPI
def get_top_headlines():
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWSAPI_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('articles', [])
    else:
        print(f"Error fetching news: {response.status_code}")
        return []

# Function to post a tweet
def post_tweet(content):
    try:
        twitter_client.update_status(content)
        print("Tweet posted successfully!")
    except Exception as e:
        print(f"Error posting tweet: {e}")

# Main function to fetch news and post to Twitter
def main():
    posted_urls = set()  # Track URLs already posted to avoid duplicates

    for _ in range(3):  # Run 3 times a day
        articles = get_top_headlines()
        if not articles:
            print("No articles found.")
            time.sleep(86400 / 3)  # Sleep to wait for next post
            continue

        for article in articles:
            title = article.get('title')
            url = article.get('url')
            if url not in posted_urls:
                tweet = f"{title} \nRead more: {url}"
                post_tweet(tweet)
                posted_urls.add(url)
                break

        time.sleep(86400 / 3)  # Sleep to ensure 3 tweets in a day

if __name__ == "__main__":
    main()
