#! python3

import bs4, requests, re
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }

class watch:
    def __init__(self, url):
        self.url = url
        res = requests.get(url, headers=headers)
        
        try:
            res.raise_for_status()
        except:
            raise Exception('Either my program sucks or the provided url is invalid ¯\_(ツ)_/¯')

        self.soup = bs4.BeautifulSoup(res.text, 'html.parser')
        #self.results = []
        self.getResults()

    def getResults(self):
        self.listings = []
        #self.results = self.soup.select('#sortable-results > ul')
        self.results = self.soup.select('#sortable-results > ul')[0].findAll('li')
        for item in self.results:
            self.listings.append(listing(item))
        print(self.listings[0].__dir__())
        #print(self.results[0])#.text.strip())
        #print()
        #this gets the link to the post
        #print(self.results[0].find('a')['href'])
        #print(self.results[0].find('a').find('span').text.strip())
        #print(type(self.results[0]))

class listing(bs4.element.Tag):
    def __init__(self, result):
        #super(bs4.element.Tag, self).__init__()
        pass
    def test(self):
        pass

#sortable-results > ul > li:nth-child(1)

watch('https://nh.craigslist.org/search/sss?sort=rel&query=boat')
