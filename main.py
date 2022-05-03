from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

words = []

driver.get('https://monkeytype.com/')

soup = BeautifulSoup(driver.page_source, 'html.parser')
parse = soup.find_all('div', attrs={'class': 'word'})
for item in parse:
  words.append(item.get_text())

driver.find_element(By.XPATH,'//*[@id="cookiePopup"]/div[2]/div[2]/div[1]').click()
driver.find_element(By.XPATH,'/html/body')

actions = ActionChains(driver)
for word in words:
  for letter in word:
    actions.send_keys(letter).perform()
    print(letter, word)
  actions.send_keys(' ').perform()
