#!/usr/bin/python3

import utils

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from glob import glob


driver = utils.FirefoxDriver('.')
# Get on the page
driver.get("http://192.168.1.225/index.html")

# sign in
object = driver.find_element_by_id('U1')

print(object.get_attribute("value"))


driver.close()

