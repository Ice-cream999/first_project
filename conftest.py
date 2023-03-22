from selenium.webdriver.chrome.options import Options
from selenium import webdriver

options = Options()
options.add_experimental_option('--lang=en')
browser = webdriver.Chrome(options=options)