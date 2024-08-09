from bs4 import BeautifulSoup
import requests
from datetime import datetime
import random
import time


class HTTPRequest:
    def __init__(self, url):
        self.url = url
        self.headers = self.generate_header() # Identification string sent with the network request
        self.soup = self.get_soup()

    def random_user_agent(self):
        with open('list-common-user-agents.txt', 'r') as ua_file:
            user_agents = ua_file.readlines()
        user_agents = [agent.strip() for agent in user_agents]
        return random.choice(user_agents)

    def generate_header(self):
        return {
            'User-Agent': self.random_user_agent(), # Browser and user software
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', # Content type that user is able to accept
            'Accept-Language': 'en-GB,en;q=0.5',
            'Accept-Encoding': 'gzip', # Compresing algorythm
            'DNT': '1', # Do Not Track
            'Connection': 'close', # If network connection stays open after the current transaction finishes
            'Referer': 'https://google.com'
        }

    def get_soup(self):
        response = requests.get(self.url, headers=self.headers)

        if response.status_code != 200:
            raise Exception(f'{response.status_code} - Error connecting to the url provided.')

        return BeautifulSoup(response.content, 'html.parser')

class WebScraping:

    def __init__(self, url_list):
        self.url_list = url_list
        self.web_scraping_results = []
        self.index = 1
    
    def get_results(self):
        for url in self.url_list:

            if 'amazon' in url.lower():
                scraper = AmazonWebScraper(url)
                title, price, currency = scraper.get_all()
                if title is None or price is None or currency is None:
                    continue
        
            else:
                print(f'The app currently only supports Amazon URLs. The following url could not be scraped: {url}')
                continue
            
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

            url_results = (self.index, title, currency, price, timestamp, url)
            self.web_scraping_results.append(url_results)
            
            if self.index % 25 == 0: # Adding a pause every bunch of requests
                time.sleep(2)

            self.index += 1
             
    def print_results(self):
        self.get_results()
        for result in self.web_scraping_results:
            print(result)

class AmazonWebScraper(WebScraping):
    def __init__(self, url):
        self.url = url
        self.soup = HTTPRequest(self.url).soup

    def get_all(self):
        title = self.get_title()
        price, currency = self.get_price()
        return title, price, currency

    def get_title(self):
        return self.soup.find(id='productTitle').get_text().strip()

    def get_price(self):
        try:
            price_whole = self.soup.find('span', class_ = 'a-price-whole').get_text(strip=True)
            price_decimal = self.soup.find('span', class_ = 'a-price-fraction').get_text(strip=True)
            currency = self.soup.find('span', class_ = 'a-price-symbol').text

        except AttributeError:
            print(f'Error loading price for {self.url}.')
            return None, None
        
        else:
            price_comb = price_whole + price_decimal
            price = price_comb.replace(',','.') # Uniformize prices formatting in other language to EN number convention
        
        return price, currency


# Variable url would come as an input from the FE side, hard-coded for testing
url_list = [
    'https://www.amazon.es/Loop-Tap%C3%B3n-O%C3%ADdos-Reducci%C3%B3n-Ruido/dp/B08TCH6CVB/ref=sr_1_5?sr=8-5',
    'https://www.amazon.co.uk/Molblly-Breathable-Resistant-Skin-friendly-135x190x20cm/dp/B07YV84PTM',
    'https://www.amazon.co.uk/UNO-W2087-Card-Game-European/dp/B005I5M2F8/ref=sr_1_4?c=ts&s=kids&sr=1-4&ts_id=364147031'
    ]
ws = WebScraping(url_list)
ws.print_results()


''' WEBSCRAPING STEPS
    Input needed: variable url_list (from FE (user interaction) or from DB as a dialy trigger)
    Step 1: parse through each url and get its content (BeautifulSoup) passing header details with random user-agent                    class HTTPRequest
    Step 2: webscrape data first checking website is supported (Amazon only initially)                                                  class WebScraping & AmazonWebScraper
    Step 3: save id, title, price, currency, timestamp from each url as a tuple in a list
    Next action: send WS results to DB and/or print nicely to user
'''

'''
PENDING
-testing of different URLs list
-test error handling

NEXT LEVEL 
- add other websites - Argos
'''