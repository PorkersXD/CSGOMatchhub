import requests
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

print("-- Imported libs")











matches = []
matchlist = []
url = 'http://localhost:3000'

page = requests.get(url)

print(page.text)

matches = page.text

# Splits up matches page into seperate matches
matchlist = matches.split('},{')
print('--Games loaded: ', len(matchlist))



print(matchlist)
matchone = matchlist[0]

# Splits match into seperate components     
matchone = matchone.split(',')

# Event
event = str(matchone[0])
event = event.split('"')
event = str(event[3])

maps = str(matchone[1])
maps = maps.split('"')
maps = str(maps[2])

t1name = str(matchone[2])
t1name = t1name.split('"')
t1name = str(t1name[5])

t1crest = str(matchone[3])
t1crest = t1crest.split('"')
t1crest = str(t1crest[2])

#t1result = str(matchone[4])
#t1result = t1result.split('"')
#t1result = str(t1result[5])

t2name = str(matchone[5])
t2name = t1name.split('"')
t2name = str(t1name[5])

# Match attribute sorting code
class match:
        def __init__(self, event, maps, t1name, t1crest, t1result, t2name, t2crest, t2result, ID):
                self.t1name = t1name
                self.t1crest = t1crest
                self.t1result = t1result
                self.t2name = t2name
                self.t2crest = t2crest
                self.t2result = t2result

