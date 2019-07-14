import bs4
import time
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#set variables and grab client
my_url = 'https://en.wikipedia.org/wiki/Twice_(group)'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
infobox_soup = page_soup.find("table",{"class":"infobox vcard plainlist"}).tbody




x, sleeper = 0, 5
while True:
    print("sleepy time: " + str(x * sleeper))
    time.sleep(sleeper)
    x += 1


















#end of file
