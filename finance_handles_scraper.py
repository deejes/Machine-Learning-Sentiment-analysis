from lxml import html
from bs4 import BeautifulSoup
import requests


links = []
handles = []
root_link = 'http://www.businessinsider.com/117-finance-people-to-follow-on-twitter-2014-9/#charlie-robertson-125'

# extracts all hyperlinks from a url and appends them to links
def links_getter(link):
    page = requests.get(link).content
    soup = BeautifulSoup(page, 'html.parser')
    for a in soup.find_all('a', href=True):
        links.append(a['href'])

links_getter(root_link)

#  fitlers for twitter links
for link in links:
    if 'https://twitter.com/' in link:
        handles.append((link[20:]))

#removes duplicates
handles = set(handles)


# writes them out to a text file.
with open("finance_handles.txt", 'w') as out:
    for x in handles:
        out.write(str(x) + '\n')
