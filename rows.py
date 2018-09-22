from num import num
from sym import sym
import re

class data:
	def __init__(self):
		self.w = {}
		self.syms = {}
		self.nums = {}
		self._class = None
		self.rows = {}
		self.name = {}
		self._use = {}
		self.indeps = []

	#???
	#def indep(self, c): return not self.w[c] and self._class is not c
	#def dep(self, c): return not self.indep(c) 

	def header(self, cells):
		for idx, x in enumerate(cells):
			if not re.match('?', x):
				c = len(self._use) + 1
				self._use[c] = idx
				self.name[c] = x
				if re.match('[<>%$]', x):
					self.nums[c] = num()
				else:
					self.syms[c] = sym()
				if re.match('<', x):
					self.w[c] = -1
				elif re.match('>', x):
					self.w[c] = 1
				elif re.match('!', x):
					self._class = c
				else:
					self.indeps.append(c)
	

