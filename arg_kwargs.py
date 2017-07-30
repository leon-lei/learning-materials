# #arguments
# #setting up unlimited arguments with *
# #going through arguments in a list as individual items

# def Func(*args):
	# for arg in args:
		# print arg

# l = [1,2,3,54,'ham']
# Func(*l)

# #keyword arguments
# #setting defaults
# def Func(x = 234, y = 9):
	# print x, y

# Func(8, 15)

def Func2(*args, **kwargs):
	for arg in args:
		print arg
	for item in kwargs.items():
		print item

stuff = ['john','smith', 98]		
Func2(*stuff, x=53, y=12, a=15, b='foobar')
