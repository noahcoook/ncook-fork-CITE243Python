from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random, time

browser = webdriver.Firefox()
browser.get('https://play2048.co')
time.sleep(5)

random_keys = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]
sent_keys = ''

for i in range(1, 100):
    sent_keys = random.choice(random_keys)
    send_keys(sent_keys)
    time.sleep(1)
