import unittest
from unittest import mock
from back_end.web_scraping import *
import os
from datetime import datetime

class TestHTTPRequest(unittest.TestCase):

    @mock.patch('web_scraping.HTTPRequest.generate_header', return_value = None)
    @mock.patch('web_scraping.HTTPRequest.get_soup', return_value = None)
    def test_random_user_agent(self, mocked_soup, mocked_header):
        a = os.path.dirname(__file__)
        file = open(a + "/list_common_user_agents.txt")
        lines = file.readlines()
        file.close()
        ua_list = [ele[:-1] for ele in lines]               #remove line jump at the end of each string in list
        httprequest=HTTPRequest(None, False)
        random_ua = httprequest.random_user_agent()
        self.assertIn(random_ua,ua_list)

    @mock.patch('web_scraping.HTTPRequest.random_user_agent', return_value = 'Mocked User Agent value')
    @mock.patch('web_scraping.HTTPRequest.get_soup', return_value = None)
    def test_generate_header(self, mocked_soup, mocked_ua):
        httprequest=HTTPRequest(None, False)
        header = httprequest.generate_header()
        expected_header = {
            'User-Agent': 'Mocked User Agent value',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language': 'en-GB,en;q=0.5', 
            'Accept-Encoding': 'gzip', 'DNT': '1', 'Connection': 'close', 'Referer': 'https://google.com'
        }
        self.assertTrue('User-Agent' in header.keys())
        self.assertEqual(header['User-Agent'],expected_header['User-Agent'])
        self.assertTrue('Accept' in header.keys())
        self.assertEqual(header['Accept'],expected_header['Accept'])
        self.assertTrue('Accept-Language' in header.keys())
        self.assertEqual(header['Accept-Language'],expected_header['Accept-Language'])
        self.assertTrue('Accept-Encoding' in header.keys())
        self.assertEqual(header['Accept-Encoding'],expected_header['Accept-Encoding'])
        self.assertTrue('DNT' in header.keys())
        self.assertEqual(header['DNT'],expected_header['DNT'])
        self.assertTrue('Connection' in header.keys())
        self.assertEqual(header['Connection'],expected_header['Connection'])
        self.assertTrue('Referer' in header.keys())
        self.assertEqual(header['Referer'],expected_header['Referer'])

    @mock.patch('web_scraping.requests.get')
    def test_get_soup_valid_url_(self, mocked_get):
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.content = '<html><title>TITLE</title></html>'
        mocked_get.return_value = mock_response
        logger = Logger("")
        httprequest = HTTPRequest('https://validurl.com', logger = logger)
        self.assertEqual(httprequest.soup.title.string, 'TITLE')

    @mock.patch('web_scraping.requests.get')
    def test_get_soup_not_valid_url_(self, mocked_get):
        mock_response = mock.Mock()
        mock_response.status_code = 400
        mock_response.content = ''
        mocked_get.return_value = mock_response        
        logger = Logger("")
        httprequest = HTTPRequest('https://invalidurl.com', logger = logger)
        self.assertIsNone(httprequest.soup)

