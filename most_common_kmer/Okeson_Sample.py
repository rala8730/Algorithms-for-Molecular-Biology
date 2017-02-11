







######################################################################################
#  File            : alexokeson_hw1.py
#  Purpose         : To calculate the GC content of nucleotide sequences and find
#                    exact matches for an input k-mer in nucleotide and protein
#                    sequences
#  Developer       : Alex Okeson Jan 2016
######################################################################################
#
#   File     : alexokeson_hw2.py
#
#   Purpose  : This program is used to evaluate the 5 most commonly seen DNA sequences
#              in a file. Most commonly seen sequences refers to how many chromosomes
#              in the input file contain a sequence. The sequence is of size k where
#              k is an input parameter given by the user and the input file is also
#              given by the user.
#
#   Developer : Alex Okeson
#               CSCI 4314, Spring 2016, HW2
#
##############################################################################
#   
#   Sample command line arguments to run program: 
#   python alexokeson_hw1.py -f file.fasta.txt -l 5
#   -f specifies a fasta .txt input file to be read in and analyzed
#   -l specifies the length of kmers to be evaluated
#
##############################################################################
#
#   Runtime and Space Complexity:
#
#   Runtime:
#     The algorithm to find the 5 most common kmers runs in O(n*m*4^(2k))
#     Where n is the number of sequences in the file,
#     m is the number of nucleotides in each sequence,
#     and k is the length of the kmer specified in the input.
#   
#   Space:
#     The algorithm to find the 5 most common kmers uses O(2*4^(k)) space
#     2 arrays are stored that are the length of the number of all possible
#     kmers of size k.
#
##############################################################################
# 
#   References: Korshoj Jan 2016
#               Korshoj_HW1.py
#               Formatting of the header comment
#
##############################################################################

import sys, getopt, math, os.path

######################################################################################
#  Usage function to help if the user doesn't know how to use the program
#    or makes an error when trying to use it.
#  Sample Command: python alexokeson_hw1.py -f file.fasta.txt -l 5
######################################################################################
def usage():
	# print the usage of the application
	print 'python alexokeson_hw1.py -f <filename> -l <kmer length between 3 and 8>'
	print "where -f specifies the .txt fasta file to be read and analyzed"
	print "and -l is the size of kmer (integer between 3 and 8 inclusive) to search for."

######################################################################################
#  
#  Main application function
#    Parses and checks the input arguments
#    Runs readInput fuction to parse input file into a list of lists of the form
#      [[chromosome name, sequence], [chromosome name, sequence], ...] where chromosome
#      chromosome name and sequence are strings.
#    Runs through each sequence and every kmer in each sequence. Converts the kmer to
#      a unique index where the count for that kmer will be stored. Keep track of what
#      kmers have been seen. After finishing that sequence, updates the counts of each
#      kmer seen in the list storing how many sequences have a given kmer.
#    Runs findTop5 function to find which kmers show up in the most sequences in the
#      input file. Returns a list of length 5 where each element is of the format
#      [number, number] where the first element corresponds to the kmer and the second
#      is the count of how many sequences contained that kmer.
#    Convert the indices corresponding to kmers back to kmers and print the results.
#      
######################################################################################
def main(argv):
	
	inputFile = ''   # The input file name
	lengthKmer = 0   # The length of the kmer
	
	try:
		# go through the input parameters, make sure there is a -f, and -l option
		opts, args = getopt.getopt(argv,"hf:l:")
	# If one of the arguments is missing, print an error message and exit the program
	except getopt.GetoptError:
		print "ERROR! An input file (-f) and a length of a kmer (-l) must be specified. Correct usage:"
		usage()
		sys.exit(2)
	for opt, arg in opts:
		# process each input parameter
		if opt == '-h':
			print "Correct usage is:"
			usage()
			sys.exit()
		if opt == '-f':
			if os.path.isfile(arg):
				inputFile = arg
			# If the input file given does not exist, print an error message and exit the program
			else:
				print "ERROR! Input file must exist. Correct usage:"
				usage()
				sys.exit(2)
		if opt == '-l':
			# If the kmer length is not between 3 and 8 inclusive, print an error message and exit the program
			if int(arg)<3 or int(arg)>8:
				print "ERROR! Length of kmer (-l command) must be between 3 and 8 inclusive. Correct usage:"
				usage()
				sys.exit(2)
			else:
				lengthKmer = int(arg)

	# Run the readInput function to format the input file. Store the returned
	# list in the variable sequences
	sequences = readInput(inputFile)
	
	# Store the counts of how many sequences contain each kmer in the list totalInvertedIndex
	totalInvertedIndex = [0]*int(math.pow(4,lengthKmer))
	
	# Run through each sequence and each kmer in each sequence
