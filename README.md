# Job scraper from the most popular services in Poland (Currently 2 - will be more !)


# Info
- Scraper gathers the offers which have appeared within 24 hours
- Scraper creates the daily report from offers which contain the key words provided by user
- Scraper can be ran anytime - it creates the date report and edits it (each day = one new xls file)
- Scraper avoids duplicates
- DataBase clears itself daily

# Setup
- open starter.py in your editor
- find variable 'city' and put the city you are interested about
- find variable 'key_words' and add as many words as you want. I recommend max 3. 

# Requirements
1.  Python 3.x required
2. Chrome browser required (chromedriver.exe in repo is for version 80)
3. If you have another version of chrome, go to this web https://chromedriver.chromium.org/downloads and find the proper one
4. Replace the downloaded chromedriver with the one existing in repo

# How to run
1. clone this repository
2. open repository location in cmd/powershell
3. pip install -r requirements.txt
4. python starter.py
5. Report will be created in "Day Reports" folder :) Good luck !




