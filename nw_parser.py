# parser
# TODO: add trailers and mods
# TODO: conditional replies

def ParseReport(report = ''):
	# determine threat type
	# for now, predetermined list of threats
	# verify with Carrington: if we wanted to test during lockdown,
	# "lockdown" keyword would be used
	threats = ['shooter', 'fire', 'lockdown', 'animal', 'dog', 'student with a gun', 'student with gun']

	for item in threats:
		if item in report:
			threat = item

	# split the message at the first number to determine location
	location = ''

	for i in report:
		if i.isdigit():
			# append to location string
			location += i
			
	# form a coherent sentence for alert
	# ask Carrington what this message should say
	alert = "Attention faculty and students: There is a(n) " + threat + " around the " + location + " part of the campus."

	return alert

if __name__ == "__main__":
	ParseReport()