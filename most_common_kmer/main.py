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
    print 'python hw2.py -F <filename> -L <kmer>'
    # print "where -F specifies the .txt fasta file to be read and analyzed,"
    # print "-K is the size of kmer to search for"
    # print "and -S is the Sequence."
    #
    # print ""

#speed=O(opt)
def main(argv):
    try:
        opts, args = getopt.getopt(argv, "H:F:L:")
    except getopt.GetoptError:
        print "ERROR! An input file (-F) and a length of a kmer (-L) must be specified. Correct usage:"
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
        if opt == '-L':
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
            mostcommonkmer_in_allseq(sequences,kmerlen)
            mostcommon_in_mostseq(sequences, kmerlen)
    else:
        print "ERROR: length of sequence is None"


#this gives 1st sequence of the sequence and i made this to practice making kmer and kmer count function
#speed=O(lines)
def search_seq(sequences):
    i=0
    for lines in sequences:
        seq=sequences[i]
        return seq

#this function makes the kmer for a given sequence and returns the kmer
#speed=O(DNA)
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

#this function counts the occurence of kmer in a given sequence
#speed=O(len(kmer))
def kmer_count(kmer,search_sq):
    kmer_n_count={}
    for i in range(0,len(kmer)):
        kmer_n_count[kmer[i]] = kmer.count(kmer[i])
    return kmer_n_count


#this function finds the most common kmer in all sequence and counts the occurance of
# it by using the helper function kmercount and makingkmer
#speed=O(key)*O(len(sequence))=O(key*len(sequence))
def mostcommonkmer_in_allseq(sequences,kmerlen):
    countt={}
    for i in range (len(sequences)):
        count_result=kmer_count(makingkmer(kmerlen,sequences[i]),sequences[i])
        for key,value in count_result.items():
            if countt.has_key(key):
                countt[key]=countt[key]+value
            else:
                countt[key]=value
    print "K-mers","Occurences"
    count = 0
    for items in sorted(countt.items(), key=lambda x: x[1],reverse=True):
        if count<5:
            print items[0],"     ",items[1]
        else:
            break
        count=count+1


#this function counts the most commen knmer for most sequence and counts
# using the helper function makingkmer and numpy.unique
#speed=O(len(sequence))*O(key)=O(len(sequence)*key)
def mostcommon_in_mostseq(sequences,kmerlen):
    all_kmer_dict={}
    for item in range((len(sequences))):
        all_kmer_list=numpy.unique(makingkmer(kmerlen,sequences[item]))
        for key in all_kmer_list:
            if all_kmer_dict.has_key(key):
                all_kmer_dict[key]=all_kmer_dict[key]+1
            else:
                all_kmer_dict[key]=1

    print "K-mers", "seq Count"
    count = 0
    for items in sorted(all_kmer_dict.items(), key=lambda x: x[1], reverse=True):

        if count < 5:
            print items[0], "     ", items[1]
        else:
            break
        count = count + 1




if __name__ == '__main__':
    main(sys.argv[1:])


#What are the speed and memory limitations of your implementations?
#the speed for each function is written above the function on the  comments
#there are most 4^k slots with k from 3-8 so  memory would consumeat k*4^k bytes