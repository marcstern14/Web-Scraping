from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com/2020/06/30/science/kentucky-elk-wildlife-coal.html'

response = requests.get(url)
text = response.text

soup = BeautifulSoup(response.text, 'html.parser')

title_find = soup.find('meta', {'property': 'og:title'})
title = title_find['content']

byl = soup.find('meta', {'name': 'byl'})
byline = byl['content']

date_find = soup.find('meta', {'name': 'pdate'})
date = date_find['content']
date_format = f'{date[:4]}/{date[4:6]}/{date[6:]}'

all_p = soup.find_all('p', class_="css-158dogj evys1bk0")

print(f'Article Title: {title}\n\n'
      f'Byline: {byline}\n\n'
      f'Date: {date_format}\n')

for line in all_p:
    print(line.text)


