# Each character costs $.0075

# TODO: implement report verification and student notification functions
# probably can't write a separate module, so do it in this file 

# import NestWatch-specific modules
import nw_parser

# client import for outgoing messages and responses
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

# import for database
import psycopg2

# set up server
app = Flask(__name__)
@app.route("/sms", methods = ['GET', 'POST'])

# method to verify threat
def verifyThreat(alert, sender):
	# create verification message
	alert = alert + " WHEN IT IS SAFE TO DO SO, please verify this threat by replying to this message."
	
	# connect to database and instantiate cursor
	connection = psycopg2.connect(host="localhost",
                                  database="nestwatch",
                                  port="5432",
                                  user="postgres",
                                  password="Rn83:xD4")
	cursor = connection.cursor()
	
	# read from database, looking for teachers' numbers
	cursor.execute("SELECT phone_number FROM teachers")
	teachers = str(cursor.fetchall())
	
	# iterate through teachers list and send verification message to all but sender
	for row in teachers:
		if not sender:
			message = client.message.create(
				to = teachers[row],
				from_ = "+19193354640",
				body = alert)
			
			print(message.sid)
			
# method called if teacher sends report
def handleReport():
	# connect to database and instantiate cursor
	connection = psycopg2.connect(host="localhost",
                                  database="nestwatch",
                                  port="5432",
                                  user="postgres",
                                  password="Rn83:xD4")
	cursor = connection.cursor()
	
	# format response
	# store message sent by teacher and pass it to parser
	report = request.values.get('Body', None)
			
	# parse message and store as reply
	alert = nw_parser.ParseReport(report)
	
	# read from database, looking for teachers' numbers
	cursor.execute("SELECT phone_number FROM teachers")
	teachers = str(cursor.fetchall())
	
	# iterate through list	
	# if sender is a verified teacher, give them a response
	sender = request.values.get('From')
	for row in teachers:
		if sender in teachers:
			# respond to teacher that reported threat
			# init TwiML response
			resp = MessagingResponse()
			
			# ask Carrington what to say to teachers who are reporting incidents
			resp.message('Your report will look like this once sent: ' + alert)
			
			# TODO: function doesn't recognize parameters
			# verify threat
			verifyThreat(alert, sender)
			
			return str(resp)
			
if __name__ == "__main__":
	app.run(debug=True)