from requests_html import HTMLSession
from Database.database import Database

class RemoteFetch(Database):
    def __init__(self, links=None, pages=None, new=None):
        self.links = links
        self.pages = pages
        self.new = new
        super(RemoteFetch, self).__init__()
        self.db_main()
        print("Remote fetching started")
    
    def get_html(self, link):
        scrap = HTMLSession().get(link)
        return scrap
    
    def page_amount(self, core):
        pages = core.html.find(self.pages)
        last_page = pages[len(pages)-2].text
        return int(last_page)
        
    def get_content(self, core, array):
        try:
            links = core.html.find(self.links)
            for link in links:
                href = "https://nofluffjobs.com"+link.attrs["href"]
                day = link.find(self.new, first=True)
                if "NEW" in str(day.text):
                    double_check = self.check_db(href)
                    if double_check:
                        self.add_links(href)
                        array.append(href)
                else:
                   return "No more"
        except:
            return False
        
