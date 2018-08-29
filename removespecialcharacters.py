def remove_special_characters(txt):
	pattern = '!@#$%^&*()\\.+[]={}<>~`?,|'
	import re
	x = re.sub('[' + re.escape(pattern) + ']', '', txt)
	return x
