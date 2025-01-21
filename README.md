# HistoryX - Twitter History Analyzer

This tool analyzes a Twitter/X user's history (tweets, likes, and replies) to identify potentially concerning content using sentiment analysis and content filtering.

## Setup

1. Create a Twitter Developer Account and get your API credentials at https://developer.twitter.com/
2. Create a `.env` file in the project root with your Twitter API credentials:
```
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET=your_api_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
TWITTER_BEARER_TOKEN=your_bearer_token
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the analyzer:
```bash
python twitter_analyzer.py
```

Enter a Twitter username when prompted (without the @ symbol). The tool will:
1. Collect the user's tweets, replies, and likes
2. Analyze the content for concerning patterns
3. Generate a summary report in the console
4. Save a detailed CSV report

## Analysis Features

- Profanity detection
- Sentiment analysis (positive/negative)
- Subjectivity analysis
- Timeline analysis
- Interaction patterns

## Output

The tool generates two types of output:
1. A console summary with key metrics
2. A detailed CSV report with all analyzed content

## Note

This tool respects Twitter's API rate limits and terms of service. Make sure you have appropriate authorization before analyzing any user's content.
