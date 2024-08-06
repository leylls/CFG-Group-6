from bs4 import BeautifulSoup
import requests
import datetime
import random

#Variable url would come as an input from the FE side, hard-coded for testing
#for cron job, would it be passed a url list? create for loop and introduce 'time.sleep' function
url_list= [
    'https://www.amazon.co.uk/dp/B0BL6GJVZS',
    'https://www.amazon.co.uk/eero-pro-mesh-wi-fi-system/dp/B07WFJCSYX',
    'https://www.amazon.co.uk/Court-Thorns-Roses-Sarah-Maas/dp/1526605392?ref_=Oct_d_oup_d_266239_2&pd_rd_i=1526605392',
    'https://www.amazon.co.uk/Ends-Us-Colleen-Hoover/dp/1471156265/',
    'https://www.amazon.com/Mighty-Patch-Hydrocolloid-Absorbing-count/dp/B074PVTPBW',
    'https://www.amazon.com/HP-Single-3200MHz-Laptop-Memory/dp/B0948X9C9N/ref=sr_1_3?sr=8-3'
    ]

#get random user-agent info from txt file to prevent from getting blocked while web scraping
def get_random_user_agent():
    with open('list-common-user-agents.txt','r') as ua_file:
        user_agents = ua_file.readlines()
    user_agents = [agent.strip() for agent in user_agents]
    return random.choice(user_agents)

random_user_agent = get_random_user_agent()

#identification string sent with the network request
headers = { 
    'User_Agent': random_user_agent, #browser and user software
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', #content type that user is able to accept
    'Accept-Language': 'en-GB,en;q=0.5',
    'Accept-Encoding': 'gzip', #compresing algorythm
    'DNT': '1', # Do Not Track
    'Connection': 'close', #if network connection stays open after the current transaction finishes
    'Referer': 'https://google.com'
    }

def get_price(page_content):
    try:
        price_whole = page_content.find('span', class_ = 'a-price-whole').get_text(strip=True)
        price_decimal = page_content.find('span', class_ = 'a-price-fraction').get_text(strip=True)
        #store currency to display it to the user
        currency = page_content.find('span', class_ = 'a-price-symbol').text

    except:
        raise ValueError('Error loading price.')
    
    else:
        price = price_whole + price_decimal
        #In case price is showing with a comma (searching Amazon ES, for example), convert to EN number convention
        price = price.replace(',','.')
    
    return price, currency

def webscraper(url):
    response = requests.get(url, headers=headers)

    try: 
        if response.status_code != 200:
            raise Exception
    except:
        print(str(response.status_code) + ' - Error connecting to the url provided.')
    else:
        soup = BeautifulSoup(response.content, 'html.parser') #lxml

        title = soup.find(id='productTitle').get_text().strip()
        price, currency = get_price(soup)
        timestamp = datetime.datetime.now()
        formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M")

    return title,price,currency,formatted_timestamp

web_scraping_results = []
index = 1
for url in url_list:
    title,currency,price,timestamp = webscraper(url)
    results = (index,title,currency,price,timestamp,url)
    web_scraping_results.insert(index,results)
    # print(id)
    # print(f'Product: {title}')
    # print(f'Price: {currency + price}')
    # print(timestamp)
    index += 1

for result in web_scraping_results:
    print(result)

''' 
ISSUES
Incorrect pricing in following products: 

https://www.amazon.es/LYCZMKSF-Seamless-Ultra-Thin-Comfort-2X-Large/dp/B0D6RQYD5M
https://www.amazon.co.uk/coskefy-Underwear-Waisted-Knickers-Stretchy/dp/B0BRK8YHMC?pd_rd_i=B0BRK8YHMC&ref_=oct_dx_dotd_B0BRK8YHMC
https://www.amazon.co.uk/Tomorrow-best-books-ever-GREEN-ebook/dp/B09LH8HSXJ?ref_=Oct_d_oup_d_266239_1&pd_rd_i=B09LH8HSXJ
'''

#Argos