#
# Library imports
#

from bs4 import BeautifulSoup
import requests

#
# Variables
#

version = "NIV"

#
# Main
#
print("Which book of the Bible would you like headings for?")
book = input("Please type the full name of the book: ").capitalize().strip()
print("Which chapter of " + book + " would you like the headings for?")
chapter = input("Enter a number such as 1: ").strip()
url = "https://www.biblegateway.com/passage/?search=" + book + "%20" + chapter + "&version=" + version

html = requests.get(url)
soup = BeautifulSoup(html.text,'html.parser')
print("--------------------------------------------------------------------")
print(book + " " + str(chapter) + ":")
for x in soup.findAll("h3"):
    for y in x.findAll('span'):
        print(y.get_text())
print("--------------------------------------------------------------------")