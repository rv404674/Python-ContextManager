import time, httplib

class Timer:
	def __init__(self, name):
		self.name = name

	def __enter__(self):
		self.start = time.time()

	def __exit__(self, *args):
		self.end = time.time()
		self.interval = self.end - self.start
		print('{} took {} seconds'.format(self.name, self.interval))
		return False

with Timer('fetching Google Homepage'):
	conn = httplib.HTTPConnection('google.com')
	conn.request('GET', '/')
