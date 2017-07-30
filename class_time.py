class Time(object):
	"""Represents the time of day."""
	def __init__(self, hour=0, minute=0, second=0):
		self.hour = hour
		self.minute = minute
		self.second = second
	def print_time(self):
		print '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
	def time_to_int(self):
		minutes = self.hour * 60 + self.minute
		seconds = minutes * 60 + self.second
		return seconds
	def is_after(self, other):
		return self.time_to_int() > other.time_to_int()
	def increment(self, seconds):
		seconds += self.time_to_int()
		return int_to_time(seconds)
	def __str__(self):
		return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
	def __add__(self, other):
		if isinstance(other, Time):
			return self.add_time(other)
		else:
			return self.increment(other)
	def add_time(self, other):
		seconds = self.time_to_int() + other.time_to_int()
		return int_to_time(seconds)
	def __radd__(self, other):
		return self.__add__(other)
		
def int_to_time(seconds):
	time = Time()
	minutes, time.second = divmod(seconds, 60)
	time.hour, time.minute = divmod(minutes, 60)
	return time
	
start = Time(9, 45)
duration = Time(1, 35)
# new_time = start + duration
# print start
# print 300 + start

# end = Time()
# end.hour = 8
# end.minute = 0
# end.second = 0

# end.print_time()

# end = start.increment(1337)
# end.print_time()

# print end.is_after(start)

t1 = Time(7, 43)
t2 = Time(7, 41)
t3 = Time(7, 37)
# total = sum([t1, t2, t3])
total = sum([t1, t2])
print total