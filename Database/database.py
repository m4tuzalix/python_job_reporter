from sqlite3 import Connection
from datetime import datetime, timedelta
from os import path

class Database(Connection):
    def __init__(self, **args):
        Connection.__init__(self, path.abspath('Database/main.db'))
        self.cur = self.cursor()
        self.date = datetime.now().date()
        self.time = str(datetime.now().time())
    
    def db_main(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS links(id INTEGER PRIMARY KEY, link TEXT UNIQUE, date TEXT, time TEXT)")
        self.cur.execute("DELETE FROM links WHERE date >= ?", (str(self.date+timedelta(days=3)),))
        self.commit()
        return True

    def check_db(self,link):
        result = None
        self.cur.execute("SELECT * FROM links WHERE link=?", (link,))
        if self.cur.fetchone():
            result = False
        else:
            result = True
        self.commit()
        return result

    def add_links(self,link):
        self.cur.execute("INSERT INTO links VALUES(NULL,?,?,?)", (link,self.date,self.time,))
        self.commit()
