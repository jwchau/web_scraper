import bs4
import time
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#set variables and grab client
#my_url = 'https://en.wikipedia.org/wiki/Twice_(group)'
#amazon juan's laptop search
my_url = 'https://amazon.com/s?k=laptop&i=computers&rh=n%3A13896617011%2Cp_85%3A2470955011%2Cp_72%3A1248879011%2Cp_36%3A10000-25000%2Cp_n_size_browse-bin%3A2423840011%2Cp_n_feature_five_browse-bin%3A7817222011%2Cp_n_operating_system_browse-bin%3A17702486011&dc&crid=3G334NDQTHNUL&qid=1563568378&rnid=562215011&sprefix=laptop%2Caps%2C230&ref=sr_nr_p_n_operating_system_browse-bin_1'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
#infbox is for wikipedia: infobox_soup = page_soup.find("table",{"class":"infobox vcard plainlist"}).tbody



x, sleeper = 0, 5
while True:
    print("sleepy time: " + str(x * sleeper))
    time.sleep(sleeper)
    x += 1


















#end of file
