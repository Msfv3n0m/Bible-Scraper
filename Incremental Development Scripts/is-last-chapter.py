#
# Library imports
#

from bs4 import BeautifulSoup
import requests

#
# Variables
#

book = "John"
chapter = 20
version = "NIV"

#
# Main
#

chapter += 1
url = "https://www.biblegateway.com/passage/?search=" + book + "%20" + str(chapter) + "&version=" + version
html = requests.get(url)
soup = BeautifulSoup(html.text,'html.parser')

if (soup.find_all("a", {"class": "next-chapter", "title": book + " " + str(chapter) })):
    print("this is not the last chapter of the book")
else:
    print("this is the last chapter of the book")
