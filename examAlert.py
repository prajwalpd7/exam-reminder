from datetime import datetime, timedelta
from twilio.rest import Client
import emoji

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Event date
event_date = datetime(2023, 1, 27)

# Calculating days remaining
now = datetime.now()
days_remaining = event_date - now

# Sending message
message = client.messages.create(
    from_='whatsapp:+14********',
    body='..your exam is coming up..                      ' +
    str(days_remaining.days) + ' days remaining for "SE" paper' +
    emoji.emojize(':thumbs_up:'),
    to='whatsapp:+9183********'
)

print(message.sid)
