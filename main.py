from selenium import webdriver
from helper import get_post_info
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import pandas
import json
from datetime import date
from IPython.display import display

df = pandas.DataFrame(columns=['post_url', 'account', 'like_count', 'comment_count', 'share_count', 'caption', 'hashtags','comments', 'date_posted', 'date_collect'])

while len(df) < 100:
    options = webdriver.ChromeOptions() 
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-setuid-sandbox")
    # options.binary_location = '/usr/bin/google-chrome'
    # options.add_argument("--remote-debugging-port=9230")

    # START DRIVER
    # executable_path='/usr/local/bin/chromedriver', 
    driver = uc.Chrome(options=options)
    driver.get("https://www.tiktok.com")

    # GET ALL POSTS' URLS
    soup = BeautifulSoup(driver.page_source, "html.parser")
    script = soup.find("script", {"id": "SIGI_STATE"}).text.strip()
    json_object = json.loads(script)

    # handle KeyError Exception
    while not json_object['ItemList'] or not json_object['ItemList']['foryou'] or not json_object['ItemList']['foryou']['list'] or not json_object['UserModule'] or not json_object['UserModule']['users']:
        driver.refresh()

    video_id_list = json_object['ItemList']['foryou']['list']
    user_name_list = list(json_object['UserModule']['users'].keys())

    url_list = []
    for i in range(len(user_name_list)):
        prefix = 'https://www.tiktok.com/@'
        post_url = prefix + user_name_list[i] + '/video/' + video_id_list[i]
        url_list.append(post_url)

    # GET ALL POST INFORMATION
    for url in url_list:
        post_info = get_post_info(url)
        df = df.append({'post_url': post_info[0], 
                        'account': post_info[1], 
                        'like_count': post_info[2], 
                        'comment_count': post_info[3], 
                        'share_count': post_info[4], 
                        'caption': post_info[5], 
                        'hashtags': post_info[6], 
                        'comments': post_info[8], 
                        'date_posted': post_info[7], 
                        'date_collect': date.today()}, ignore_index = True)
        display(df)
        
    driver.quit()

df.to_csv('result.csv')