from PageModels.manual_fetch_model import ManualFetch
from PageModels.remote_fetching import RemoteFetch
from Selectors.page_selectors import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


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
        self.delay = 0.5
        self.open_web()
    
    def fetching_data(self):
        search_results = self.browser.find_element(By.CSS_SELECTOR, self.selector.search_results).text
        while True:
            try:
                found_results = WebDriverWait(self.browser, self.delay).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.selector.final_button)))
                found_results.click()
                self.scroll_down(self.timer)
                break
            except:
                self.scroll_down(self.timer)
            self.timer += 99999
        for link in self.get_all_links():
            try:
                self.link_validation(link, "linkedin")
            except:
                continue
        self.close_web()
        return self.links_array

class NoFluffJobs(RemoteFetch):
    def __init__(self, city):
        self.city = city
        selector = nofluffjobs
        super(NoFluffJobs, self).__init__(links=selector.links, pages=selector.pages, new=selector.new)

    def fetching_data(self):
        links_array = []
        html = self.get_html(f"https://nofluffjobs.com/jobs/{self.city}?criteria=city%3D{self.city}&page=1")
        pages = self.page_amount(html)
        for i in range(1,pages+1):
            html = self.get_html(f"https://nofluffjobs.com/jobs/{self.city}?criteria=city%3D{self.city}&page={str(i)}")
            work = self.get_content(html, links_array)
            if work == "No more":
                break
        self.close()
        return links_array

