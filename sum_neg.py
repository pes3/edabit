
def sum_neg(lst):
	x = [i for i in lst if i > 0]
	y = str(x).count
	a = [i for i in lst if i < 0]
	b = sum(a)
	lt = [y,b]
	print(lt)
