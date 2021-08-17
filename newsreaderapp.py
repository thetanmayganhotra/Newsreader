from urllib.request import urlopen

import nltk


from newspaper import Article

ans = input("APNA_KHABRI \n\n"
            "1. TELL ME THE LATEST NEWS \n"
      "2. I'LL CHOOSE THE NEWS CATEGORY \n")

if ans == '1':
    site = 'https://news.google.com/news/rss'


elif ans == '2':
    cat = input("Select NEWS category \n"
                "1.INDIA \n"
                "2.WORLD \n"
                "3.LOCAL NEWS \n"
                "4.BUSINESS \n"
                "5.TECHNOLOGY \n"
                "6.ENTERTAINMENT \n"
                "7.SPORTS  \n"
                "8.SCIENCE \n"
                "9.HEALTH \n"
                )
    rsslink = {"1":"https://rss.app/feeds/pTuVCcCNCF4wBjbF.xml",
               "2":"https://rss.app/feeds/H5lD8qkEQznWfNbz.xml",
               "3":"https://rss.app/feeds/rJmdyeHncaKl8dmg.xml",
               "4":"https://rss.app/feeds/efN7WWPr4NJ4rJei.xml",
               "5":"https://rss.app/feeds/gclQFGUJi2Ih5x5I.xml",
               "6":"https://rss.app/feeds/y7C1gyRTLRP8za39.xml",
               "7":"https://rss.app/feeds/WzrWoLHguaKwg5ml.xml",
               "8":"https://rss.app/feeds/bdCyfknNQkfOa1jf.xml",
               "9":"https://rss.app/feeds/S6toNW5WLm61UDnN.xml"}

    site = rsslink.get(cat)

else:
    print("wrong input")


# webscrapping the rss feed

from bs4 import BeautifulSoup as soup

import os

op = urlopen(site)  # Open that site

rd = op.read()  # read data from site

op.close()  # close the object

sp_page = soup(rd, 'xml')  # scrapping data from site

news_list = sp_page.find_all('item')  # finding news



from gtts import gTTS

for news in news_list:

    print(news.title.text)
    url = news.link.text



    article = Article(url)
    article.download()
    article.parse()

    article.nlp()
    print(article.summary)

    mytext = article.summary



    language = 'en'
    output = gTTS(text=mytext, lang=language, slow=False)
    output.save('latestnews.mp3')
    os.system('start latestnews.mp3')

    com = input("do you want hear the next news(y/n)")
    if com == 'y':
        continue
    elif com == 'n':
        break
    else:
        print("wrong input")


