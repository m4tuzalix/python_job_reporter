from selenium import webdriver
import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from selenium.webdriver.common.by import By
from JavaScript.javascript import main_js, scroll_js
from time import sleep

class PageSettings(object):
    def __init__(self, link=None, all_links=None, city_name=None, bar_scroll=None, date_posted=None):
        self.all_links = all_links
        self.link = link
        self.city_name = city_name
        self.bar_scroll = bar_scroll
        self.date_posted = date_posted
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--enable-javascript")
        self.options.add_argument("--headless")
        self.browser = webdriver.Chrome("D:/netguru/features/chromedriver.exe", chrome_options=self.options)
        self.browser.set_script_timeout(20)
        self.browser.implicitly_wait(20)
        self.browser.maximize_window()
        self.browser.get(link)
        self.days = 3
           
    def web_scroling(self):
        links_array = []
        timer = 700
        result = True
        while result:
            try:
                links = self.browser.find_elements(By.CSS_SELECTOR, self.all_links)
                for link in links:
                    link_href = link.find_element(By.TAG_NAME, "a").get_attribute("href")
                    validation = self.browser.execute_script(main_js, timer, self.days, self.city_name, link, self.date_posted, self.bar_scroll)
                    if validation != False:
                        if not str(link_href) in links_array:
                            links_array.append(link_href)
                    else:
                        result = False
                        break
                scrolling = self.browser.execute_script(scroll_js, self.bar_scroll, timer, self.link) #// Scrolling down triggers the divs to appear on the page
                sleep(0.2)
                timer += 700
                if scrolling == "bottom": #// when scrolling hits the offsetHeight then stops
                    break
            except:
                continue
        return links_array
    