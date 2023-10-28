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

class Twitter:
    def __init__(self):
        self.consumer_key = os.environ.get('API_KEY') 
        self.consumer_secret = os.environ.get('API_SECRET_KEY')
        self.access_token = os.environ.get('ACCESS_TOKEN')
        self.access_token_secret = os.environ.get('SECRET_ACCESS_TOKEN')
        self.bearer_token = os.environ.get('BEARER_TOKEN')
    
    def post_tweet_message(self): 
        api = tweepy.Client(bearer_token=self.bearer_token,
                            consumer_key=self.consumer_key,
                            consumer_secret=self.consumer_secret,
                            access_token=self.access_token,
                            access_token_secret=self.access_token_secret
                            )
        try:
            api.create_tweet(text='Twitter is great for dev and newbies')
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


    def call_tool_specific_task(self):
       
        self.tool, self.specific_task = ToolSpecfic_Task().get_tool()
    
    def get_template(self):
        template = f""" Answer the question based on the context below. If the question cannot be answered using the information provided, answer with "I don't know."

        Context: Recently discovered {self.tool} and it's a game-changer for {self.specific_task}. Highly recommend it to my fellow coders!

        Question: What is the tool/resource mentioned in the context, and what specific task is it recommended for?

        Answer: {self.tool} is the mentioned tool/resource, and it's highly recommended for {self.specific_task}. It's a game-changer in the context.
        """
        return (template)
    
        

class LangchainPrompt:

    def get_template(self):
        get_temp = Template()
        get_temp.call_tool_specific_task()
        self.template = get_temp.get_template()

    
    # initialize the models
    openai = OpenAI(
    model_name="text-davinci-003",
    openai_api_key = os.environ.get('OPENAI_API_KEY')
    )
    
    def LLMPromptTemplate(self):
        try:
            llm = OpenAI(temperature = .8)
            chain = LLMChain(llm = llm, prompt = self.template)
            chain.run()
        except Exception as e:
            print(e)

class ToolSpecfic_Task:
    def random_word(self):
        num = random.randint(0,41)
        return num
    
    def get_tool(self):
        df = pd.read_csv('tools-specific_task.csv')
        index = self.random_word()
        tool, specific_task = df.iloc[index,[0,1]]
        return tool, specific_task
 

if __name__ == "__main__":
    # get_temp = Template()
    # get_temp.call_tool_specific_task()
    # get_temp.get_template()
    get_temp = LangchainPrompt()
    get_temp.get_template()
    get_temp.LLMPromptTemplate()
    # post = Twitter()
    # status = post.post_tweet_message()
    # if status:
    #     print('Success')
    # else:
    #     print('Failed')

# PromptTemplate = "🛠️ Recently discovered [tool/resource] and it's a game-changer for [specific task]. Highly recommend it to my fellow coders!        