from Twitter_Api import ToolSpecficTask, Template, LangchainPrompt, TwitterClient, SaveTweet

def main():
    # Get Random Tool and Information about Tool
    get_tool = ToolSpecficTask()
    get_tool  = get_tool.get_tool()
    
    # Get Template about Tool and Information about Tool for GPT model or Custom model
    get_template = Template(**get_tool) 
    get_template = get_template.get_template()

    # Generate Tweet about Tool and Information about Tool using Template
    get_tweet = LangchainPrompt(get_template)
    get_tweet = get_tweet.LLMPromptTemplate()

    # Make Api cal To X(Twitter) to Tweet
    post_tweet = TwitterClient(*get_tweet)
    post_tweet = post_tweet.post_tweet()

    # # save the tweet in Dataframe using pandas
    save_tweet = SaveTweet(tool=get_tool['tool'], tool_info=get_tool['tool_info'], tweet=get_tweet)
    save_tweet = save_tweet.savetweet()

    # # post_tweet = True
    if post_tweet and save_tweet:
        print("Tweet Successfully")
    else:
        print("Tweet Failure")


# if __name__ == '__main__':
    # main()