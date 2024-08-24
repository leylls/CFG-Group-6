import unittest
from unittest.mock import MagicMock
from back_end.email_api import PriceAlert

class TestPriceAlert(unittest.TestCase):
    def setUp(self):
        self.api_key = 'your_api_key'
        self.api_secret = 'your_secret_key'
        self.sender_email = "group6.cfgdegree24@gmail.com"
        self.price_alert = PriceAlert(self.api_key, self.api_secret, self.sender_email)

    def test_format_price(self):
        self.assertEqual(self.price_alert.format_price(30.00, "£"), "£30.00")
        self.assertEqual(self.price_alert.format_price(10.95, "$"), "$10.95")
        self.assertEqual(self.price_alert.format_price(2.99, "€"), "€2.99")
        self.assertEqual(self.price_alert.format_price(1050.00, "¥"), "¥1050.00")

    def test_send_alert(self):
        mock_client = MagicMock()
        mock_client.send.create.return_value.status_code = 200
        self.price_alert.mailjet = mock_client
        self.price_alert.send_alert("recipienttest6@gmail.com", "Valued Customer", "Example Product", 30.00, 40.00,"https://www.amazon.co.uk/", "£")
        self.assertEqual(mock_client.send.create.call_count, 1)

    def test_create_text_content(self):
        text_content = self.price_alert._create_text_content("Example Product", 30.00, 40.00)
        self.assertIn("The price of Example Product has fallen below your price threshold", text_content)
        self.assertIn("Current price: $30.00", text_content)
        self.assertIn("Your price threshold: $40.00", text_content)

    def test_create_html_content(self):
        html_content = self.price_alert._create_html_content("Valued Customer", "Example Product", 30.00, 40.00, "https://www.amazon.co.uk/","£","recipienttest6@gmail.com")
        #print(html_content) #uncomment line 33 to see actual html content
        self.assertIn("<h1 style=\"color: #1a5f7a; font-size: 24px; margin: 0 0 20px; text-align: center;\">Price Alert</h1>", html_content)
        self.assertIn(f"Dear Valued Customer,", html_content)
        self.assertIn(f"The price of <strong>Example Product</strong> has dropped below your set threshold.", html_content)
        self.assertIn(f"Current price:</strong></td>", html_content)
        self.assertIn(f"Don't miss this opportunity to save!</p>", html_content)
        self.assertIn(f"<a href=\"https://www.amazon.co.uk/\" style=\"background-color: #1a5f7a; color: white; padding: 12px 24px; text-decoration: none; font-weight: bold; border-radius: 4px; display: inline-block;\">View Product</a>", html_content)
        self.assertIn(f"This email was sent to: recipienttest6@gmail.com", html_content)


if __name__ == '__main__':
    unittest.main()
