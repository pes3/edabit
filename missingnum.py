def missing_nums(a):
	n = len(a) + 1
	return (n*(n+1)/2) - sum(a)
