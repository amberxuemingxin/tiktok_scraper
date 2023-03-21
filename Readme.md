## Project Introduction: 
A TikTok Scraper that automatically scrap the tiktok recommendation posts, gather all related information of that post, and create a csv file including all information

## File Description:
```Readme```: The main writeup of the whole project\
```main.py```: The starting point of execution for this TikTok Scraper program. The program executes only when it runs\
```helper.py```: Define two helper functions for the main program. The main logic of getting all required information from a post is implemented in one of the helper function 'get_post_info'\
```Dockerfile```: The text document that contains all commands to call on command line to build a docker image\
```requirements.txt```: Stores information of all libraries and packages in itself that are used during development\
```result.csv```: A csv file shows the example of the result from a single run of this TikTok Scraper program. The 10 attributs are 'post_url', 'account', 'like_count', 'comment_count', 'share_count', 'caption', 'hashtags','comments', 'date_posted', 'date_collect'

## Libraries and Modules:
1. Selenium Python Module
2. Beautiful Soup Python Library
3. Pandas

## Considered but discarded Approaches:
There are actually several existing APIs in the market for developers to retrieve data from TikTok. Some of them are paid and some of them are free. However, I did not choose to use them in my project. Following are two APIs I have considered to use but finally discarded.

### 1. Official TikTok Api (https://developers.tiktok.com)
This is the official Api that TikTok provides for developers to perform analysis tasks. It includes login and video kit, anda bunch of multi-purposes APIs. This official API accelerates a lot the scraping process due to its internal mechanism. The reason I didn't choose it is that to use this official API, I have to register an actual application and link it to a TikTok developer account. To do this, I have to submit a request and wait for TikTok to approve my request. My request was rejected because I was not developing an actual product and my qualification didn't meet their requirements. 

### 2. Unofficial David Teather TikTok-Api (https://github.com/davidteather/TikTok-Api)
This is an unofficial TikTok API wrapper developed by David Teather, and was successfully used by several hundreds of users. This api is designed to retrieve data TikTok, and cannot be used to upload content on the behalf of a user. The reason I didn't choose it is that this API has been non-functional for months since May 2022. 

NOTE: Since the TikTok settings is constantly changed, almost all existing open-sourced tiktok APIs/libraries (scrapers or downloaders) are not functional anymore. 

### 3. TikAPI (https://tikapi.io/), Trendpop (https://www.ensembledata.com/), EnsembleData (https://www.ensembledata.com/) 
These are all PAID unofficial APIs that enable extensive features and functions. They provide a full out-of-box solution for developers for more complex tasks. The reason that I didn't choose it is that they are paid based on the number of posts I need to scrape.

## Possible Extensions:
### 1. Sentiment analysis (tone analyzer)
We can perform sentiment analysis on all comments. Sentiment analysis is an approach to natural language processing (NLP) that identifies the emotional tone behind a body of text. The general algorithm is parse text into sentences, determine if sentence is subjective or objective, and classify positive, negative, or neutral identities via certain mechaine learning rules. An example web service is Komprehend (https://komprehend.io). In this way, we can analyze the general attitudes of a certain post. For example, if a post we are scraping is about a certain fashion style Y2K, by performing the sentiment analysis on the comments, we know if people like this kind of style or not in general, and who like it. 

### 2. Get comment owner information:
When we scrape the comments of a post, we could store the comment column as a map, whose key is the account of that comment, and the value is the comment content. In this way, if this comment is considered as positive by sentiment analysis, this account user is a potential customer for FINESSE. We can record the information of all potential customers in this way, and use them as targets for future marketing campaigns or advertisements. 

### 3. Scrap live videos
In the current trend, the live videos are also a great target to retrieve the data and perform further analysis. Since this TikTok scraper is based on the html content, scraping the live videos will need a different implementation.

### 4. Add search function
The current implemenation is randomly get recommended videos in the TikTok homepage. We can add search functions and start scraping the resulted videos to better narrow down our target. For example, we can search "#ootd" in the search box and start scraping from all the videos with the "#ootd" tags. For each keyword that we search, we can create a separate csv file. In this way, we can better focus on our interested topics. 
