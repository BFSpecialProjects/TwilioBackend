# Each character costs $.0075

# TODO: implement report verification and student notification functions
# TODO: fix HTTP retrieval failure

# import NestWatch-specific modules
import nw_parser

# client import for outgoing messages and responses
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

# import for database access
import psycopg2

# set up server
app = Flask(__name__)

@app.route('/sms', methods = ['GET', 'POST'])

# method called if teacher sends report
def handleReport():
	# connect to database and instantiate cursor
	connection = psycopg2.connect(host='localhost',
                                  database='nestwatch',
                                  port='5432',
                                  user='postgres',
                                  password='Rn83:xD4')
	cursor = connection.cursor()

	# format response
	# store message sent by teacher and pass it to parser
	report = request.values.get('Body', None)

	# parse message and store as reply
	alert = nw_parser.ParseReport(report)

	# read from database, looking for teachers' numbers
	cursor.execute('SELECT phone_number FROM teachers')
	teachers = str(cursor.fetchall())

	# iterate through list
	# if sender is a verified teacher, give them a response
	sender = request.values.get('From')

	for row in teachers:
		if sender in teachers:	# TODO: else statement to log false positives?
			# respond to teacher that reported threat
			# init TwiML response
			resp = MessagingResponse()

			# ask Carrington what to say to teachers who are reporting incidents
			resp.message('Your report will look like this once sent: '+ alert)

			# verify threat
			verifyThreat(alert, sender)

			return str(resp)

# method to verify threat
def verifyThreat(alert, sender):
	# remember to reomve these when pushing to GitHub
	# using bfspecialprojects account
	account_sid = ''
	auth_token = ''
	client = Client(account_sid, auth_token)

	# create verification message
	alert = alert + ' WHEN IT IS SAFE TO DO SO, please verify this threat by replying to this message.'

	# connect to database and instantiate cursor
	connection = psycopg2.connect(host='localhost',
                                  database='nestwatch',
                                  port='5432',
                                  user='postgres',
                                  password='Rn83:xD4')
	cursor = connection.cursor()

	# count number of rows teachers table
	cursor.execute('SELECT COUNT(*) FROM teachers')
	i = str(cursor.fetchone())

	tableLength = nw_parser.ParseTableLength(i)

	# assign each teacher's number to an element in a list
	teacherNumbers = {}
	cursor.execute('SELECT phone_number FROM teachers')

	x = 0
	while x <= tableLength - 1:
		teacherNumbers[x] = str(cursor.fetchone())
		x += 1

	for number in teacherNumbers:
		print teacherNumbers[number]
		message = client.messages.create(
			to = teacherNumbers[number],
			from_ = '+19842052676',
			body = alert)

		print(message.sid)

	return str(alert)

if __name__ == '__main__':
	app.run(debug=True)
