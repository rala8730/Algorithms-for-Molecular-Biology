#!/usr/bin/env/python

import sys, getopt, math, os.path, string

def readInput(inFile):
	File=open(inFile,'r')
	sequence_name=[]
	sequences=[]
	output=[]
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
	return output


def usage():
	# print the usage of the application
    print 'python Rasmi_lamichhane_hw1.py -F <filename> -S <seq-name> -K <kmer>'
    print "where -F specifies the .txt fasta file to be read and analyzed,"
    print "-K is the size of kmer to search for"
    print "and -S is the Sequence."

def main(argv):
    sequences=[]
    inputFile = ''  # The input file name
    lengthKmer = 0  # The length of the kmer

    try:
        # go through the input parameters, make sure there is a -f, and -l option
        opts, args = getopt.getopt(argv, "H:F:K:S:")
    # If one of the arguments is missing, print an error message and exit the program
    except getopt.GetoptError:
        print "ERROR! An input file (-F) and a length of a kmer (-K) must be specified. Correct usage:"
        usage()
        sys.exit(2)
    for opt, arg in opts:
        # process each input parameter
        if opt == '-H':
            print "Correct usage is:"
            usage()
            sys.exit()
        if opt == '-F':
            if os.path.isfile(arg):
                inputFile = arg
            # If the input file given does not exist, print an error message and exit the program
            else:
                print "ERROR! Input file must exist. Correct usage:"
                usage()
                sys.exit(2)
        if opt == '-K':
            lengthKmer = int(arg)
        if opt =='-S':
            usage()
            seqname=arg
            print 'NO Error in _s'

    # Run the readInput function to format the input file. Store the returned
    # list in the variable sequences

    #store the array
    sequences=readInput(inputFile)


def k_mer(sequences):
    for lines in sequences:
        print sequences
	return 0

def reverse_compliment(sequences):
	return 0

def GC_content(sequence):
	return 0

if __name__== '__main__':
    main(sys.argv[1:])

