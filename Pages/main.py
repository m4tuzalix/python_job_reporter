from PageModels.manual_fetch_model import ManualFetch
from Selectors.page_selectors import *
from selenium.webdriver.common.by import By

class JustJoinIt(ManualFetch):
    def __init__(self, city):
        self.selector = justJoinIt
        super(JustJoinIt, self).__init__(link=f"https://justjoin.it/{city}", 
                all_links=self.selector.all_links, 
                city=self.selector.city,
                city_name=city,
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
        self.close_web()
        return self.links_array

class LinkedIn(ManualFetch):
    def __init__(self, city):
        self.selector = linkedin
        super(LinkedIn, self).__init__(link=f"https://www.linkedin.com/jobs/search?location={city}&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0&f_TP=1", 
                all_links=self.selector.all_links, 
                city=self.selector.city,
                city_name=city,
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
        self.close_web()
        return self.links_array
