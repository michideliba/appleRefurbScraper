# coding:utf-8

import pprint
import requests
from bs4 import BeautifulSoup

# for US setting
domain = 'https://www.apple.com/shop/refurbished/'
scrapList = ['mac', 'ipad', 'iphone', 'watch', 'appletv', 'clearance', 'accessories']

# for JP setting
#domain = 'https://www.apple.com/jp/shop/refurbished/'
#scrapList = ['mac', 'ipad', 'watch', 'appletv', 'accessories', 'clearance']

listClass1 = 'rf-refurb-category-grid-no-js'
listClass2 = 'refurbished-category-grid-no-js'
listTag = 'li'
nameTag = 'a'
priceTag = 'div'

def appleRefurbScraper(req):
  items = []
  soup = BeautifulSoup(req.text, 'html.parser')
  productList = soup.find('div', class_=listClass1)
  if productList == None:
    productList = soup.find('div', class_=listClass2)
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
