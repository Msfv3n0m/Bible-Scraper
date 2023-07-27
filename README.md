# Bible-Scraper
I have always had a hard time remembering the reference for the events found in scripture; I find the headings to be very useful in remembering this, but it was a pain to do it by hand. Here is a little repo of scripts for scraping the headings from chapters in the bible by parsing and searching biblegateway.com's content. I'm hoping this will be helpful for mapping chapters to events

## Installation
1. Install [python3](https://www.bing.com/ck/a?!&&p=604f706e7df28e3cJmltdHM9MTY5MDQxNjAwMCZpZ3VpZD0xM2U0MzFkNi1jOTMwLTY2N2MtMmY2ZS0yMjlhYzhmNzY3YmImaW5zaWQ9NTIxNQ&ptn=3&hsh=3&fclid=13e431d6-c930-667c-2f6e-229ac8f767bb&psq=python3&u=a1aHR0cHM6Ly93d3cucHl0aG9uLm9yZy9kb3dubG9hZHMv&ntb=1) </br>
2. Install the required python modules </br>
`pip install -r requirements.txt` </br> 
## Usage
![](https://github.com/Msfv3n0m/Bible-Scraper/blob/main/usage1.PNG) </br>
The current translation is in NIV, but that can be easily changed by editing the version variable in the script to be whatever version you prefer
## Issues
- some headings will return with 1-2 letters encapsulated by parentheses appended at the end
