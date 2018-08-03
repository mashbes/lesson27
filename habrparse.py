import lxml.html as html
from urllib.request import urlopen
import requests
import json

main_domain_stat = 'https://habr.com/'
data = []
main_page = html.parse(urlopen(main_domain_stat)).getroot()

article_links = main_page.xpath(
   '//li/article[contains(@class, "post")]/h2[@class="post__title"]/a[@class="post__title_link"]/@href')

for link in article_links:
    article_page = html.parse(urlopen(link))

    title = article_page.xpath('//article[contains(@class, "post")]/div[@class="post__wrapper"]/h1[contains(@class, "post__title")]/span/text()')

    text = article_page.xpath('//article[contains(@class, "post")]/div[@class="post__wrapper"]/div[contains(@class, "post__body")]/'
                              'div[contains(@class, "post__text")]/text()')

    images = article_page.xpath('//article[contains(@class, "post")]/div[@class="post__wrapper"]/div[contains(@class, "post__body")]/'
                              'div[contains(@class, "post__text")]/img/@src')

    data.append({
        'title': title[0],
        'text' : text,
        'images' : images
    })

    with open('article.json', 'w', encoding='utf-8') as jdata:
        json.dump(data, jdata, sort_keys=True, indent=4, ensure_ascii=False)