class TestWebScraping(unittest.TestCase):

    @mock.patch('web_scraping.AmazonWebScraper')
    def test_get_product_data_empty_url_list(self, mocked_amazonws):
        ws = WebScraping([])
        res = ws.get_product_data()
        self.assertEqual(res, [])

    @mock.patch('web_scraping.AmazonWebScraper')
    def test_get_product_data_not_supported_sites(self, mocked_amazonws):
        ws = WebScraping(['google.com', 'codefirstgirls.com'])
        res = ws.get_product_data()
        self.assertEqual(res, [])

    @mock.patch('web_scraping.AmazonWebScraper')
    def test_get_product_data_scraper_error_currency(self, mocked_scraper):
        mocked_scaper_class = mocked_scraper.return_value
        mocked_scaper_class.get_all.return_value = ['title', 'price_example', None]
        ws = WebScraping(['amazon.co.uk/example'])
        res = ws.get_product_data()
        self.assertEqual(res, [])

    @mock.patch('web_scraping.AmazonWebScraper')
    def test_get_product_data_scraper_error_title(self, mocked_scraper):
        mocked_scaper_class = mocked_scraper.return_value
        mocked_scaper_class.get_all.return_value = [None, 'price_example', '€']
        ws = WebScraping(['amazon.co.uk/example'])
        res = ws.get_product_data()
        self.assertEqual(res, [])

    @mock.patch('web_scraping.AmazonWebScraper')
    def test_get_product_data_scraper_error_price(self, mocked_scraper):
        mocked_scaper_class = mocked_scraper.return_value
        mocked_scaper_class.get_all.return_value = ['title', None, '€']
        ws = WebScraping(['amazon.co.uk/example'])
        res = ws.get_product_data()
        self.assertEqual(res, [])

    @mock.patch('web_scraping.AmazonWebScraper')
    def test_get_product_data_scraper_success(self, mocked_scraper):
        expected_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        mocked_scaper_class = mocked_scraper.return_value
        mocked_scaper_class.get_all.return_value = ['title', 'price_example', '€']
        ws = WebScraping(['amazon.co.uk/example'])
        res = ws.get_product_data()
        self.assertEqual(res, [{'title': 'title', 'price': 'price_example', 'currency': '€', 'timestamp':expected_timestamp, 'url': 'amazon.co.uk/example'}])

class TestAmazonWebScraper(unittest.TestCase):

    @mock.patch('web_scraping.HTTPRequest')
    def test_get_title_soup_error(self, mocked_request):
        mocked_request.return_value.soup = None
        scraper = AmazonWebScraper('https://www.amazon.com/test', mock.Mock())
        title = scraper.get_title()
        self.assertIsNone(title)

    @mock.patch('web_scraping.HTTPRequest')
    def test_get_title_attribute_error(self, mocked_request):
        html = ''
        soup = BeautifulSoup(html, 'html.parser')
        mocked_request.return_value.soup = soup
        scraper = AmazonWebScraper('https://www.amazon.com/test', mock.Mock())
        title = scraper.get_title()
        self.assertIsNone(title)
    
    @mock.patch('web_scraping.HTTPRequest')
    def test_get_title_success(self, mocked_request):
        html = '<span id="productTitle">Test title</span>'
        soup = BeautifulSoup(html, 'html.parser')
        mocked_request.return_value.soup = soup
        scraper = AmazonWebScraper('https://www.amazon.com/test', mock.Mock())
        title = scraper.get_title()
        self.assertEqual(title, 'Test title')

    @mock.patch('web_scraping.HTTPRequest')
    def test_get_price_soup_error(self, mocked_request):
        mocked_request.return_value.soup = None
        scraper = AmazonWebScraper('https://www.amazon.com/test', mock.Mock())
        price = scraper.get_price()
        self.assertEqual(price, (None, None))

    @mock.patch('web_scraping.HTTPRequest')
    def test_get_price_attribute_erro(self, mocked_request):
        html = ''
        soup = BeautifulSoup(html, 'html.parser')
        mocked_request.return_value.soup = soup
        scraper = AmazonWebScraper('https://www.amazon.com/test', mock.Mock())
        price = scraper.get_price()
        self.assertEqual(price, (None, None))

    @mock.patch('web_scraping.HTTPRequest')
    def test_get_price_success(self, mocked_request):
        html = '''
        <span class="a-price-symbol">$</span>
        <span class="a-price-whole">23</span>
        <span class="a-price-fraction">99</span>
        '''
        soup = BeautifulSoup(html, 'html.parser')
        mocked_request.return_value.soup = soup
        scraper = AmazonWebScraper('https://www.amazon.com/test', mock.Mock())
        price = scraper.get_price()
        self.assertEqual(price, ('2399', '$'))
    
if __name__ == '__main__':
    unittest.main()