from bs4 import BeautifulSoup
import requests

#Variable url would come as an input from the FE side, hard-coded for testing
url= 'https://www.amazon.co.uk/LG-LED-LQ63-32-Smart/dp/B0D17VJPSD?ref_=Oct_d_otopr_d_560864_0&pd_rd_i=B09SKR4QD9'

#browser information - amend 'User_Agent' according to your browser (google 'my user agent')
browser_header = {
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip', 
    'DNT': '1', # Do Not Track Request Header 
    'Connection': 'close'
    }

def get_price(page_content):
    try:
        price_whole = page_content.find('span', class_ = 'a-price-whole').get_text(strip=True)
        price_decimal = page_content.find('span', class_ = 'a-price-fraction').get_text(strip=True)
        #store currency to display it to the user
        currency = page_content.find('span', class_ = 'a-price-symbol').text
    except:
        print('Error loading price.')
    else:
        price = price_whole + price_decimal
        #In case price is showing with a comma (searching Amazon ES, for example), convert to EN number convention
        price = price.replace(',','.')
    return price, currency

response = requests.get(url, headers=browser_header)

try: 
    if response.status_code != 200:
        raise Exception
except:
    print(str(response.status_code) + ' - Error connecting to the url provided.')
else:
    page_content = BeautifulSoup(response.content, 'html.parser') #lxml

    product_title = page_content.find(id='productTitle').get_text()
    print(f'Product: {product_title.strip()}')

    price, currency = get_price(page_content)
    print(f'Price: {currency + price}')

''' 
ISSUES
Incorrect pricing in following products: 
https://www.amazon.co.uk/Ends-Us-Colleen-Hoover/dp/1471156265/ref=sr_1_1?s=books&sr=1-1
https://www.amazon.co.uk/Windy-Seamless-Ultra-Ultra-Thin-Comfort/dp/B0D6RR2661/ref=zg_bsnr_c_fashion_d_sccl_1/258-6243987-5478100?pd_rd_i=B0D6RR2661&psc=1
https://www.amazon.co.uk/coskefy-Underwear-Waisted-Knickers-Stretchy/dp/B0BRK8YHMC?pd_rd_i=B0BRK8YHMC&ref_=oct_dx_dotd_B0BRK8YHMC
'''

#get price under title
    # price = page_content.select_one('span.a-price').select_one('span.a-offscreen')
    # print(price.text)