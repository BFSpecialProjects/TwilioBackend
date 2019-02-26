# File to combine sending and replying funcitonalities

# client import for simply sending messages
from twilio.rest import Client

# imports for responding to messages
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

# welcome users to service
def welcomeMessage():
	# account SID
	account_sid = "SIDHERE"

	# account auth token
	### when posting to GitHub, remove auth token from code ###
	auth_token = "AUTHTOKENHERE"

	# client object
	client = Client(account_sid, auth_token)

	# create and send message
	# upon implementation, change to "Welcome to NestWatch"
	message = client.messages.create(
		to = "+19192748780",
		from_ = "+19193354640",
		body = "Welcome to NestWatch.")

	print(message.sid)

# reply to messages
app = Flask(__name__)

@app.route("/sms", methods = ['GET', 'POST'])

# reply to messages sent from user
def sms_reply():
	try:
		# get message sent by user
		body = request.values.get('Body', None)

		# start TwiML response
		resp = MessagingResponse()

		# determine reply
		# 1 and 2 just to demonstrate multiple responses
		# if "n" (for new user), send welcome message
		if body == 'a':
			resp.message('1')
		elif body == 'b':
			resp.message('2')
		elif body=="n":
			welcomeMessage();

		return str(resp)
	except TwilioRestException as e:
		print(e)

if __name__ == "__main__":
	app.run(debug=True)