# arguments or args
# setting up unlimited arguments with *
# can be thought of as lists but not really
# going through arguments in a list as individual items

def Func(*args):
	for arg in args:
		print('Show me my argument:', arg)

sample = [1,2,3,54,'ham']

print('\nRunning args function now\n')
Func(*sample)
print('\nArgs function complete\n')

# keyword arguments or kwargs
# can be thought of as like dictionaries but not really
# setting defaults

def Func2(*args, **kwargs):
	for arg in args:
		print('Look at me, I am', arg)
	for p_title, p_object in kwargs.items():
		print(p_title, p_object)

stuff = ['ramen','bento box', 42]

print('Running kwargs function now\n')
Func2(*stuff, x='kwarg1', y='kwarg2', a=35, b='kwarg4')
print('\nKwargs function complete\n')
