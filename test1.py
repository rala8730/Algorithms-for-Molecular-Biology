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
    #print "where -F specifies the .txt fasta file to be read and analyzed,"
    #print "-K is the size of kmer to search for"
    #print "and -S is the Sequence."

def main(argv):

    try:
        opts, args = getopt.getopt(argv, "H:F:K:S:")
    except getopt.GetoptError:
        #print "ERROR! An input file (-F) and a length of a kmer (-K) must be specified. Correct usage:"
        usage()
        sys.exit(2)
    for opt, arg in opts:
        # process each input parameter
        if opt == '-H':
            #print "Correct usage is:"
            usage()
            sys.exit()
        if opt == '-F':
            if os.path.isfile(arg):
                inputFile = arg
            # If the input file given does not exist, print an error message and exit the program
            else:
                #print "ERROR! Input file must exist. Correct usage:"
                usage()
                sys.exit(2)
        if opt == '-K':
            lengthKmer = int(arg)
        if opt =='-S':
            usage()
            seqname=arg

    # Run the readInput function to format the input file. Store the returned
    # list in the variable sequences

    #store the array
    sequences=readInput(inputFile)
    foundseq = searchseq(seqname,sequences)
    splitseq=splitedfoundseq(foundseq)
    GCcont=GC_content(splitseq)
    print GCcont,"== total count in main"
    reverse_compliment(splitseq)


def searchseq(seqname,sequences):
    for lines in sequences:
        if(lines[0]==seqname):
            return lines[1]
def splitedfoundseq(foundseq):
        split=foundseq.split()[0]
        return split

def GC_content(splitseq):
    count=0
    print splitseq
    for pos in range(len(splitseq)-1):
        if (splitseq[pos]=="G" and splitseq[pos+1]=="C") or (splitseq[pos]=="C" and splitseq[pos+1]=="G"):
           count=count+1
           print count, "count of GC"
        elif (splitseq[pos]=="T" and splitseq[pos+1]=="A") or (splitseq[pos]=="A" and splitseq[pos+1]=="T"):
            count = count+1
            print count,"count of AT"
    print count,"==total count inside fun"
    G_Ccount=(float(count) *100)/len(splitseq)
    print G_Ccount,"GC =-----"
    return G_Ccount

#possible longest length of the string
def k_mer(foundseq):

    return 0

def reverse_compliment(splitseq):
    print splitseq
    compliment=[]
    for pos in range(len(splitseq)-1):
        if splitseq[pos]=="G":
            compliment.append("C")
            print splitseq[pos],"this is the pos"
            continue
        elif splitseq[pos] == "C":
            compliment.append("G")
            continue
        elif splitseq[pos] == "A":
            compliment.append("T")
        elif splitseq[pos] == "T":
            compliment.append("A")
        else:
            print pos,"<--- this is not G A C T "
            #compliment.append(pos)
    print compliment

    return 0


if __name__== '__main__':
    main(sys.argv[1:])







