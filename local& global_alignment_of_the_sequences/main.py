#!/usr/bin/env/python
#Rasmi Lamichhane Hw2

import sys, getopt, math, os.path, string, collections
import numpy

#reads the file
#speed=O(lines)

def readInput(inFile):
    File = open(inFile, 'r')
    sequences = []
    output = []
    for line in File:
        if not line.startswith('>'):
             output.append(line.rstrip())
    return output

def usage():
    # print the usage of the application
    print 'python Rasmi_lamichhane_hw2.py -F <filename> -S <seq-name> -K <kmer>'
    # print "where -F specifies the .txt fasta file to be read and analyzed,"
    # print "-K is the size of kmer to search for"
    # print "and -S is the Sequence."
    #
    # print ""

#speed=O(opt)
def main(argv):
    try:
        opts, args = getopt.getopt(argv, "H:F:K:S:")
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
        #if opt == '-K':
         #   kmerlen = int(arg)

    # Run the readInput function to format the input file. Store the returned
    # list in the variable sequences

    # store the array
    sequences= readInput(inputFile)
    if len(sequences) is not None:
        search_sq=search_seq(sequences)
    else:
        print "ERROR: length of sequence is None"


#this gives 1st sequence of the sequence and i made this to practice making kmer and kmer count function
#speed=O(lines)
def search_seq(sequences):
    i=0
    print len(sequences)-1
    for lines in range (len(sequences)):
        if lines+1 <= len(sequences)-1:
            print sequences[lines],lines
            print sequences[lines+1],lines+1
        else :
            break





if __name__ == '__main__':
    main(sys.argv[1:])


#What are the speed and memory limitations of your implementations?
#the speed for each function is written above the function on the  comments
#there are most 4^k slots with k from 3-8 so  memory would consumeat k*4^k bytes