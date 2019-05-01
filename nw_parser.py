# parser
# TODO: add trailers and mods
# TODO: hardcode locations
# TODO: conditional replies

def ParseReport(report = ''):
	# determine threat type
	# for now, predetermined list of threats
	# verify with Carrington: if we wanted to test during drill,
	# "drill" keyword would be used
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

def ParseTableLength(lengthString = ''):
	import string
	all = string.maketrans('','')
	nodigs = all.translate(all, string.digits)
	tableLength = int(lengthString.translate(all, nodigs))

	return tableLength
