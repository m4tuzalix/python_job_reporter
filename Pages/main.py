import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
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
                if len(self.get_all_links()) == int(search_results):
                    break
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
            work = self.get_content(html, links_array, "https://nofluffjobs.com")
            if work == "No more":
                break
        self.close()
        return links_array

class Pracuj(ManualFetch):
    def __init__(self, city):
        self.city = city
        self.selector = pracuj
        super(Pracuj, self).__init__(link=f"https://www.pracuj.pl/praca/{self.city};wp?rd=0", city=self.city)
        self.open_web()
    
    def fetching_data(self):
        from datetime import datetime
        pages = self.browser.find_elements(By.CSS_SELECTOR, self.selector.pages)
        pages = int(pages[len(pages)-2].text)
        day_now = datetime.now().day
        for i in range(1,pages,1):
            try:
                self.browser.execute_script("""window.location = arguments[0]""", f"https://www.pracuj.pl/praca/{self.city};wp?rd=0&pn={str(i)}")
                links = self.browser.find_elements(By.CSS_SELECTOR, self.selector.links)
                for link in links:
                    date_added = str(link.find_element(By.CSS_SELECTOR, self.selector.day).text).split(" ")[1]
                    if int(date_added) == day_now:
                       href = link.find_element(By.TAG_NAME, "a").get_attribute("href")
                       double_check = self.check_db(href)
                       if double_check:
                           self.add_links(href)
                           self.links_array.append(href)
                    else:
                        raise Exception("Fetched all")   
            except Exception as e:
                break
        self.close_web()
        return self.links_array