lengthen.py reads a .csv file that must have the columns 'loc.end' and 'loc.start', which must contain data that can be parsed as integers.
Writes a new .csv file, by default in the "output" subfolder, that also has the column 'sec_length', containing each row's (loc.end - loc.start).

Accepts 0-4 positional arguments: <SOURCE> <OUTPUT> <SUFFIX> <INCLUSIVE> (enter "" to use the default)
    source = csv to read from, defaults to brca_cnvs_tcga-1.csv in the source folder
    output = filename of the output file (in the output subfolder). Defaults to same as source filename
    suffix = appended to a default filename to facilitate distinction from source file. Defaults to -seq_length.
        suffix is ignored if the function is also passed an explicit output path
    inclusive is a manual override to prevent off-by-one error:
        True:  assumes loc points to nucleotides (i.e. loc.start == loc.end should be length 1)
        False: asummes loc points the space between them (in which case loc.start == loc.end is length 0)

example: python lengthen.py "" "output/Differentname" "" True

SYNTAX: python lengthen.py <SOURCE> <OUTPUT> <SUFFIX> <INCLUSIVE>