#
# ...
#
#top5 = findTop5(totalInvertedIndex)
	
	# Print the results
    #print "5 most common " + str(lengthKmer) + "-mers in the fasta file " + inputFile + " are:"
    #print convertIndextoKmer(top5[4][0],lengthKmer) + " occurs " + str(top5[4][1]) + " times"
    #print convertIndextoKmer(top5[3][0],lengthKmer) + " occurs " + str(top5[3][1]) + " times"
    #print convertIndextoKmer(top5[2][0],lengthKmer) + " occurs " + str(top5[2][1]) + " times"
    #print convertIndextoKmer(top5[1][0],lengthKmer) + " occurs " + str(top5[1][1]) + " times"
#print convertIndextoKmer(top5[0][0],lengthKmer) + " occurs " + str(top5[0][1]) + " times"


######################################################################################
#
#  Algorithm to assign a unique number to each kmer in a sequence. The integer
#  corresponds to the index of the list that the kmer would be stored at if all
#  possible kmers of size lengthKmer were to be stored alphabetically.
#    Input: a kmer to be converted
#    Output: an integer corresponding to the index the kmer would occupy in an
#      alphabetically sorted list of all kmers of size lengthKmer
#
######################################################################################
def convertKmertoIndex(kmer):
#
# ...
#
	return int(index)


######################################################################################
#
#  Algorithm to find the 5 most commonly seen kmers in the file. In the event of a 
#  tie for 5th place, take the kmer in order alphabetically. Only return 5 kmers
#  even if 5th place is a tie
#    Input: the list of how many sequences contain each kmer
#    Output: A list of lists of the form [[number, number], [number, number],...]
#      where the first element of each sublist is the index of the kmer that was 
#      stored in alphabetical order and the second element of the sublist is the
#      count of how many times that kmer was seen. This list is sorted in order from
#      least to greatest.
#
######################################################################################
def findTop5(invertedIndex):
#
# ...
#
	return top5


######################################################################################
#
#  Algorithm to reverse the encoding done by convertKmertoIndex function. Takes the
#  index of the kmer and returns the actual kmer.
#    Input: the index of a kmer and the length of the kmer that was stored
#    Output: the kmer which was originally encoded as an integer
#
######################################################################################
def convertIndextoKmer(index,lengthKmer):
	kmer = ''
#
# ...
#
	return kmer


######################################################################################
#  Parsing input file function
#    Finds the beginning of each sequence and stores chromosome name in one list
#    Puts the corresponding sequence into one string and stores in another list
#    Combines the lists to output
######################################################################################
def readInput(inFile):
    File = open(inFile, 'r')
    sequenceNames = []
    sequences = []
    sequenceSoFar = []
    output = []
    index=0
    for line in File:
        if line.startswith('>'):
            if index >=1:
                sequenceNames.append(name)
                sequences.append(seq)
            index+=1
            name=line[1:].rstrip('\n')
            seq=''
        else:
            seq+=line.rstrip('\n')
    for i in range(len(sequenceNames)):
        output.append((sequenceNames[i],sequences[i]))
        return output


######################################################################################
#  Calls the main() function which will run the program
######################################################################################
if __name__ == "__main__":
	main(sys.argv[1:])
	
