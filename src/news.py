import requests
from bs4 import BeautifulSoup

class Nnews:
    def newspull(self):
        self.coin = input("Please input the name of coin in LOWERCASE and WITHOUT ERRORS: ")
        url = "https://coinmarketcap.com/ru/currencies/"+self.coin+"/news/"
        site = requests.get(url)
        soup = BeautifulSoup(site.text, 'html.parser')
        title = soup.find("meta", property="og:image")
        st = title['content']
        coinid = st.rpartition('/')[2].rpartition('.')[0]
        ll = requests.get('https://api.coinmarketcap.com/content/v3/news?coins='+coinid+'&page=1&size=20')
        data = ll.json()
        for x in range(20):
            print(data.get('data')[x].get('meta').get('title')+": ")
            newsurl = data.get('data')[x].get('meta').get('sourceUrl')
            print(newsurl)
            newspage = requests.get(newsurl)
            soup2 = BeautifulSoup(newspage.text, 'html.parser')
            try:
                news = soup2.findAll('p', limit=None)
                newlen = len(news)
                for x in range(newlen):
                    print(news[x].text)
                print('\n')
            except: AttributeError