#A small snippet of code which generates all the combinations
#of the password

from past.builtins import xrange
num = "abcdefghijklmnopqrstuvwxyz0123456789"
num_list = "012345"
#If len is 1 we have one pass
a=[]

for x in xrange(len(num_list)):
	a = [i for i in num]
	for y in xrange(x):
		a=[s+i for i in num_list for s in a]
