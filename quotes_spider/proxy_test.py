import requests 
from requests.auth import HTTPProxyAuth

url = "http://quotes.toscrape.com" 

proxies = { 
        "http": "http://256acc8ba0d94d52878a8f146b01b2f2:@proxy.crawlera.com:8011/",
        "https": "http://256acc8ba0d94d52878a8f146b01b2f2:@proxy.crawlera.com:8011/"
} 

r = requests.get(url, proxies=proxies, verify=False)
print(r)