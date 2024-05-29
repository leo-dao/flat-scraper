from bs4 import BeautifulSoup
from splinter import Browser
import time

BASE_URL = 'https://www.facebook.com'
LISTING_SELECTOR = 'a[class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 xggy1nq x1a2a7pz x1heor9g xt0b8zv x1hl2dhg x1lku1pv"]'
PRICE_SELECTOR = 'div[class="x78zum5 x1q0g3np x1iorvi4 x4uap5 xjkvuk6 xkhd6sd"]'
SEE_MORE_SELECTOR = f'div[class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1n2onr6 x87ps6o x1lku1pv x1a2a7pz"][role="button"]:not([aria-label])'
DESCRIPTION_SELECTOR = 'span[class="x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u"]'
INFO_SELECTOR = 'span[class="x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u x1yc453h"]'

def close_popup(browser):
    time.sleep(3)
    if browser.is_element_present_by_css('div[aria-label="Close"]'):
        # Click on the element once it's found
        browser.find_by_css('div[aria-label="Close"]').first.click()

def goto_page(browser, url):
    browser.visit(url)
    time.sleep(1)
    close_popup(browser)

def scroll_down(browser):
    for i in range(3):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

def get_price(listing):
    price = listing.select_one(PRICE_SELECTOR).text

    # convert to an integer
    price = price.replace('$', '').replace(',', '')
    price = ''.join(filter(str.isdigit, price))
    price = int(price)

    return price

def get_description(browser, selector):
    if browser.is_element_present_by_css(selector):
        return browser.find_by_css(selector)[1].text.split('See less')[0]
    return 'No description available'

def parse_info_lines(info_lines):
    info = {}
    for line in info_lines:
        text = line.text
        if 'Dog and cat' in text or 'Dog' in text or 'Cat' in text:
            info['pets'] = text
        elif 'Available' in text:
            info['available'] = text.split('Available')[1].strip()
        elif 'Furnished' in text or 'Unfurnished' in text:
            info['furnished'] = text
    return info

def get_listing_info(browser):
    
    # Scroll a bit to load the description
    browser.execute_script("window.scrollTo(0, 500);")
    time.sleep(3)

    if browser.is_element_present_by_css(SEE_MORE_SELECTOR):

        button = browser.find_by_css(SEE_MORE_SELECTOR).first

        button.click()

    description = get_description(browser, DESCRIPTION_SELECTOR)

    info_lines = browser.find_by_css(INFO_SELECTOR)
    address = info_lines[0].text if info_lines else ''

    info = {
        'address': address,
        'description': description,
    }

    info.update(parse_info_lines(info_lines))

    return info

def scrape_listings():
    browser = Browser('chrome')
    
    goto_page(browser, BASE_URL + '/marketplace/montreal/search/?query=2%20bedroom%20apartment%20for%20rent')

    # Scroll down to load more listings
    #scroll_down(browser)

    # Parse html
    html = browser.html

    # Create a BeautifulSoup object from the scraped HTML
    market_soup = BeautifulSoup(html, 'html.parser')

    # Find all the listings on the page
    listings = market_soup.select(LISTING_SELECTOR)
    listings_list = []

    # Loop through the listings
    for listing in listings:

        # Check price of listing
        price = get_price(listing)

        # TODO: User input for max price
        
        # Get the link of the listing
        link = listing.get('href')
        
        goto_page(browser, BASE_URL + link)

        listing_info = get_listing_info( browser)

        listing_info.update({'price': price})

        # Append the listing to the list
        listings_list.append(listing_info)
        print (listing_info)

    browser.quit()