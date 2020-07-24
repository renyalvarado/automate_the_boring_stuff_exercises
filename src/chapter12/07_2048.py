#! /usr/bin/env python3
# Play 2048 game

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

base_url = "https://gabrielecirulli.github.io/2048/ "

browser = webdriver.Firefox()
browser.get(base_url)
time.sleep(10)
body_html = browser.find_element_by_tag_name("body")
body_html.send_keys(Keys.UP)
time.sleep(2)
body_html.send_keys(Keys.RIGHT)
time.sleep(2)
body_html.send_keys(Keys.DOWN)
time.sleep(2)
body_html.send_keys(Keys.LEFT)
