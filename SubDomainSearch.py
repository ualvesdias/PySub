import socket
from termcolor import colored
from LoadSearch import LoadSearch

class SubDomainSearch:
	def __init__(self, file, domain, threads=1):
		self.threads = threads
		self.domainsfound = []
		self.workqueue = LoadSearch(file, domain).loadFile()
		self.numOfItemsPerThread = round(self.workqueue.qsize() / self.threads) + 1

	def search(self):
		for _ in range(self.numOfItemsPerThread):
			if not self.workqueue.empty():
				addr = self.workqueue.get()
				try:
					hostip = socket.gethostbyname(addr)
					print(colored('[+]','green') + ' Sub domain found!! %s with IP address: %s.' % (addr,hostip))
					self.domainsfound.append((addr,hostip))
				except:
					print(colored('[-]','red') + ' Sub domain %s not found.' % (addr))
				self.workqueue.task_done()
			else:
				return False