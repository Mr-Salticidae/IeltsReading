from bs4 import BeautifulSoup
import requests

with open('links.txt', 'r') as f:
    links = f.readlines()

for link in links:
    link = link[:-1]
    html_text = requests.get(str(link)).text

    soup = BeautifulSoup(html_text, 'lxml')
    article = soup.find('div', class_='reading-text')
    paragraphs = article.find_all('p')
    with open('articles.txt', 'a', encoding='utf-8') as article_file:
        for paragraph in paragraphs:
            content = paragraph.text.strip()
            article_file.write(f'{content}\n')
        article_file.write('\n')
