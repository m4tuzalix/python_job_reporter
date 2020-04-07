from settings import PageSettings
from selenium.webdriver.common.by import By
from test import test

class Scraper(PageSettings):
    def __init__(self):
        super().__init__()
        print("Started work")
        
    def just_joinit_scrap(self):
        links_array = []
        result = True
        timer = 700
        days = 3
        while result:
            try:
                all_links = self.browser.find_elements(By.CSS_SELECTOR, "a.css-18rtd1e")
                for link in all_links:
                    link_href = link.get_attribute("href")
                    city = link.find_element(By.CSS_SELECTOR, "div.css-1ihx907").text
                    if not str(link_href) in links_array and city == "Wrocław":
                        links_array.append(link_href)
                result = self.browser.execute_script(test, timer, days)
                timer += 700
            except:
                continue
        return links_array
        
        


m = Scraper()
m.just_joinit_scrap()