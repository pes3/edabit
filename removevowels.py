import re
def silence_Trump(txt):
	 result = re.sub(r'[AEIOU]', '', txt, flags=re.IGNORECASE)
	 return result
