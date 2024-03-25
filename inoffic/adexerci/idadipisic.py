from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.headless = True
  
browser = webdriver.Chrome(options=options)

browser.get("https://www.example.com 
print(browser.title)

browser.quit()
