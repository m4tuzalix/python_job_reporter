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
        print("Started work")

class LinkedIn(PageSettings):
    def __init__(self):
        selector = linkedin
        super().__init__(link="https://www.linkedin.com/jobs/search?location=Wroc%C5%82aw%2Bi%2Bokolice&trk=public_jobs_jobs-search-bar_search-submit&f_TP=1&redirect=false&position=1&pageNum=0", 
                all_links=selector.all_links, 
                city_name=selector.city,
                bar_scroll = selector.bar_scroll,
                date_posted=selector.date_posted)
        


m =  LinkedIn()
print(m.web_scroling())