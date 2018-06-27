from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

print("-- Imported libs")

#page = requests.get('192.168.1.15:3000')
#page = requests.get('https://realpython.com/python-web-scraping-practical-introduction/')

#raw_html = simple_get('https://realpython.com/python-web-scraping-practical-introduction/')
#print(len(raw_html))

def get_page(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if response_good(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url,str(e)))
        return None

def response_good(resp):

    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)