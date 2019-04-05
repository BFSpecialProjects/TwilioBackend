from twilio.rest import Client

account_sid = "account_sid"
auth_token = "auth_token"

client = Client(account_sid, auth_token)

# Monthly Usage Summary
records = client.usage.records.last_month.list()

# All Time Usage Summary
ATrecords = client.usage.records.list()

# Monthly Messages Sent
Mrecords = client.usage.records.last_month.list(category="sms")

# Messages sent during specific period
Srecords = client.usage.records.daily.list(
    category="sms", start_date="2019-04-05", end_date="2019-04-06"
)

print("All Time Records\n")
print(ATrecords)
input("Press Enter to continue...")
print("Montly SMS Records\n")
print(Mrecords)
input("Press Enter to continue...")
print("SMS Records during specified period\n")
print(Srecords)
input("Press Enter to continue...")
