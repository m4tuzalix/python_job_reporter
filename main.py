from settings import PageSettings
from Selectors.page_selectors import *

class JustJoinIt(PageSettings):
    def __init__(self):
        selector = justJoinIt
        super().__init__(link="https://justjoin.it/wroclaw", 
                all_links=selector.all_links, 
                city_name=selector.city,
                bar_scroll = selector.bar_scroll,
                date_posted=selector.date_posted)
        self.days = 5
        print("Started work")

class LinkedIn(PageSettings):
    def __init__(self):
        selector = linkedin
        super().__init__(link="https://www.linkedin.com/jobs/search?location=Wroc%C5%82aw%2C%2BWoj.%2BDolno%C5%9Bl%C4%85skie%2C%2BPolska&trk=public_jobs_jobs-search-bar_search-submit&f_TP=1&redirect=false&position=1&pageNum=0", 
                all_links=selector.all_links, 
                city_name=selector.city,
                bar_scroll = selector.bar_scroll,
                date_posted=selector.date_posted)

        


m = LinkedIn().web_scroling()
print(len(m))
