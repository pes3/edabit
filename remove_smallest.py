def remove_smallest(lst):
	if len(lst) > 0:
		y = min(lst)
		lst.remove(y)
		return lst
	else:
		return lst
