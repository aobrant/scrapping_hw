from datetime import datetime
from importlib.resources import contents
from time import time
from urllib import response
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from pprint import pprint

KEYWORDS = ['дизайн', 'фото', 'web', 'python','материал','DevOps']

if __name__ == '__main__':

    ua = UserAgent()
    HEADERS = {'User-Agent':ua.chrome}

    base_url = "https://habr.com"
    url = base_url + "/ru/all/"
    response = requests.get(url, headers=HEADERS)
    text = response.text
    articles_list = []


    soup = BeautifulSoup(text, features="html.parser")
    articles = soup.find_all("article")
    for article in articles:
        a_text = article.find_all(class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
        t_ime = article.find(class_="tm-article-snippet__datetime-published")
        t = t_ime.time
        t= str(t)[48:67]
        title = article.find(class_="tm-article-snippet__title-link").find("span").text
        href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
        a_text = [atext.text.strip() for atext in a_text ]
        a_text.append(t)
        a_text.append(title)
        a_text.append(href)
        articles_list.append(a_text)

    final_list = []
    for i in range(len(articles_list)):
        if len(articles_list[i]):
            for key in KEYWORDS:
                if key in articles_list[i][0]:
                    final_list.append(articles_list[i])
            
    for news in final_list:
        print (f"{news[1]} \n {news[2]} \n {news[0]} \n",'*'*10,'\n')
        

                
        

