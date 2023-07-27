#
# Library imports
#

from bs4 import BeautifulSoup
import requests

#
# Variables
#

chapter = 1
version = "NIV"

#
# Main
#

print("Which book of the Bible would you like headings for?")
book = input("Please type the full name of the book: ").capitalize().strip()
done = False
while (done == False):
    next_chapter = chapter+1
    url = "https://www.biblegateway.com/passage/?search=" + book + "%20" + str(chapter) + "&version=" + version
    html = requests.get(url)
    soup = BeautifulSoup(html.text,'html.parser')

    if (soup.find_all("a", {"class": "next-chapter", "title": book + " " + str(next_chapter) }) or soup.find_all("a", {"class": "prev-chapter", "title": book + " " + str(next_chapter-2) })):
        print("--------------------------------------------------------------------")
        print(book + " " + str(chapter) + ":")
        for x in soup.findAll("h3"):
            for y in x.findAll('span'):
                print("\t" + y.get_text())
        chapter = next_chapter
    else:
        done = True
print("--------------------------------------------------------------------")
