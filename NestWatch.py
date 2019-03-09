# Each character costs $.0075

# import NestWatch-specific modules
import nw_parser

# client import for simply sending messages
from twilio.rest import Client

# imports for responding to messages
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

# reply to messages
app = Flask(__name__)
@app.route("/sms", methods = ['GET', 'POST'])

# method called if teacher sends report
def handleReport():
	# temp list of "teacher" numbers, replace w/ database
	teachers = ['+19192748780']
	sender = request.values.get('From')

	# if sender is a verified teacher, give them a response
	for number in teachers:
		if sender in teachers:
			try:
				# store message sent by teacher and pass it to parser
				report = request.values.get('Body', None)

				# parse message and store as reply
				alert = nw_parser.ParseReport(report)

				# respond to teacher that reported threat
				# init TwiML response
				resp = MessagingResponse()

				# ask Carrington what to say to teachers who are reporting incidents
				resp.message('Your report will look like this once sent: ' + alert)

				return str(resp)
			except TwilioRestException as e:
				print(e)


if __name__ == "__main__":
	app.run(debug=True)