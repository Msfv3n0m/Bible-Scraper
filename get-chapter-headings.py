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
book_list = input("Please type the full name of the book: ").capitalize().strip().split()

if len(book_list) == 2:
    book = book_list[0] + " " + book_list[1].capitalize()
else:
    book = book_list[0].capitalize()

print("Which chapter of " + book + " would you like the headings for?")
chapter = input("Enter a number such as 1: ").strip()
url = "https://www.biblegateway.com/passage/?search=" + book + "%20" + chapter + "&version=" + version

html = requests.get(url)
soup = BeautifulSoup(html.text,'html.parser')
print("--------------------------------------------------------------------")
print(book + " " + str(chapter) + ":")
for x in soup.findAll("h3"):
    for y in x.findAll('span'):
        print("\t" + y.get_text())
print("--------------------------------------------------------------------")
