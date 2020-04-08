from manual_fetch_model import ManualFetch
from Selectors.page_selectors import *
from selenium.webdriver.common.by import By

class JustJoinIt(ManualFetch):
    def __init__(self):
        self.selector = justJoinIt
        super(JustJoinIt, self).__init__(link="https://justjoin.it/wroclaw", 
                all_links=self.selector.all_links, 
                city_name=self.selector.city,
                bar_scroll = self.selector.bar_scroll,
                date_posted=self.selector.date_posted)
        self.open_web()
    
    def fetching_data(self):
        valid = True
        while valid:
            try:
                for link in self.get_all_links():
                    valid = self.link_validation(link)
                self.scroll_down(self.timer)
                self.timer += 700
            except:
                continue
        self.browser.quit()
        return self.links_array

class LinkedIn(ManualFetch):
    def __init__(self):
        self.selector = linkedin
        super(LinkedIn, self).__init__(link="https://www.linkedin.com/jobs/search?location=Wroc%C5%82aw%2C%2BWoj.%2BDolno%C5%9Bl%C4%85skie%2C%2BPolska&trk=public_jobs_jobs-search-bar_search-submit&f_TP=1&redirect=false&position=1&pageNum=0", 
                all_links=self.selector.all_links, 
                city_name=self.selector.city,
                bar_scroll = self.selector.bar_scroll,
                date_posted=self.selector.date_posted)
        self.open_web()
    
    def fetching_data(self):
        search_results = self.browser.find_element(By.CSS_SELECTOR, self.selector.search_results).text
        while True:
            found_results = len(self.get_all_links())
            if int(search_results) == found_results:
                break
            self.scroll_down(self.timer)
            self.timer += 99999
        for link in self.get_all_links():
            try:
                self.link_validation(link, "linkedin")
            except:
                continue
        self.browser.quit()
        return self.links_array
