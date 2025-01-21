# HistoryX - Twitter History Analyzer

🚧 **Work in Progress** 🚧

This tool analyzes a Twitter/X user's history (tweets, likes, and replies) to identify potentially concerning content using sentiment analysis and content filtering.

## Current Status

### What Works
- ✅ Twitter data collection (tweets, replies, and likes from the past 5 years)
- ✅ CSV export of collected data
- ✅ Basic rate limit handling

### Under Development
- 🔄 Analysis features for identifying explicit, immoral, or unethical behavior
- 🔄 Enhanced rate limit handling for better data collection
- 🔄 Data visualization and reporting

## Setup

1. Clone the repository:
```bash
git clone https://github.com/lame-o/HistoryX.git
cd HistoryX
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your Twitter API credentials:
```
TWITTER_BEARER_TOKEN=your_bearer_token_here
TWITTER_API_KEY=your_api_key_here
TWITTER_API_SECRET=your_api_secret_here
TWITTER_ACCESS_TOKEN=your_access_token_here
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret_here
```

## Usage

```bash
python twitter_analyzer.py
```

When prompted, enter a Twitter username (without @) to analyze.

## Known Limitations

1. **Rate Limiting**: The script is currently affected by Twitter API rate limits. If you hit the rate limit:
   - The script will stop collecting data
   - You'll need to wait until your rate limit resets (usually monthly)
   - Future versions will implement better rate limit handling and data persistence

2. **Analysis Features**: The analysis component is still under development. Currently, the script only collects and stores data without performing any analysis.

## Next Steps

1. Implement analysis features for:
   - Content classification
   - Pattern recognition
   - Behavioral analysis

2. Add data persistence to handle rate limits better:
   - Save partial progress
   - Resume from last successful point
   - Merge multiple collection sessions

3. Create visualization and reporting features:
   - Timeline views
   - Content summaries
   - Analysis reports

## Contributing

This project is in active development. Feel free to open issues or submit pull requests!

## Note

This tool respects Twitter's API rate limits and terms of service. Make sure you have appropriate authorization before analyzing any user's content.
