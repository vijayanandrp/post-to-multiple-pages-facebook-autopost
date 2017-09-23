from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import os
import urllib.parse

"""
source: https://raw.githubusercontent.com/kyleadkins/facebook-automation/master/selDemo.py
"""

user_name = ''
pass_word = ''
profile = "Vijay Anand"
facebook_url = "http://facebook.com"
page_id = ''


# Code nabbed from Stack Overflow to disable browser
# notifications for selenium
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
current_path = os.getcwd()  # current working path
chrome_path = os.path.join(current_path, 'chromedriver')
browser = webdriver.Chrome(executable_path=chrome_path, chrome_options=chrome_options)
browser.switch_to.window(browser.current_window_handle)
browser.implicitly_wait(30)
browser.maximize_window()

browser.get(facebook_url)
email = browser.find_element_by_css_selector("#email")
password = browser.find_element_by_css_selector("#pass")

email.send_keys(user_name)
password.send_keys(pass_word)

password.submit()

page_url = urllib.parse.urljoin(facebook_url, page_id)
browser.get(page_url)
photo_video = WebDriverWait(browser, 45).until(
    EC.presence_of_element_located((By.XPATH, '//span[text()="Photo/Video"]'))
)
photo_video.click()

status = WebDriverWait(browser, 45).until(
    EC.presence_of_element_located((By.XPATH, '//span[text()="Status"]'))
)
status.click()

status = browser.switch_to.active_element
status.send_keys(Keys.NULL)
status.send_keys('My Dream comes True')

publish = WebDriverWait(browser, 45).until(
    EC.presence_of_element_located((By.XPATH, '//span[text()="Publish"]'))
)
publish.click()

