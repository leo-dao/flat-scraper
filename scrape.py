import requests
from bs4 import BeautifulSoup
from splinter import Browser
import time


# Set up Splinter
browser = Browser('chrome')
browser.visit('https://www.facebook.com/marketplace/montreal/search/?query=2%20bedroom%20apartment%20for%20rent')


# Close the login popup
if browser.is_element_present_by_css('div[aria-label="Close"]', wait_time=10):
    # Click on the element once it's found
    browser.find_by_css('div[aria-label="Close"]').first.click()


# Scroll down to load more listings
for i in range(3):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# Parse html
html = browser.html

# Create a BeautifulSoup object from the scraped HTML
market_soup = BeautifulSoup(html, 'html.parser')

# 
listings = market_soup.find_all('a', class_='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 xggy1nq x1a2a7pz x1heor9g xt0b8zv x1hl2dhg x1lku1pv')
listings_list = [listings.get('href') for listings in listings]
print(listings_list)