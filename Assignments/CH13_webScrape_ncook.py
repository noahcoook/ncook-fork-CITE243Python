"""
===========================================================
Program Name: play2048
Author: Noah Cook
Date: 10/19/2025
Description:
    This program sends random keys to play the 2048 web game.
    It is designed to send random keystrokes to play the 2048 game.
    
Usage:
    Run the script using Python 3.9. Ensure all dependencies
    are installed before execution.

===========================================================
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import random, time

browser = webdriver.Firefox()
browser.get('https://play2048.co')
time.sleep(5)

random_keys = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]
sent_keys = ''

for i in range(1, 300):    
    sent_keys = random.choice(random_keys)
    html_elem = browser.find_element(By.TAG_NAME, 'html')
    html_elem.send_keys(sent_keys)
    time.sleep(.1)
