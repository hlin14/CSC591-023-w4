from num import num
from sym import sym
import re
from testEngine import O

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

	def header(self, cells):#cells just one row
		for idx, x in enumerate(cells):
			#print(idx, x)
			if not re.match('\?', x):
				c = len(self._use) + 1
				self._use[c] = idx
				self.name[c] = x
				if re.match('[<>$]', x):
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

	#add a row
	def row(self, cells):
		r = len(self.rows) + 1
		self.rows[r] = {}
		for c, col in self._use.items():#col will collect the col that is in used
			x = cells[col]  #get the col obj in the cell
			if x != '?':
				if self.nums.get(c, '') != '':
					x = float(x)
					self.nums[c].numInc(x)
				else:
					self.syms[c].symInc(x)
		self.rows[r][c] = x


	def rows1(self,fname):
		with open(fname) as stream:
			first = True
			lines = stream.readlines()
			for line in lines:
				re.sub("[\t\r]*","",line)
				re.sub("#.*","",line)
				cells = line.split(',')
				for i in range(len(cells)):
					cells[i] = cells[i].strip()
				if len(cells) > 0:
					if first:
						#print(cells)
						self.header(cells)
					else:
						#print(cells)
						self.row(cells)
				first = False
				#print(line)

	def readRows(self, fname):
		return self.rows1(fname)

@O.k
def testing():
	n1 = data()
	n1.readRows("weather.csv")

	print("           "+ "n"+ "  " +"mode" + " " + "frequency")
	for sym_idx in n1.syms:
		print(sym_idx, n1.name[sym_idx], n1.syms[sym_idx].n, n1.syms[sym_idx].mode, n1.syms[sym_idx].most)

	assert n1.syms[1].n == 14 and n1.syms[1].mode == 'sunny' and n1.syms[1].most == 5

	print("        "+ "n"+ "  " +"mu" + "    " + "sd")
	for num_idx in n1.nums:	
		print(num_idx, n1.name[num_idx], n1.nums[num_idx].n ,round(n1.nums[num_idx].mu, 2),round(n1.nums[num_idx].sd, 2))

	assert round(n1.nums[2].mu, 2) == 73.57 and round(n1.nums[2].sd, 2) == 6.57

	print('\n')

	n2 = data()
	n2.readRows("weatherLong.csv")

	print("           "+ "n"+ "  " +"mode" + " " + "frequency")
	for sym_idx in n2.syms:
		print(sym_idx, n2.name[sym_idx],n2.syms[sym_idx].n, n2.syms[sym_idx].mode, n2.syms[sym_idx].most)
	
	assert n2.syms[1].n == 28 and n2.syms[1].mode == 'sunny' and n2.syms[1].most == 10

	print("         "+ "n"+ "  " +"mu" + "    " + "sd")
	for num_idx in n2.nums:	
		print(num_idx, n2.name[num_idx], n2.nums[num_idx].n ,round(n2.nums[num_idx].mu, 2),round(n2.nums[num_idx].sd, 2))
	
	assert n2.nums[2].n == 28 and round(n2.nums[2].mu, 2) == 73.57 and round(n2.nums[2].sd, 2) == 6.45

	print('\n')

	n3 = data()
	n3.readRows("auto.csv")
	print("              "+ "n"+ "  " +"mode" + " " + "frequency")
	for sym_idx in n3.syms:
		print(sym_idx, n3.name[sym_idx],n3.syms[sym_idx].n, n3.syms[sym_idx].mode, n3.syms[sym_idx].most)
	#print(n3.syms[1].n,n3.syms[1].mode,n3.syms[1].most)
	assert n3.syms[1].n == 398 and n3.syms[1].most == 204

	print("                 "+ "n"+ "   " +"mu" + "      " + "sd")
	for num_idx in n3.nums:	
		print(num_idx, n3.name[num_idx], n3.nums[num_idx].n ,round(n3.nums[num_idx].mu, 2),round(n3.nums[num_idx].sd, 2))

	assert n3.nums[2].n == 398 and round(n3.nums[2].mu, 2) == 193.43 and round(n3.nums[2].sd, 2) == 104.27
	
if __name__== "__main__":
  O.report()

