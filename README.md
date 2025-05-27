# TwitterAutomated

A Python script that automatically generates and posts tweets about various coding tools using the OpenAI API and the Tweepy library.  This project leverages Langchain for prompt engineering and manages tweets in a CSV file.

## Project Overview

This project automates the process of creating and posting tweets about different software development tools. It randomly selects a tool from a CSV file (`tools_specific_task.csv`), generates a tweet description using OpenAI's GPT-3 model, and then posts the tweet to a Twitter account using the Tweepy library.  The generated tweets and their associated tool information are saved to a CSV file (`Save_tweet.csv`).

**Key Features:**

* **Random Tool Selection:**  Selects a random tool and its description from a predefined CSV file.
* **GPT-3 Tweet Generation:** Uses OpenAI's GPT-3 to generate concise and informative tweets based on a template.
* **Twitter Integration:** Posts tweets to a designated Twitter account using the Tweepy library.
* **Tweet Saving:** Stores generated tweets and tool information in a CSV file for record-keeping.
* **Rate Limit Handling:** Includes a basic mechanism to handle OpenAI API rate limits by pausing execution.

**Problem Solved:** Automates the creation and posting of tweets, saving time and effort for promoting various development tools.

**Use Cases:**  Marketing and promotion of software development tools, automating social media presence.


## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Usage](#usage)
5. [Project Architecture](#project-architecture)
6. [Contributing Guidelines](#contributing-guidelines)
7. [License](#license)


## Prerequisites

* Python 3.7+
* `pip` (Python package installer)
* A Twitter developer account with API keys and access tokens.
* An OpenAI API key.
* The `tools_specific_task.csv` file containing tool names and descriptions (see example below).


## Installation

1. Clone the repository: `git clone https://github.com/harshkasat/TwitterAutomated.git`
2. Navigate to the project directory: `cd TwitterAutomated`
3. Install the required packages: `pip install -r requirements.txt`


## Configuration

1. **Create `tools_specific_task.csv`:** This CSV file should have two columns: "tool" and "tool_info".  Each row represents a tool and its description.  Example:

```csv
tool,tool_info
Python,Programming Language
Git,Version Control System
Docker,Containerization Platform
```

2. **Set Environment Variables:** Create a `.env` file in the project's root directory and add your API keys:

```
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
API_KEY=YOUR_TWITTER_API_KEY
API_SECRET_KEY=YOUR_TWITTER_API_SECRET_KEY
ACCESS_TOKEN=YOUR_TWITTER_ACCESS_TOKEN
SECRET_ACCESS_TOKEN=YOUR_TWITTER_SECRET_ACCESS_TOKEN
BEARER_TOKEN=YOUR_TWITTER_BEARER_TOKEN
```

## Usage

Run the `main.py` script: `python main.py`

The script will:

1. Read tools from `tools_specific_task.csv`.
2. Randomly select a tool.
3. Generate a tweet using the selected tool's information and a GPT-3 prompt.
4. Post the tweet to Twitter.
5. Save the tweet information to `Save_tweet.csv`.


## Project Architecture

The project consists of the following components:

* **`main.py`:** The main script that orchestrates the tweet generation and posting process.
* **`Twitter_Api.py`:** Contains classes for interacting with the Twitter API, generating tweets using OpenAI's GPT-3, and saving tweets to a CSV file.  Key classes include:
    * `TwitterClient`: Handles Twitter API interactions (posting tweets).
    * `Template`: Creates the prompt template for GPT-3.  Example:
      ```python
      template = f"""Provide information on the topic of {self.tool} and its relevance in {self.tool_info}. Please limit your response to 20 words. #Information #Coding #Development"""
      ```
    * `LangchainPrompt`: Interacts with the Langchain LLM (OpenAI) to generate tweets. Includes rate limit handling.
    * `ToolSpecficTask`: Selects a random tool and its information from the CSV.
    * `SaveTweet`: Saves the generated tweets to a CSV file.


## Contributing Guidelines

Contributions are welcome! Please open an issue or submit a pull request.


## License

[Specify your license here, e.g., MIT License]


Note:  Error handling and more robust rate limit management could be improved in the provided code.  The current implementation uses a simple retry mechanism with a fixed wait time.  More sophisticated strategies (exponential backoff, etc.) are recommended for production use.  Additionally,  consider adding more comprehensive logging and input validation.
