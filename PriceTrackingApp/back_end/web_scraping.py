from bs4 import BeautifulSoup
import requests
from datetime import datetime
import random
import time


class HTTPRequest:
    def __init__(self, url, logger):
        self.url = url
        self.headers = self.generate_header() # Identification string sent with the network request
        self.soup = self.get_soup()
        self.logger = logger

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
            self.logger.write_log(f'Error connecting to the url - ERROR: {response.status_code} - URL: {url}')
            raise Exception(f"""{response.status_code} - Error connecting to the url provided.
----------------------------------------------------------------
""")

        return BeautifulSoup(response.content, 'html.parser')

class Logger: #to keep logs of errors, disabled to users per default

    def __init__(self,timestamp, enabled=False):
        self.enabled = enabled
        self.log_filename = timestamp + '.txt' #records info retrieved from page content
        self.debug_log_filename = timestamp + '_debug.txt' #records page content 

    def __write(self, filename, msg):
        if self.enabled:
            with open('logs/' + filename, 'a', encoding="utf-8") as log_file:
                log_file.write(msg)

    def write_log(self, msg):
        self.__write(self.log_filename, msg)
    
    def write_debug_log(self, msg):
        self.__write(self.debug_log_filename, msg)

class WebScraping:

    def __init__(self, url_list):
        self.logger = Logger(timestamp=datetime.now().strftime("%Y-%m-%d %H-%M")) #add 'enabled=True' as parameter to debug and create error log
        self.url_list = url_list
        self.web_scraping_results = []

    def get_product_data(self):
        index = 1
        for url in self.url_list:

            if 'amazon' in url.lower():
                scraper = AmazonWebScraper(url, self.logger)
                title, price, currency = scraper.get_all()
                if title is None or price is None or currency is None:
                    self.logger.write_log(f"""WebScraping.get_products_data - Information could not be retrieved.
URL: {url}, TITLE: {title}, PRICE: {price}, CURRENCY: {currency}
----------------------------------------------------------------
""")
                    self.logger.write_debug_log(f"""URL: {url}
PAGE CONTENT: 
{scraper.soup}
----------------------------------------------------------------
""")
                    continue
        
            else:
                self.logger.write_log(f"""Website not supported - URL: {url}
----------------------------------------------------------------
""")
                print(f'The app currently only supports Amazon URLs. The following url could not be scraped: {url}')
                continue
            
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

            url_results = {'title': title, 'currency': currency, 'price': price, 'timestamp': timestamp, 'url': url}
            self.web_scraping_results.append(url_results)
            
            if index % 25 == 0: # Adding a pause every bunch of requests
                time.sleep(5)

            index += 1
        return self.web_scraping_results
             
    def print_results(self):
        self.get_updated_data()
        for result in self.web_scraping_results:
            print(result)

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
            title = self.soup.find(id='productTitle').get_text().strip()
        except AttributeError:
            print(f'Error loading title for {self.url}.')
            return None
        return title

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
    'https://www.amazon.es/WYBOT-Limpiafondos-Piscina-Inal%C3%A1mbrico-planificaci%C3%B3n/dp/B0CLH4Q6SR',
    'https://www.amazon.co.uk/Windy-Seamless-Ultra-Ultra-Thin-Comfort/dp/B0D6RR2661/ref=zg_bsnr_c_fashion_d_sccl_1/258-6243987-5478100?psc=1',
    'https://www.amazon.co.uk/Pritt-Child-Friendly-Activities-Strong-Hold-adhesive/dp/B004QFI99Y/ref=zg_bs_c_kitchen_d_sccl_4/258-6243987-5478100?psc=1',
    'https://www.argos.co.uk/product/8245757?clickCSR=slp:cannedSearch'
    ]

if __name__ == "__main__":
    ws = WebScraping(url_list)
    web_scraping_results = ws.get_product_data()
    print(web_scraping_results)