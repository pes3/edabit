def is_valid_PIN(pin):
	import re
	pattern = '!@#$%^&*()\\.+[]={}<>~`?,_-|'
	x = re.sub('[' + re.escape(pattern) + ']', '', pin) # come back to make into 1 line of regex
	pin = re.sub(r"[a-z]", '', x)
	if len(pin) == 4:
		return True
	elif len(pin) == 6:
		return True
	else:
		return False
