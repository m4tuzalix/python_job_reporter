# Job scraper from the most popular services in Poland (Currently 2 - will be more !)


# Info
- Scraper gathers the adverts which have appeared within 24 hours
- Scraper creates the daily report from adverts which contains the key words provided by user
- Scraper can be run anytime - it creates the date report and edits it (each day = one new xls file)
- Scraper avoids duplicates
- DB clears itself every 3 days

# Setup
- open starter.py in your editor
- find variable 'key_words' and add as many words as you want. I recommend max 3. 

# How to run
1. clone this repository
- Python 3.x required
- Chrome browser required (chromedriver.exe in repo is for version 80)
- If you have another version of chrome, go to this web https://chromedriver.chromium.org/downloads and find the proper one
- Replace the downloaded chromedriver with the one existing in repo
2. open repository location in cmd/powershell
3. pip install -r requirements.txt
4. python starter.py




