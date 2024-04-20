from twilio.rest import Client
# in this part you have to replace account_sid
# auth_token, twilio_number, recipient_number with your actual credential

account_sid = 'AC1a822264350a96972f22fcbb87aefec1'
auth_token = 'ae1f32fdf20a91cba89a4d287298ff08'
twilio_number = +13344876127
recipient_number = +919322150275

# Create Twilio client
client = Client(account_sid, auth_token)

# Send SMS
# in body part you have to write your message
message = client.messages.create(
	body='Hi, This automated messege..',
	from_= +13344876127,
	to = +919322150275
)
print("Message sent with SID: {message.sid}")
