#all strings must be lower case
def first_before_second(str, x, y):
	return str.rindex(x)<str.index(y)
	
print(first_before_second("happy birthday", "a", "y"))
