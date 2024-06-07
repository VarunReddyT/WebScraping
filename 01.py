import requests
from bs4 import BeautifulSoup
import csv
import time

url = 'https://www.bbc.com/news'

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')

timestamp = time.strftime("_%H_%M_%S")

with open('headlines'+timestamp+'.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline', 'URL'])
    for tag in soup.find_all('h2'):
        headline = tag.text.strip()
        parent = tag
        while parent.name != 'body': 
            parent = parent.parent
            link = parent.find('a', href=True)
            if link:
                headline_url = link['href']
                if not headline_url.startswith('http'):
                    headline_url = 'https://www.bbc.com' + headline_url
                writer.writerow([headline, headline_url])
                break
