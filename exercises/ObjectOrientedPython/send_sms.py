from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC85eb0d13d9390baab73f98909265a85f"
auth_token  = "d7a38db989ea199e078ed6671ce4e91a"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hi, Julia!",
    to="+380663712766",    # Replace with your phone number
    from_="+12016132368") # Replace with your Twilio number
print message.sid
