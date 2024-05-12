import requests
from bs4 import BeautifulSoup
from splinter import Browser
import time

def close_popup(browser):
    if browser.is_element_present_by_css('div[aria-label="Close"]', wait_time=10):
        # Click on the element once it's found
        browser.find_by_css('div[aria-label="Close"]').first.click()

def goto_page(browser, url):
    browser.visit(url)
    time.sleep(3)
    close_popup(browser)

def scroll_down(browser):
    for i in range(3):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

def getPrice(listing):
    price = listing.find('div', class_='x78zum5 x1q0g3np x1iorvi4 x4uap5 xjkvuk6 xkhd6sd').text

    # convert to an integer
    price = price.replace('$', '').replace(',', '')
    price = ''.join(filter(str.isdigit, price))
    price = int(price)

    return price

def getListingInfo(browser, html):
    listing_soup = BeautifulSoup(html, 'html.parser')

    # Click on "See More" button to get full description
    class_name = "x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1n2onr6 x87ps6o x1lku1pv x1a2a7pz"
    selector = f'div[class="{class_name}"][role="button"]:not([aria-label])'

    button = browser.find_by_css(selector).first

    print(button.outer_html)

    if button:

        button.click()

        description = browser.find_by_css('span[class="x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u"]')[1].text
        print(description)


def __main__():

    base_url = 'https://www.facebook.com'

    browser = Browser('chrome')
    
    goto_page(browser, base_url + '/marketplace/montreal/search/?query=2%20bedroom%20apartment%20for%20rent')

    # Scroll down to load more listings
    #scroll_down(browser)

    # Parse html
    html = browser.html

    # Create a BeautifulSoup object from the scraped HTML
    market_soup = BeautifulSoup(html, 'html.parser')

    # Find all the listings on the page
    listings = market_soup.find_all('a', class_='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 xggy1nq x1a2a7pz x1heor9g xt0b8zv x1hl2dhg x1lku1pv')
    listings_list = []

    # Loop through the listings
    for listing in listings:

        # Check price of listing
        price = getPrice(listing)

        # TODO: User input for max price
        # If the price is greater than the max price, skip the listing
        max_price = 2000
        min_price = 1000
        if price > max_price or price < min_price:
            continue
        
        # Get the link of the listing
        link = listing.get('href')
        
        goto_page(browser, base_url + link)

        listing_info = getListingInfo( browser, html)

        # Append the listing to the list
        listings_list.append(listing_info)

    browser.quit()

if __name__ == '__main__':
    __main__()