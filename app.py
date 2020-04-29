from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def index():
  

    return render_template('index.html')

@app.route('/bbc')
def bbcNews():
    newsapi = NewsApiClient(api_key='3bf0db982cf4456b88151b7d2546f619')
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")

    articles = topheadlines['articles']

    pubAt = []
    author = []
    news = []
    desc = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        pubAt.append(myarticles['publishedAt'])
        author.append(myarticles['author'])
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        url.append(myarticles['url'])

    mylist = zip(pubAt, author, news, desc, url)
    

    return render_template('bbc.html', context = mylist)


@app.route('/fox')
def foxNews():
    newsapi = NewsApiClient(api_key='3bf0db982cf4456b88151b7d2546f619')
    topheadlines = newsapi.get_top_headlines(sources="fox-news")

    articles = topheadlines['articles']

    pubAt = []
    author = []
    news = []
    desc = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        pubAt.append(myarticles['publishedAt'])
        author.append(myarticles['author'])
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        url.append(myarticles['url'])

    mylist = zip(pubAt, author, news, desc, url)
    

    return render_template('fox.html', context = mylist)

@app.route('/cnn')
def cnnNews():
    newsapi = NewsApiClient(api_key='3bf0db982cf4456b88151b7d2546f619')
    topheadlines = newsapi.get_top_headlines(sources="cnn")

    articles = topheadlines['articles']

    pubAt = []
    author = []
    news = []
    desc = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        pubAt.append(myarticles['publishedAt'])
        author.append(myarticles['author'])
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        url.append(myarticles['url'])

    mylist = zip(pubAt, author, news, desc, url)
    

    return render_template('cnn.html', context = mylist)

@app.route('/mtv')
def mtvNews():
    newsapi = NewsApiClient(api_key='3bf0db982cf4456b88151b7d2546f619')
    topheadlines = newsapi.get_top_headlines(sources="mtv-news")

    articles = topheadlines['articles']

    pubAt = []
    author = []
    news = []
    desc = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        pubAt.append(myarticles['publishedAt'])
        author.append(myarticles['author'])
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        url.append(myarticles['url'])

    mylist = zip(pubAt, author, news, desc, url)
    

    return render_template('mtv.html', context = mylist)

if __name__ == '__main__':
    app.run(debug=True)