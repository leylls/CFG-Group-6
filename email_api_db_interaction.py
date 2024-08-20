import sqlite3
# from email_api_v005 import PriceAlert
from utils import check_price_below_threshold # replace utils with cron-jobs/backend_interactions file

def get_user_data():
    conn = sqlite3.connect('price_tracker.db')
    cur = conn.cursor()

    # Query 1: retrieve user details
    cur.execute('''
        SELECT user_id, username, user_email
        FROM user_details
        WHERE email_pref = 1
        LIMIT 1
    ''')
    user_data = cur.fetchone()

    if user_data:
        user_id, username, user_email = user_data

        # Query 2: retrieve product details with the latest price and currency
        cur.execute('''
            SELECT 
                pd.product_id, 
                pd.product_title, 
                pd.url, 
                pd.target_price,
                ph.currency,
                ph.price AS current_price
            FROM product_details pd
            LEFT JOIN price_history ph ON pd.product_id = ph.product_id
            WHERE pd.email_notif = 1
            AND ph.timestamp = (
                SELECT MAX(timestamp)
                FROM price_history
                WHERE product_id = pd.product_id
            )
        ''')
        product_data = cur.fetchall()

        cur.close()
        conn.close()

        # Prepare the user data structure
        user = {
            'user_id': user_id,
            'username': username,
            'email': user_email,
            'products': []
        }

        # Add product details to the user data structure
        for product in product_data:
            product_id, product_title, url, target_price, currency, current_price = product
            user['products'].append({
                'product_id': product_id,
                'product_title': product_title,
                'url': url,
                'target_price': target_price,
                'currency': currency,
                'current_price': current_price
            })

        return [user]  # Return a list of dictionaries for a single user
    else:
        cur.close()
        conn.close()
        return []  # Return an empty list if no user is found

# run line 72 to see the user's information as a list of dictionaries
# print(get_user_data())

def notify_user_from_db(price_alert):
    user_data = get_user_data()

    if not user_data:
        print("No users found with email preferences enabled.")
        return

    emails_sent = 0
    for user in user_data:
        username = user['username']
        email = user['email']

        for product in user['products']:
            if check_price_below_threshold(product['current_price'], product['target_price']):
                try:
                    price_alert.send_alert(
                        recipient_email=email,
                        name=username,
                        product_name=product['product_title'],
                        current_price=product['current_price'],
                        threshold_price=product['target_price'],
                        product_url=product['url'],
                        currency=product['currency']
                    )
                    emails_sent += 1
                except Exception as e:
                    print(f"Failed to send email to {email}: {str(e)}")

    if emails_sent == 0:
        print("No emails sent. Check if any products are below their target prices.")
    else:
        print(f"Total emails sent: {emails_sent}")

# # run to check the code - and delete # on line 2
# if __name__ == "__main__":
#     price_alert = PriceAlert(api_key='your_api_key', api_secret='your_api_secret', sender_email='group6.cfgdegree24@gmail.com')
#     notify_user_from_db(price_alert)