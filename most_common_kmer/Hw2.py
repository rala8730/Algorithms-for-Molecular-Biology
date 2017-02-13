#!/usr/bin/env/python

import sys, getopt, math, os.path, string, collections


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
    print 'python Rasmi_lamichhane_hw1.py -F <filename> -S <seq-name> -K <kmer>'
    # print "where -F specifies the .txt fasta file to be read and analyzed,"
    # print "-K is the size of kmer to search for"
    # print "and -S is the Sequence."
    #
    # print ""


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
            kmerlen = int(arg)

    # Run the readInput function to format the input file. Store the returned
    # list in the variable sequences

    # store the array
    sequences= readInput(inputFile)
    if len(sequences) is not None:
        if (kmerlen<3 or kmerlen>8 ):
            print "length of kmer should be 3-8"
        else:
            search_sq=search_seq(sequences)
            kmer=makingkmer(kmerlen,search_sq)
            count=kmer_count(kmer,search_sq)
            #
            # print count
    else:
        print "ERROR: length of sequence is None"

def search_seq(sequences):
    i=0
    for lines in sequences:
        seq=sequences[i]
    i=i+1
    return seq
def makingkmer(kmerlen,search_sq):
    kmer=[]
    j=0
    k=kmerlen
    i=0
    j=kmerlen
    for DNA in search_sq:
        if (j<=len(search_sq)):
            kmer.append(search_sq[i:j])
            i = i + 1
            j = j + 1

    return kmer

def kmer_count(kmer,search_sq):
    kmer_n_count={}
    for i in range(0,len(kmer)):
        kmer_n_count[kmer[i]] = kmer.count(kmer[i])
    #print kmer_n_count
    return kmer_n_count




if __name__ == '__main__':
    main(sys.argv[1:])
