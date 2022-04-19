"""Installs"""
pip install selenium
pip install msedge-selenium-tools==3.141.3

"""Import Libraries"""
import csv
from bs4 import BeautifulSoup
from selenium import webdriver # Firefox & Chrome
from msedge.selenium_tools import Edge, EdgeOptions # Edge

"""Initialize Webdriver"""

edge_options = EdgeOptions()
edge_options.use_chromium = True # Make edge headless

chrome_driver = webdriver.Chrome()
firefox_driver = webdriver.Firefox()
edge_driver = Edge(options=edge_options)

"""Run Link Using Webdriver"""

url = https://www.amazon.com

#edge_driver.get(url)
chrome_driver.get(url)
#firefox_drive.get(url)

"""Run for Chrome """

import csv
from bs4 import BeautifulSoup
from selenium import webdriver # Firefox & Chrome

def get_url(search_term):
  # Generate a url from search term
  search_term = search_term.replace(' ', '+')
  template = 'https://www.amazon.pl/s?k={}&ref=nb_sb_noss'
  url = template.format(search_term)
  url += '&page={}'

  return url

item = results[0]

def extract_record(item):
  atag = item.h2.a
  description = atag.text.strip()
  url = 'https://www.amazon.com'+ atag.get('href')

  try:
    price_parent = item.find('span', 'a-price')
    price = price_parent.find('span', 'a-offscreen').text
  except:
    price_parent = ''
    price = ''

  try:
    rating = item.i.text
    review_count = item.find('span', {'class': 'a-size-base', 'dir': 'auto'}).text
  except:
    rating = ''
    review_count = ''

  result = (description, price, rating, review_count, url)

  return result

def main(search_term):
  chrome_driver = webdriver.Chrome()
  records = []
  url = get_url(search_term)
  for page in range(1, 21):
    driver.get(url.format(page))
    soup = BeautifulSoup(chrome_driver, page_source, 'html.parser')

    results = soup.find_all('div', {'data-component-type': 's-search-result'})
    for item in results:
      record = extract_record(item)
      if record:
        records.append(record)
  chrome_driver.close()

  with open('scrapped_dataset.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Description', 'Price', 'Rating', 'Url'])
    writer.writerows(records)

main('Monitor')