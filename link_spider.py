from bs4 import BeautifulSoup
import requests

PAGE_LIST = [
    'http://mini-ielts.com/reading'
]
PAGE_COUNT = 33

for i in range(2, PAGE_COUNT + 1):
    PAGE_LIST.append('http://mini-ielts.com/reading?page=' + str(i))

for page in PAGE_LIST:
    html_text = requests.get(page).text

    soup = BeautifulSoup(html_text, 'lxml')
    controlers = soup.find_all('div', class_='list-item-control')
    with open('links.txt', 'a') as f:
        for controler in controlers:
            link = controler.find('a', class_='btn btn-primary')['href']
            link = 'http://mini-ielts.com' + link
            f.write(f'{link}\n')
