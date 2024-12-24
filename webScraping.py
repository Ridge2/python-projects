import requests
from bs4 import BeautifulSoup

url =  "https://www.clcoding.com/"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
links = soup.find_all('a')
for link in links: 
    print(link.get('href'))