from selenium import webdriver
import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from test import test
from time import sleep

class PageSettings(object):
    def __init__(self):
        self.browser = webdriver.Chrome("chromedriver.exe")
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--enable-javascript")
        self.browser.set_script_timeout(20)
        self.browser.implicitly_wait(10)
        self.browser.maximize_window()
        self.browser.get("https://justjoin.it/wroclaw")
        
