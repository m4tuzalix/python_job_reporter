from selenium import webdriver
from selenium.webdriver.common.by import By
from JavaScript.javascript import main_js, scroll_js
from time import sleep
from Database.database import Database
from os import path

class ManualFetch(Database):
    def __init__(self, link=None, all_links=None, city=None, city_name=None, bar_scroll=None, date_posted=None):
        super(ManualFetch, self).__init__()
        self.all_links = all_links
        self.link = link
        self.city = city
        self.city_name = city_name
        self.bar_scroll = bar_scroll
        self.date_posted = date_posted
        self.days = 1 #// adverts created within the given number
        self.timer = 700 #// scrolling pixels value
        self.links_array = []
        self.db_main()
        print("Manual fetching started")
    
    def open_web(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--enable-javascript")
        self.browser = webdriver.Chrome(path.abspath("chromedriver.exe"), chrome_options=self.options)
        self.browser.set_script_timeout(10)
        self.browser.implicitly_wait(10)
        self.browser.maximize_window()
        self.browser.get(self.link)

    def get_all_links(self):
        return self.browser.find_elements(By.CSS_SELECTOR, self.all_links)

    def link_validation(self, link, *args):
        link_href = link.find_element(By.TAG_NAME, "a").get_attribute("href")
        validation = self.browser.execute_script(main_js, self.days, self.city, self.city_name, link, self.date_posted, self.bar_scroll)
        if validation != False:
            double_check = self.check_db(str(link_href))
            if "linkedin" in args:
                refId = link_href.index("refId")
                if double_check:
                    self.add_links(str(link_href[:refId]))
                    self.links_array.append(link_href)
            else:
                if double_check:
                    self.add_links(str(link_href))
                    self.links_array.append(link_href)
        else:
            return False
        return True
    
    def scroll_down(self, timer):
        try:
            scrolling = self.browser.execute_script(scroll_js, self.bar_scroll, timer, self.link) #// Scrolling down triggers the divs to appear on the page
        except:
            return False


    def close_web(self):
        self.close()
        self.browser.quit()
