from mailjet_rest import Client

def send_price_alert(recipient_email, product_name, current_price, threshold_price):
    # MailJet API credentials
    api_key = 'f28667eb78876aad46462e8d6b7180f3'
    api_secret = '656726402cd90b557e2b0a2372e9c4a2'

    mailjet = Client(auth=(api_key, api_secret), version='v3.1')

    # Email content
    subject = f"Price Alert: {product_name}"
    text_content = f"The price of {product_name} has fallen below your price threshold!\n\nCurrent price: ${current_price:.2f}\nYour price threshold: ${threshold_price:.2f}"
    html_content = f"""
    <h3>Price Alert for {product_name}</h3>
    <p>The price has fallen below your price threshold!</p>
    <ul>
        <li>Current price: <strong>${current_price:.2f}</strong></li>
        <li>Your threshold: <strong>${threshold_price:.2f}</strong></li>
    </ul>
    <p>Don't miss this opportunity!</p>
    """

    # Construct the email data
    sender_email = "group6.cfgdegree24@gmail.com"
    data = {
        'Messages': [
            {
                "From": {
                    "Email": sender_email,
                    "Name": "Price Alert"
                },
                "To": [
                    {
                        "Email": recipient_email,
                        "Name": "Valued Customer"
                    }
                ],
                "Subject": subject,
                "TextPart": text_content,
                "HTMLPart": html_content
            }
        ]
    }

    # Send the email
    result = mailjet.send.create(data=data)

    # Check if the email was sent successfully
    if result.status_code == 200:
        print(f"Email sent successfully to {recipient_email}")
    else:
        print(f"Failed to send email. Status code: {result.status_code}")
        print(result.json())


# Example usage
if __name__ == "__main__":
    send_price_alert("recipienttest6@gmail.com", "Example Product", 30.00, 40.00)