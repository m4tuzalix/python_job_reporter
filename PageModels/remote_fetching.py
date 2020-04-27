from requests_html import HTMLSession
from Database.database import Database

class RemoteFetch(Database):
    def __init__(self, links=None, pages=None, new=None):
        self.links = links
        self.pages = pages
        self.new = new
        super(RemoteFetch, self).__init__()
        self.db_main()
        print("Remote fetching started: NoFluffJobs")
    
    def get_html(self, link):
        scrap = HTMLSession().get(link)
        return scrap
    
    def page_amount(self, core):
        page = core.html.find(self.pages)
        return int(page[len(page)-2].text)
        
    def get_content(self, core, position, array, page):
        try:
            links = core.html.find(self.links)
            for link in links:
                href = link.attrs["href"]
                position_name = link.find(position, first=True).text
                if not page in href:
                    href = page + href
                day = link.find(self.new, first=True)
                if "NOWA" in str(day.text):
                    double_check = self.check_db(href)
                    if double_check:
                        self.add_links(href, position_name)
                        array.append([href, position_name])
                else:
                    return "No more"
        except Exception as e:
            print(str(e))
            return False
       
        