#!/usr/bin/env/python

import sys, getopt, math, os.path, string, collections


def readInput(inFile):
    File = open(inFile, 'r')
    sequence_name = []
    sequences = []
    output = []
    index = 0
    for line in File:
        if line.startswith('>'):
            if index >= 1:
                sequence_name.append(name)
                sequences.append(seq)
            index += 1
            name = line[1:].rstrip('\n')
            seq = ' '
        else:
            seq += line.rstrip('\n')
        for i in range(len(sequence_name)):
            output.append((sequence_name[i], sequences[i]))
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
                print inputFile,"----------Filename"
            # If the input file given does not exist, print an error message and exit the program
            else:
                print "ERROR! Input file must exist. Correct usage:"
                usage()
                sys.exit(2)
        if opt == '-K':
            kmer = arg

        if opt == '-S':
            usage()
            seqname = arg

    # Run the readInput function to format the input file. Store the returned
    # list in the variable sequences

    # store the array
    sequences = readInput(inputFile)
    foundseq = searchseq(seqname, sequences)
    if foundseq is not None:
        splitseq = splitedfoundseq(foundseq)
        GCcount = GC_content(splitseq)

        kmer_match = k_mermatch(kmer, foundseq)  # Kmar match of sequence
        reverse_seq(foundseq)
        comp = compliment(kmer, foundseq)

        rev_kmer_match = k_mermatch(reverse_seq(kmer), foundseq)  # rev kmer match of sequence
        rev_kmer_and_comp_of_seq_match = k_mermatch(reverse_seq(kmer), compliment(kmer,
                                                                                  foundseq))  # reverse kmer match of sequence compliment

        print "File:", inputFile
        print "Seq:", foundseq
        print "comp:", compliment(kmer, foundseq)
        # print "seq length:", len(foundseq)
        print "Kmer:", kmer
        print "kmermatchpos:", kmer_match, rev_kmer_match, rev_kmer_and_comp_of_seq_match
        print "GC count is :", GCcount, "%"

        # prints the GFF for the Kmer match with sequence
        for match in range(0, len(kmer_match)):
            print seqname, " ", "Rasmi", " ", "match", kmer_match[match], " ", kmer_match[match] + len(
                kmer), " ", "100", " ", "+", " ", "."

        # prints the GFF for the rev kmer and sequence
        for match in range(0, len(rev_kmer_match)):
            if kmer_match[match] != rev_kmer_match[match]:
                print seqname, " ", "Rasmi", " ", "match", rev_kmer_match[match], " ", rev_kmer_match[match] + len(
                    kmer), " ", "100", " ", "+", " ", "."

        # prints the GFF for the rev kmer and sequence compliment
        for match in range(0, len(rev_kmer_and_comp_of_seq_match)):
            print seqname, " ", "Rasmi", " ", "match", rev_kmer_and_comp_of_seq_match[match], " ", \
            rev_kmer_and_comp_of_seq_match[match] + len(kmer), " ", "100", " ", "-", " ", "."
    else:
        print "No sequence found to do the operation"
        return 0


# search for the specific sequence
def searchseq(seqname, sequences):
    for lines in sequences:
        #print lines, "++++++++++++"
        if (lines[0] == seqname):
            return lines[1]


# splits the sequence
def splitedfoundseq(foundseq):
    print foundseq
    if foundseq is not None:
        split = foundseq.split()
        print "split"
        return split
    else:
        print "No seq found"
        return 0


# filters GG and finds the Gc content the GC content
def GC_content(splitseq):
    print splitseq, "splitted seq"
    count = 0
    if splitseq is not 0:
        for pos in range(len(splitseq) - 1):
            if (splitseq[pos] == "G" and splitseq[pos + 1] == "C") or (
                    splitseq[pos] == "C" and splitseq[pos + 1] == "G"):
                count = count + 1
            elif (splitseq[pos] == "T" and splitseq[pos + 1] == "A") or (
                    splitseq[pos] == "A" and splitseq[pos + 1] == "T"):
                count = count + 1
        count = count - 1 + 0.0
        G_Ccount = (float(count) * 100.0) / len(splitseq)
        return G_Ccount
    else:
        print "no sequence found to count GC"
        return 0


# finds the position of the kmer in foundseqence
def k_mermatch(kmer, foundseq):
    if foundseq is not None:
        index = 0
        matchpos = []
        for pos in range(len(foundseq) - len(kmer) + 1):
            if kmer == foundseq[index:index + len(kmer)]:
                matchpos.append(index)
            index = index + 1

        return matchpos
    else:
        print "NO sequence found to compare with K mer"
        return 0


# this function tkes the reverse of sequence
def reverse_seq(foundseq):
    if foundseq is not None:
        for seq in foundseq:
            reverse = foundseq[::-1]

            return reverse
    else:
        print "NO sequence found to reverse"
        return 0


# this function takes the compliment
def compliment(kmer, foundseq):
    if foundseq is not None:
        compliment = ""
        for seq in foundseq:
            if seq == "G":
                seq = "C"
                compliment = compliment + seq
            elif seq == "C":
                seq = "G"
                compliment = compliment + seq
            elif seq == "A":
                seq = "T"
                compliment = compliment + seq
            elif seq == "T":
                seq = "A"
                compliment = compliment + seq
            else:
                compliment = compliment + seq
        return compliment
    else:
        print "no sequence found to take the compliment"
        return 0


if __name__ == '__main__':
    main(sys.argv[1:])
