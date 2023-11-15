from dotenv import load_dotenv
import tweepy
import os
import random
import openai
import pandas as pd
from langchain.prompts import PromptTemplate
# from abc import ABC, abstractmethod
from langchain.llms import OpenAI
from langchain.chains import LLMChain
load_dotenv()
# Temporary module 

class TwitterClient:
    def __init__(self, tweet):
        self.consumer_key = os.environ.get('API_KEY') 
        self.consumer_secret = os.environ.get('API_SECRET_KEY')
        self.access_token = os.environ.get('ACCESS_TOKEN')
        self.access_token_secret = os.environ.get('SECRET_ACCESS_TOKEN')
        self.bearer_token = os.environ.get('BEARER_TOKEN')
        self.text = tweet
    
    def post_tweet(self): 
        api = tweepy.Client(bearer_token=self.bearer_token,
                            consumer_key=self.consumer_key,
                            consumer_secret=self.consumer_secret,
                            access_token=self.access_token,
                            access_token_secret=self.access_token_secret
                            )
        try:
            # self.text = self.text.strip('\n\n')
            api.create_tweet(text=self.text.strip('\n\n'))
            return True
        except Exception as e:
            print(e)
            return False

"""
    This Bot class is optional because we can use Prompt Template to get suitable results 
"""

# class Bot(ABC):
#     @abstractmethod
#     def __init__(self, message) -> None:
#         self.message = message


# class OpenAI(Bot):    
#     def get_message(message):
#         response = openai.ChatCompletion.create(
#             model = 'gpt-3.5-turbo',
#             messages = [{"role": "user", "content": message},]
#         )
#         response = response['choices'][0]['message']['content']
#         return response

class Template:
    """This class represents Creation of templates"""

    def __init__(self, tool, tool_info):
        self.tool = tool
        self.tool_info = tool_info

    def get_template(self):
        try:
            template = f"""Provide information on the topic of {self.tool} and its relevance in {self.tool_info}. Please limit your response to 20 words. #Information #Coding #Development"""
            return (template)
        except Exception as e:
            print(e)
        

class LangchainPrompt:

    """ This class provides a way to interact with the LangchainPrompt with Openai GPT-3 """

    def __init__(self, template) :
        self.get_template = template
    
    def LLMPromptTemplate(self):
        try:
            # print(self.template)
            # prompt = PromptTemplate.from_template(template=self.get_template)
            llm = OpenAI(openai_api_key = os.environ.get('OPENAI_API_KEY'))
            tweet = llm.predict(self.get_template)
                
            return (tweet)
        except Exception as e:
            print(e)

class ToolSpecficTask:
    """Random Tool and Infomation about Tool from the csv file."""

    def random_word(self):
        rand = random.randint(0,40)
        return rand
    
    def get_tool(self):
        try:
            df = pd.read_csv('tools-specific_task.csv')
            index = self.random_word()
            tool, tool_info = df.iloc[index,[0,1]]
            return (tool, tool_info)
        except Exception as e:
            print(e)

class SaveTweet:
    """Saving tweet generate by Tools and Store in .csv file"""

    def __init__(self, tool, tool_info, tweet) -> None:
        self.tool = tool
        self.tool_info = tool_info
        self.tweet = tweet
    
    def savetweet(self):
        try:
            # Add the new tweet information
            new_tweet = {
                "Tool": self.tool,
                "ToolInfo": self.tool_info,
                "Tweet": self.tweet.strip('\n\n')
            }
            
            # Check if the CSV file already exists
            try:
                df = pd.read_csv('Save_tweet.csv')
            except FileNotFoundError:
                # If the file doesn't exist, create a new DataFrame
                df = pd.DataFrame(columns=['Tool', 'ToolInfo', 'Tweet'])

            # Concatenate the new tweet with the existing DataFrame
            df = pd.concat([df, pd.DataFrame([new_tweet])], ignore_index=True)

            # Save the updated DataFrame to the CSV file
            df.to_csv('Save_tweet.csv', index=False)
                
            return True
        except Exception as e:
            print(e)



def main():

    # Get Random Tool and Information about Tool
    get_tool = ToolSpecficTask()
    get_tool, get_tool_info = get_tool.get_tool()
    
    # Get Template about Tool and Information about Tool for GPT model or Custom model
    get_template = Template(tool=get_tool, tool_info=get_tool_info) 
    get_template = get_template.get_template()

    # Generate Tweet about Tool and Information about Tool using Template
    get_tweet = LangchainPrompt(get_template)
    get_tweet = get_tweet.LLMPromptTemplate()

    # Make Api cal To X(Twitter) to Tweet
    post_tweet = TwitterClient(tweet=get_tweet)
    post_tweet = post_tweet.post_tweet()

    # save the tweet in Dataframe using pandas
    save_tweet = SaveTweet(tool=get_tool, tool_info=get_tool_info, tweet=get_tweet)
    save_tweet = save_tweet.savetweet()

    # post_tweet = True
    if post_tweet and save_tweet:
        print("Tweet Successfully")
    else:
        print("Tweet Failure")

if __name__ == "__main__":
    main()


# PromptTemplate = "🛠️ Recently discovered [tool/resource] and it's a game-changer for [specific task]. Highly recommend it to my fellow coders!        