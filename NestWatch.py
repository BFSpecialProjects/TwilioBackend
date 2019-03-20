# Each character costs $.0075

# TODO: implement report verification and student notification functions
# probably can't write a separate module, so do it in this file 

# pandas for "database"
import pandas as pd

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
	# temp spreadsheet of "teacher" numbers, replace w/ database
	
	# import db and assign numbers to column
	# TODO: differentiate between 'student' and 'teacher' numbers in xls file
	df = pd.read_excel('db.xls')
	teachers = df['TeacherNumbers']
	students = df['StudentNumbers']
	
	# if sender is a verified teacher, give them a response
	sender = request.values.get('From')
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
				
				# TODO: write separate methods for verification and notifying
				# students 


if __name__ == "__main__":
	app.run(debug=True)
