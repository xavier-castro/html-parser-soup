#! python3

# This was made to get an understanding of the bs4 library. The full program is the other .py in this folder

import bs4          # needed for beautiful parsing
import requests     # needed for downloading

res = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')      # passing the html text we got it (inside the .txt). second argument silences html parsing warning
elems = soup.select('#usedOfferAccordionRow > div > div.a-accordion-row-a11y > a > h5 > div > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-secondary.header-price')
print(elems[0].text)   # holds a string value inside the html text
print(elems[0].text.strip() )  # removes extra white space