#!/usr/bin/env/python

import sys, getopt, math, os.path, string, collections


def readInput(inFile):
    File = open(inFile, 'r')
    sequences = []
    output = []
    myseq=[]

    index = 0
    for line in File:
        if line.startswith('>'):
            if index >= 1:
                sequences.append(seq)
                myseq.append(seq)
            index += 1
            print myseq,"seq"
            seq = ' '
        else:
            seq += line.rstrip('\n')
        output.append(seq)
        #print output
    return output


def usage():
    # print the usage of the application
    print 'python Rasmi_lamichhane_hw1.py -F <filename> -S <seq-name> -K <kmer>'
    # print "where -F specifies the .txt fasta file to be read and analyzed,"
    # print "-K is the size of kmer to search for"
    # print "and -S is the Sequence."
    print ""


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
        if opt == '-K':
            kmerlen = arg

    # Run the readInput function to format the input file. Store the returned
    # list in the variable sequences

    # store the array
    sequences = readInput(inputFile)

    foundseq = searchseq(kmerlen,sequences)

    if kmerlen is not None:
        print len(sequences),"+_+_+_"


        if kmerlen<len(sequences):
            search_seq=sequences(kmerlen,sequences)
            if foundseq is not None:
                splitseq = splitedfoundseq(foundseq)
            else:
                print "No sequence found to do the operation"
    else:
        print "ERROR: length of kmer is greater than length of sequence"



# search for the specific sequence
def searchseq(kmerlen,sequences):
    for lines in sequences:
        if (kmerlen>0):
            #print lines[1]
            return lines[1]
def search_seq(kmerlen, sequences):
    print "hello"
    for lines in sequences:

        if (kmerlen==len(sequences)):
            return sequences
        else:
            print "operation for > kmer"

    return 0


# splits the sequence
def splitedfoundseq(foundseq):

    if foundseq is not None:
        split = foundseq.split()

        return split
    else:
        print "No seq found"
        return 0

if __name__ == '__main__':
    main(sys.argv[1:])
