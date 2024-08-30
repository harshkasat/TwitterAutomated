# Automated Twitter Bot with LLM Content Generation

This project implements an automated Twitter bot that generates and posts content using a Language Model (LLM) and the Twitter API. The bot runs on a schedule using GitHub Actions and stores tweet data in CSV files.

## Features

- Automated content generation using an LLM
- Scheduled posting using GitHub Actions
- Twitter API integration for posting tweets
- Data storage of posted tweets in `save_tweet.csv`
- Topic-specific content generation based on `tools-specific_task.csv`

## Setup

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up Twitter API credentials:
   - Create a Twitter Developer account and obtain API keys
   - Add the following secrets to your GitHub repository:
     - `TWITTER_API_KEY`
     - `TWITTER_API_SECRET`
     - `TWITTER_ACCESS_TOKEN`
     - `TWITTER_ACCESS_TOKEN_SECRET`

4. Configure your LLM:
   - [Add instructions for setting up the specific LLM you're using]

5. Prepare your `tools-specific_task.csv` file with the topics and tools you want the bot to post about

## Usage

The bot will run automatically based on the schedule defined in the GitHub Actions workflow file (`.github/workflows/twitter_bot.yml`).

To run the bot manually:

```
python twitter_bot.py
```

## File Structure

- `main.py`: Main script for the Twitter bot 
- `Twitter_Api.py`: Module for interacting with the Twitter API and generating content using the LLM
- `save_tweet.csv`: CSV file storing posted tweets
- `tools-specific_task.csv`: CSV file containing topics and tools for content generation
- `.github/workflows/actions.yml`: GitHub Actions workflow file

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
