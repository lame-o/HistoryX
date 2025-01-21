import os
import csv
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

class TwitterDataCollector:
    def __init__(self):
        self.bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
        self.headers = {
            'Authorization': f'Bearer {self.bearer_token}'
        }
        self.five_years_ago = datetime.now() - timedelta(days=5*365)
        
    def get_user_id(self, username):
        url = f'https://api.twitter.com/2/users/by/username/{username}'
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise Exception(f"Error finding user {username}: {response.text}")
        data = response.json()
        if 'data' not in data:
            raise Exception(f"User {username} not found")
        return data['data']['id']

    def collect_tweets(self, user_id):
        tweets = []
        url = f'https://api.twitter.com/2/users/{user_id}/tweets'
        params = {
            'max_results': 100,
            'tweet.fields': 'created_at',
            'exclude': 'retweets'
        }
        
        while True:
            response = requests.get(url, headers=self.headers, params=params)
            if response.status_code != 200:
                print(f"Error collecting tweets: {response.text}")
                break
                
            data = response.json()
            if 'data' not in data:
                break
                
            for tweet in data['data']:
                created_at = datetime.strptime(tweet['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
                if created_at < self.five_years_ago:
                    return tweets
                    
                tweets.append({
                    'id': tweet['id'],
                    'text': tweet['text'],
                    'created_at': created_at,
                    'type': 'tweet'
                })
            
            if 'next_token' not in data.get('meta', {}):
                break
            params['pagination_token'] = data['meta']['next_token']
            
        return tweets

    def collect_likes(self, user_id):
        likes = []
        url = f'https://api.twitter.com/2/users/{user_id}/liked_tweets'
        params = {
            'max_results': 100,
            'tweet.fields': 'created_at'
        }
        
        while True:
            response = requests.get(url, headers=self.headers, params=params)
            if response.status_code != 200:
                print(f"Error collecting likes: {response.text}")
                break
                
            data = response.json()
            if 'data' not in data:
                break
                
            for tweet in data['data']:
                created_at = datetime.strptime(tweet['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
                if created_at < self.five_years_ago:
                    return likes
                    
                likes.append({
                    'id': tweet['id'],
                    'text': tweet['text'],
                    'created_at': created_at,
                    'type': 'like'
                })
            
            if 'next_token' not in data.get('meta', {}):
                break
            params['pagination_token'] = data['meta']['next_token']
            
        return likes

    def collect_all_data(self, username):
        user_id = self.get_user_id(username)
        all_data = []
        
        print("Collecting tweets and replies...")
        tweets = self.collect_tweets(user_id)
        all_data.extend(tweets)
        
        print("Collecting likes...")
        likes = self.collect_likes(user_id)
        all_data.extend(likes)

        # Sort all data by date
        all_data.sort(key=lambda x: x['created_at'], reverse=True)
        
        # Save to CSV
        if all_data:
            filename = f"{username}_twitter_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=['id', 'text', 'created_at', 'type'])
                writer.writeheader()
                for item in all_data:
                    item['created_at'] = item['created_at'].strftime('%Y-%m-%d %H:%M:%S')
                    writer.writerow(item)
            print(f"\nSaved {len(all_data)} items to {filename}")
            print(f"- Tweets and replies: {len([x for x in all_data if x['type'] == 'tweet'])}")
            print(f"- Likes: {len([x for x in all_data if x['type'] == 'like'])}")
        else:
            print("No data collected")

def main():
    username = input("Enter Twitter/X username to analyze (without @): ")
    print(f"\nCollecting @{username}'s Twitter history from the past 5 years...")
    
    collector = TwitterDataCollector()
    try:
        collector.collect_all_data(username)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
