lengthen.py reads a .csv file that must contain the columns 'loc.end' and 'loc.start', containing data that can be read as integers.
It writes a new .csv file that also contains a column 'sec_length', containing each row's (loc.end - loc.start), in the 'output' subfolder."

    args are parsed by position:
        1 source = csv to read from, defaults to brca_cnvs_tcga-1.csv in the source folder
        2 output = filename of the output file (in the output subfolder). Defaults to same as source filename
        3 suffix = appended to filename to facilitate separation from source file. Defaults to -seq_length
        4 inclusive is a manual override to prevent off-by-one error:
            True:  assumes loc points to nucleotides (i.e. loc.start == loc.end should be length 1)
            False: asummes loc points the space between them (in which case loc.start == loc.end is length 0)
        (a ? at any point prints README.md)

SYNTAX: python lengthen.py <SOURCE> <OUTPUT> <SUFFIX> <INCLUSIVE>