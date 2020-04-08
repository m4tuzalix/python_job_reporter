import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from Pages.main import *
from Database.database import Database

class Starter(Database):
    def __init__(self):
        Database.__init__(self)
        self.webs = [JustJoinIt, LinkedIn]
        self.final_links = []
    
    def start_fetching(self):
        for web in self.webs:
            self.final_links.extend(x for x in web().fetching_data())
    



if __name__ == "__main__":
    start = Starter()
    start.start_fetching()