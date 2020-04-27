import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from Pages.main import *
from Excel_class.excel_reporting import Excel
from threading import Thread
from queue import Queue


class Starter(Excel):
    def __init__(self, city):
        self.city = city
        Excel.__init__(self)
        self.webs = [JustJoinIt, LinkedIn, NoFluffJobs, Pracuj]
    
    def start_fetching(self):
        final_links = []
        for web in self.webs:
            final_links.extend(x for x in web(self.city).fetching_data())
        return final_links

    def create_report(self, data, words):
        result = self.add_data(data, words)
        print("Finished")
        return result #// boolean

if __name__ == "__main__":
    key_words = ["developer"]
    city = "wroclaw" #// no polish signs
    start = Starter(city.lower())
    data = start.start_fetching()
    start.create_report(data, key_words)
    
