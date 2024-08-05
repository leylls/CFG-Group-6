from bs4 import BeautifulSoup
import requests

#Variable url would come as an input from the FE side, hard-coded for testing
url='https://www.amazon.co.uk/Ends-Us-Colleen-Hoover/dp/1471156265/ref=sr_1_1?sr=8-1'

#browser information - amend 'User_Agent' according to your browser (google 'my user agent')
browser_header = {
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip', 
    'DNT': '1', # Do Not Track Request Header 
    'Connection': 'close'
    }

response = requests.get(url, headers=browser_header)

try: 
    if response.status_code != 200:
        raise Exception
except:
    print(str(response.status_code) + ' - Error connecting to the url provided.')
else:
    page_content = BeautifulSoup(response.content, 'html.parser') #lxml

    product_title = page_content.find(id='productTitle').get_text()
    print(product_title.strip())

    price_whole = page_content.find('span', class_ = 'a-price-whole').get_text(strip=True)
    price_decimal = page_content.find('span', class_ = 'a-price-fraction').get_text(strip=True)
    print(price_whole + price_decimal)

    # with open('debug.txt', 'w') as text_file:
    #     text_file.write("{}".format(page_content.contents))
    # product_price = page_content.find(id = 'corePriceDisplay_desktop_feature_div')
    # print(product_price)
    # pp = product_price.find('span', {'class': 'a-price-whole'})
    # print(pp)