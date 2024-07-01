from django.shortcuts import render
import requests


def article_list(req):
    # url = 'https://i.news.qq.com/web_feed/getCommandArea'
    url = "https://i.news.qq.com/gw/event/pc_hot_ranking_list?ids_hash=&offset=0&page_size=50&appver=15.5_qqnews_7.1.60&rank_id=hot"

    headers = {
        "referer": "https://news.qq.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers).json()

    # articles = response["data"]
    articles = response["idlist"][0]["newslist"][1:]
    # print(articles)

    return render(req, "article_list.html",context={
        "articles": articles
    })
