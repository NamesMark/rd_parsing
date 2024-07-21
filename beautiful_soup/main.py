import os
import requests
import json
import html
from pprint import pprint
from bs4 import BeautifulSoup

main_pref = 'https://www.bbc.com'
main_url = main_pref + '/sport'

def get_page(url):
    sanitized_url = url
    if "://" in url:
        sanitized_url = sanitized_url.split('://')[1]
    sanitized_url = sanitized_url.replace('/', '-')

    filename = sanitized_url + '.html'

    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        return content

    response = requests.get(
        url=url,
    )
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(response.text)
    return response.text

def save_json(data):
        pprint(data)
        with open(main_url.split('://')[1].replace('/', '-') + '.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

def get_articles(html, limit):
    soup = BeautifulSoup(html, features='lxml')
    promo_links = soup.find_all('a', class_=lambda x: x and 'PromoLink' in x)
    #print(promo_links)

    articles = []

    for link in promo_links[:limit]:
        headline_tag = link.find('p', class_=lambda x: x and 'PromoHeadline' in x) 
        if headline_tag:
            headline = headline_tag.text
            url = main_pref + link['href']
            articles.append({'title': headline, 'url': url})

    return articles

def extract_related(html):
    soup = BeautifulSoup(html, features='lxml')
    related_block = soup.find('h2', text=lambda text: text and 'Related Topics' in text)

    topics = []
    if related_block:
        topic_list = related_block.find_next('ul')
        if topic_list:
            for link in topic_list.find_all('a'):
                topics.append(link.text.strip()) 

    return topics

if __name__ == '__main__':
    page_html = get_page(main_url)
    articles = get_articles(page_html, 10)
    # print(articles)
    # print(len(articles))

    articles_url_topic = []

    for article in articles:
        url = article.get('url')
        article_html = get_page(url)
        related = extract_related(article_html)
        articles_url_topic.append({'Link': url, 'Topics': related})

    # print(articles_url_topic)

    articles_url_topic = [article for article in articles_url_topic if article.get('Topics')][:5]

    save_json(articles_url_topic)