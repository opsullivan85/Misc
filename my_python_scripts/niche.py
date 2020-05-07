#! python3

import bs4, requests, re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }

class college(object):
    
    basic_selectors = {
        'Acceptance Rate':'#admissions > div.profile__buckets > div.profile__bucket--2 > div > div > div > div.scalar__value > span',
        'Enrolled Students':'#students > div.profile__buckets > div.profile__bucket--1 > div > div > div.scalar > div.scalar__value > span:nth-child(1)',
        'Overall Niche Grade':'#report-card > div > div.report-card > div > div.profile__bucket--1 > div > div > div > div.overall-grade__niche-grade > div'
        }

    list_selectors = {
        'Popular Majors':[3, '#majors > div.profile__buckets > div.profile__bucket--1 > div > div > div > div.toggle__content--profiles--hidden > ul > li:nth-child({}) > div > h6']
                            ###majors > div.profile__buckets > div.profile__bucket--1 > div > div > div > div.toggle__content--profiles-visible--hidden > ul > li:nth-child(1) > div > h6
        }
    
    def __init__(self, name):
        self.name = name
        self._name = re.sub(r'[^a-zA-Z ]', '', name).lower().replace(' ','-')
        res = requests.get('https://www.niche.com/colleges/{}/'.format(self._name), headers=headers)
        
        try:
            res.raise_for_status()
        except:
            raise Exception(f'No College Named {name} was found. Make sure the full name is used.')

        self.soup = bs4.BeautifulSoup(res.text, 'html.parser')
        self.info = {}
        self.crawl()

    def crawl(self):
        for selector in college.basic_selectors:
            self.info[selector] = self.soup.select(college.basic_selectors[selector])[0].text.strip()

        for selector in college.list_selectors:
            try:
                self.info[selector] = '\n    '+',\n    '.join(self.soup.select(college.list_selectors[selector][1].format(x+1))[0].text.strip() for x in range(college.list_selectors[selector][0]))
            except:
                pass
            

    def __str__(self):
        s = self.name + ':\n  '
        s += '\n  '.join(['%s: %s' % (key, value) for (key, value) in self.info.items()])#'\n '.join(self.info)
        return s+'\n'

print(college('Worcester Polytechnic Institute'))
print(college('Massachusetts Institute of Technology'))
print(college('Franklin W. Olin College of Engineering'))
#majors > div.profile__buckets > div.profile__bucket--1 > div > div > div > div.toggle__content--profiles--hidden > ul > li:nth-child(1)
#majors > div.profile__buckets > div.profile__bucket--1 > div > div > div > div.toggle__content--profiles--hidden > ul > li:nth-child(2)
#majors > div.profile__buckets > div.profile__bucket--1 > div > div > div > div.toggle__content--profiles-visible--hidden > ul > li:nth-child(1) > div > h6
