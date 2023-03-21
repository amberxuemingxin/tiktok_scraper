from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# options.binary_location = "/etc/apt/sources.list.d/google-chrome.list"    #chrome binary location specified here
options.add_argument("--start-maximized") #open Browser in maximized mode
options.add_argument("--no-sandbox") #bypass OS security model
options.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
options.add_argument('--headless')
options.add_argument("--remote-debugging-port=9222")
command_executor = "http://localhost:4444/wd/hub"
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
driver.get('http://google.com/')