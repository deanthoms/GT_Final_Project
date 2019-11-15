#!/usr/bin/env python
# coding: utf-8

# # Twitter Sentiment Analysis
# ## Dean Thoms
# ### 11-14-2019


# Import necessary dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time


# # Step 1 - Scraping


def scrape():
    # Set static URL's
    url1 = "https://twitter.com/realDonaldTrump?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor"
    url2 = 'https://twitter.com/BarackObama?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'
    url3 = 'https://twitter.com/jimmykimmel?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'
    url4 = 'https://twitter.com/Oprah?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'
    url5 = 'https://twitter.com/atlnewsnow?lang=en'
    url6 = 'https://twitter.com/elonmusk?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'
    url7 = 'https://twitter.com/iamcardib?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'
    url8 = 'https://twitter.com/m_ryan02?lang=en'
    url9 = 'https://twitter.com/KimKardashian?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'
    # Make list of urls
    url_list = [url1, url2, url3, url4, url5, url6, url7, url8, url9]
    
    # Create empty dictionary to store tweets
    dict = {}
    # Create counter to dynamically add keys
    key_counter = 1

    # Use splinter to establish browswer route
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', headless=False)

    # Loop through requested urls and scrape each for most recent tweet
    for url in url_list:
        browser.visit(url)

        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        
        tweet = soup.find('div',class_= 'stream-container').find('div', class_='stream').find('li', class_='js-stream-item stream-item stream-item').find('div', class_= 'content').find('div', class_= 'js-tweet-text-container').find('p').get_text()
        time.sleep(1.5)
        dict['url'+str(key_counter)] = tweet
        # dict.append({'url'+str(key_counter): tweet})
        key_counter = key_counter + 1
            
    return dict






