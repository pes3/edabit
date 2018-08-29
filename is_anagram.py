def is_anagram(s1, s2):
	x = [i for i in s1.lower()]
	z = sorted(x,reverse = False)
	p = [i for i in s2.lower()]
	w = sorted(p, reverse = False)
	if w == z:
		return True
	else:
		return False
