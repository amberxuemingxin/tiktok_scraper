import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

############
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import chromedriver_autoinstaller


# GET CAPTIONS AND HASHTAGS
def parse_caption(tokens) -> list:
    hashtag_list = []
    title_list = []
    # splitting the text into words
    for word in tokens.split():
        # checking the first character of every word
        if word[0] == '#':
            # adding the word to the hashtag_list
            hashtag_list.append(word)
        else:
            title_list.append(word)

    title = ' '.join(title_list)
    return [title, hashtag_list]


def get_post_info(url):
    options = webdriver.ChromeOptions() 
    # options.add_argument("--disable-gpu")
    # options.add_argument("--window-size=1200,900")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-extensions")
    # options.add_argument("--disable-dev-shm-usage")

    
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-setuid-sandbox")
    #options.binary_location = '/usr/bin/google-chrome'

    options.add_argument("--remote-debugging-port=9230") #################

    #executable_path='/usr/local/bin/chromedriver', 
    driver = uc.Chrome(options=options)
    wait = WebDriverWait(driver, 20)
    driver.get(url)

    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-modal"]/div[2]'))).click()
    time.sleep(2)

    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')

    res = [url]

    # GET ACCOUNT NAME
    account = soup.find("span", {"data-e2e": "browse-username"}).text.strip()
    # print("account: " + account)
    res.append(account)

    # GET LIKE COUNT, COMMENT COUNT, SHARE COUNT
    like_count = soup.find("strong", {"data-e2e": "like-count"}).text.strip()
    comment_count = soup.find("strong", {"data-e2e": "comment-count"}).text.strip()
    share_count = soup.find("strong", {"data-e2e": "share-count"}).text.strip()
    res.append(like_count)
    res.append(comment_count)
    res.append(share_count)

    # GET CAPTIONS AND HASHTAGS
    tokens = soup.find("div", {"data-e2e": "browse-video-desc"}).text.strip()
    token_list = parse_caption(tokens)
    caption = token_list[0]
    hashtags = token_list[1]
    res.append(caption)
    res.append(hashtags)

    # GET ACCOUNT NICKNAME AND DATE POSTED
    info = soup.find("span", {"data-e2e": "browser-nickname"}).text.strip()
    info_list = info.split('·')
    date_posted = info_list[-1].strip()
    res.append(date_posted)

    # GET COMMENTS
    time.sleep(2)
    driver.refresh()
    driver.execute_script("window.scrollTo(0, 2000)")

    page = driver.page_source
    time.sleep(2)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    comments = soup.find_all("p", {"data-e2e": "comment-level-1", "class": "tiktok-q9aj5z-PCommentText e1g2efjf6"})
    comment_list = [comment.text.strip() for comment in comments]
    res.append(comment_list)
    
    
    driver.stop_client() ###############
    driver.close() ###############
    driver.quit()
    
    return res

# USER LOGIN
def selenium_user_login(driver):
    login = driver.find_element("xpath", '/html/body/div[2]/div[1]/div/div[3]/button')
    driver.execute_script("arguments[0].click();", login)
    # login.click()
    time.sleep(5)
    phone_login = driver.find_element("xpath", "/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div/div/a[2]")
    driver.execute_script("arguments[0].click();", phone_login)
    # phone_login.click()
    time.sleep(5)
    username_login = driver.find_element("xpath", "//*[contains(text(), 'Log in with email or username')]")
    driver.execute_script("arguments[0].click();", username_login)
    # username_login.click()
    time.sleep(5)
    username = driver.find_element("xpath", ".//*[@name='username']")
    username.send_keys('amberxue0123')
    time.sleep(5)
    password = driver.find_element("xpath", ".//*[@type='password']")
    password.send_keys('4008958658pD@')
    time.sleep(5)
    login2 = driver.find_element("xpath", ".//*[@class='e1w6iovg0 tiktok-9c63gx-Button-StyledButton ehk74z00']")
    driver.execute_script("arguments[0].click();", login2)
    time.sleep(30)

def manual_user_login(driver):
    login_condition = False
    while not login_condition:
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[contains(text(), 'Login Successful')]")))
            login_condition = True
        except:
            login_condition = False
    print('\nsuccessful login')
    time.sleep(30)
    return