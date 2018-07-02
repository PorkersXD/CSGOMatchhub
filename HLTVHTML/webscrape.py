import sys
import requests
import time
from time import sleep
import sqlite3
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup



class match:
    def __init__(self, event, maps, t1name, t1crest, t1result, t2name, t2crest, t2result, ID):
        self.event = event
        self.maps = maps
        self.t1name = t1name
        self.t1crest = t1crest
        self.t1result = t1result
        self.t2name = t2name
        self.t2crest = t2crest
        self.t2result = t2result
        self.ID = ID

def getMatchInfo():
    print("-- Getting Info")
    start = time.time()
    matches = []
    global matchlist
    matchlist = []
    url = 'http://localhost:3000'
    
    page = requests.get(url)
 
    matches = page.text
    
    # Splits up matches page into seperate matches
    matchlist = matches.split('},{')
    
    end = time.time()
    
    print('-- Games loaded: ', len(matchlist), '(', round(end - start, 2), ' Seconds)')
    
    
    
def main():    
    print("-- Beginning Conversion")

    matchone = matchlist
    matchnum = 0
    c.execute('DELETE FROM Matches')
    c.execute('UPDATE SQLITE_SEQUENCE SET SEQ=0')     
    for x in range(len(matchlist)):
        matchone = matchlist[matchnum]
        conversion(matchone)
        matchnum += 1
        
    print("-- Matches Collected")    
        
        
def conversion(matchone):    
    # Splits match into seperate components     
    matchone = str(matchone)
    matchone = matchone.split(',')
    
    # Event
    event = str(matchone[0])
    event = event.split('"')
    event = str(event[3])
    
    maps = str(matchone[1])
    maps = maps.split('"')
    maps = str(maps[3])
    
    t1name = str(matchone[2])
    t1name = t1name.split('"')
    t1name = str(t1name[5])
    
    t1crest = str(matchone[3])
    t1crest = t1crest.split('"')
    t1crest = str(t1crest[3])
    
    t1result = str(matchone[4])
    t1result = t1result.split(':')
    t1result = str(t1result[1])
    t1result = t1result.split('}')
    t1result = str(t1result[0])
    
    t2name = str(matchone[5])
    t2name = t2name.split('"')
    t2name = str(t2name[5])
    
    t2crest = str(matchone[6])
    t2crest = t2crest.split('"')
    t2crest = str(t2crest[3])
    
    t2result = str(matchone[7])
    t2result = t2result.split(':')
    t2result = str(t2result[1])
    t2result = t2result.split('}')
    t2result = str(t2result[0])
    
    ID = str(matchone[8])
    ID = ID.split('"')
    ID = str(ID[3])
    
    firstmatch = match(event, maps, t1name, t1crest, t1result, t2name, t2crest, t2result, ID)

    params = (firstmatch.event, firstmatch.t1name, firstmatch.t1crest, firstmatch.t1result, firstmatch.t2name, 
              firstmatch.t2crest, firstmatch.t2result, firstmatch.maps, firstmatch.ID)
    
    query = (
        'INSERT INTO Matches '
        'VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)')
    
       
    c.execute(query, params)
    conn.commit()


def webscrape():
    done = False
    while not done:
        getMatchInfo()
        main()
        print("Wating 60 seconds to update...")
        sleep(60)    
        
        
def __program__():
    try:
        webscrape()
        
    except Exception as e:
        print("Error: " + str(e), ", contact 'jollyc@student.lincoln.school' for support.")
        print("Relaunching...")
        sleep(5)
        print("")
        __program__()   
        
        
        
print("-- Imported libs")
DATABASE = 'db/matchinfo.db'
conn = sqlite3.connect(DATABASE)
c = conn.cursor()

print("-- Database connected")
print("")

__program__()
