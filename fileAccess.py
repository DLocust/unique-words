# -*- coding: utf-8 -*-
class File:
	def __init__(self, FILENAME):
		self.__FILENAME = FILENAME
	
	def set_FILENAME(self, FILENAME):
		self.__FILENAME = FILENAME

	def get_FILENAME(self):
		return self.__FILENAME
	
	def get_words(self):
		infile = open(self.__FILENAME, 'r')
		words = 0
		dwords = {}
		strline = ''
		word = ''
		lwords = []
		for line in infile:
			line += ' '
			strline = line.rstrip('\n')
			for ch in strline:
				if ch == '\n':
					word = ''
				if ch != ' ' and ch != ',' and ch != '(' and ch != ')' and ch != '?' and ch != '!' and ch != ';' and ch != ':' and ch != '.' and ch != '"' and ch != '’' and ch != '“':
					word += ch.lower()
				else:
					dwords.update({word:0})
					word = ''
			dwords.pop('\n', 0)
			dwords.pop('', 0)
		words = len(dwords.keys())
		lwords = list(dwords.keys())
		orgList = self.organize(lwords)
		self.output(orgList)
		infile.close()
		return words

	def organize(self, lwords):
		lwords.sort()
		return lwords

	def output(self, orgList):
		outfile = open('list.txt', 'w')
		for i in range(len(orgList)):
			outfile.write(orgList[i] + '\n')
		outfile.close()

