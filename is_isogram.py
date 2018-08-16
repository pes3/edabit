def is_isogram(txt):
	txt = txt.lower()
	if len(list(txt)) == len(set(txt)):
		return True
	else:
		return False
