#!/usr/bin/env/python

import sys, getopt, math, os.path, string
print'head'
def readInput(inFile):
	File=open(inFile,'r') 
	print'File'
	sequence_name=[]
	sequences=[]
	outputs=[]
	index=0
	for line in File:
		if line.startswith('>'):
			if index >=1:
				sequence_name.append(name)
				sequences.append(seq)
			index+=1
			name=line[1:].rstrip('\n')
			seq=' '
		else:
			seq+=line.rstrip('\n')
	for i in range(len(sequence_name)):
		output.append((sequence_name[i],sequences[i]))
	print'sequence_name'
	return output

print'this is start'

def nameofsequence(name):
	for names in name:
		print'name'
	print(name)
	return 0
def search_insequence():
	return 0
def count():
	return 0
#nameofsequence(name):


def main(argv):
	

if __name__== '__main__':
	main(sys.argv[1:])
	



readInput
print'this is end'

