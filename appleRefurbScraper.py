# coding:utf-8

import pprint
import requests
from bs4 import BeautifulSoup

domain = 'https://www.apple.com/shop/refurbished/'
scrapList = ['mac', 'ipad', 'iphone', 'watch', 'ipod', 'appletv', 'clearance', 'accessories']
#domain = 'https://www.apple.com/jp/shop/refurbished/'
#scrapList = ['mac', 'ipad', 'watch', 'ipod', 'appletv', 'accessories', 'clearance']
listClass = 'refurbished-category-grid-no-js'
listTag = 'li'
nameTag = 'a'
priceTag = 'div'

def appleRefurbScraper(req):
  items = []
  soup = BeautifulSoup(req.text, 'html.parser')
  productList = soup.find('div', class_=listClass)
  for item in productList.find_all(listTag):
    name = item.find(nameTag).text.strip()
    price = item.find(priceTag).text.strip()
    items.append([name, price])
  return items

def writeData(name, str):
  f = open(name, 'w')
  f.write(str)
  f.close()

def main():
  try:
    print('start scraper!')
    for name in scrapList:
      req = requests.get(domain+name) # download HP data
      writeData('cache.'+name+'.html', req.text) # save HP data
      items = appleRefurbScraper(req) # scrape
      print(name)
      pprint.pprint(items, width=200) # print name, price
    print('end scraper!')
  except:
    print('error scrapper!')

if __name__ == "__main__":
  main()
