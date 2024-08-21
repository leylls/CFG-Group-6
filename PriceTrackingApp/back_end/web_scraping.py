from bs4 import BeautifulSoup
import requests
from datetime import datetime
import random
import time
import os


class HTTPRequest:
    def __init__(self, url, logger):
        self.url = url
        self.headers = self.generate_header() # Identification string sent with the network request
        self.logger = logger
        self.soup = self.get_soup()

    def random_user_agent(self):
        a = os.path.dirname(__file__)
        with open(a + '/list_common_user_agents.txt', 'r') as ua_file:
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
            self.logger.write_log(f"""
Error connecting to the url - ERROR: {response.status_code} - URL: {self.url}')
----------------------------------------------------------------
""")
            return None

        return BeautifulSoup(response.content, 'html.parser')

class Logger: 

    def __init__(self,timestamp, enabled = True):
        self.enabled = enabled
        self.log_filename = timestamp + '.txt' #records info retrieved from page content
        self.debug_log_filename = timestamp + '_debug.txt' #records page content 

    def __write(self, filename, msg):
        if self.enabled:
            with open('back_end/logs/' + filename, 'a', encoding="utf-8") as log_file:
                log_file.write(msg)

    def write_log(self, msg):
        self.__write(self.log_filename, msg)
    
    def write_debug_log(self, msg):
        self.__write(self.debug_log_filename, msg)

class WebScraping:

    def __init__(self, url_list):
        self.logger = Logger(timestamp=datetime.now().strftime("%Y-%m-%d %H-%M"))
        self.url_list = url_list
        self.web_scraping_results = []

    def get_product_data(self):
        index = 1
        for url in self.url_list:

            if 'amazon' in url.lower() or 'evapchiri' in url.lower():   #added evapchiri to include our mock wesite
                scraper = AmazonWebScraper(url, self.logger)
                title, price, currency = scraper.get_all()
                if title is None or price is None or currency is None:
                    self.logger.write_log(f"""
WebScraping.get_products_data - Information could not be retrieved.
URL: {url}, TITLE: {title}, PRICE: {price}, CURRENCY: {currency}
----------------------------------------------------------------
""")
                    self.logger.write_debug_log(f"""
URL: {url}
PAGE CONTENT: 
{scraper.soup}
----------------------------------------------------------------
""")
                    continue
        
            else:
                self.logger.write_log(f"""
Website not supported - URL: {url}
----------------------------------------------------------------
""")
                continue
            
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

            url_results = {'title': title, 'currency': currency, 'price': price, 'timestamp': timestamp, 'url': url}
            self.web_scraping_results.append(url_results)
            
            if index % 25 == 0: # Adding a pause every bunch of requests
                time.sleep(5)

            index += 1
        return self.web_scraping_results

class AmazonWebScraper(WebScraping):
    def __init__(self, url, logger):
        self.url = url
        self.logger = logger
        self.soup = HTTPRequest(self.url, self.logger).soup

    def get_all(self):
        title = self.get_title()
        price, currency = self.get_price()
        return title, price, currency

    def get_title(self):
        try:
            if self.soup is None:
                return None
            title = self.soup.find(id='productTitle').get_text().strip()
        except AttributeError:
            return None
        return title

    def get_price(self):
        try:
            if self.soup is None:
                return None, None
            price_whole = self.soup.find('span', class_ = 'a-price-whole').get_text(strip = True)
            price_decimal = self.soup.find('span', class_ = 'a-price-fraction').get_text(strip = True)
            currency = self.soup.find('span', class_ = 'a-price-symbol').text

        except AttributeError:
            return None, None
        
        else:
            price_comb = price_whole + price_decimal
            price = price_comb.replace(',','.') # Uniformize prices formatting in other language to EN number convention
        
        return price, currency


# if __name__ == "__main__":
#     ws = WebScraping(['https://evapchiri.github.io/test_websiteCFG/'])
#     ws_results_FE = ws.get_product_data()
#     print(ws_results_FE)