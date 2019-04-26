import queue

class LoadSearch():
	def __init__(self, file, domain):
		self.file = file
		self.domain = domain
		self.subqueue = queue.Queue()

	def loadFile(self):
		with open(self.file,'r') as subfile:
			[self.subqueue.put(sub.strip()+'.'+self.domain) for sub in subfile.readlines()] # .replace('\n','')
		return self.subqueue
