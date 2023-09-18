#SC0039_Exercise_MA, Mats Andersson
import csv
import os
import sys

def fileOK(file):
    # Attempts to create the output file, or raise an error if the name is invalid
    try:
        with open(file, 'w'):
            pass
        return True
    except OSError:
        return False

def writeSeqLength(source=None, output=None, suffix="-seq_length", inclusive=False):
    '''
        Reads a .csv file that must contain the columns 'loc.end' and 'loc.start', containing data that can be read as integers.
        Writes a new .csv file that also contains a column 'sec_length', containing each row's (loc.end - loc.start), in the "output" subfolder.
        
        args:
            source = csv to read from, defaults to brca_cnvs_tcga-1.csv in the source folder
            output = filename of the output file (in the output subfolder). Defaults to same as source filename
            suffix = appended to filename to facilitate separation from source file. Defaults to -seq_length
            inclusive is a manual override to prevent off-by-one error:
                True:  assumes loc points to nucleotides (i.e. loc.start == loc.end should be length 1)
                False: asummes loc points the space between them (in which case loc.start == loc.end is length 0)
        
    '''
    # write arguments, mostly for debug purposes
    print(f"writeSeqLength(source={source}, output={output}, suffix={suffix}, inclusive={inclusive})")
    # if no source is supplied, default
    if source is None or source == "":
        source = "source/brca_cnvs_tcga-1.csv"
    # if there's a source file, open it
    if not os.path.exists(source):
        raise FileExistsError("Source file not found")
    with (open(source, "r") as source_file):
        source_reader = csv.DictReader(source_file)
        headers = source_reader.fieldnames + ['sec_length'] # add header
        # if no output is supplied, build a default folder and filename
        if output is None or output == "":
            output_dir = "output/"
            if not os.path.exists(output_dir):
                os.mkdir(output_dir)
            output, csv_ext = os.path.splitext(os.path.basename(source))
            print(f"output1: {output}")
            output = output_dir + output + suffix + ".csv"
            print(f"output2: {output}")
        # if output is a valid path, open it for writing
        if not fileOK(output):
            raise SyntaxError("Output is not a valid filename; incorrect path or suffix?")
        output_file = open((output), "w")
        output_writer = csv.DictWriter(output_file, fieldnames=headers)
        output_writer.writeheader()
        # calculate and append sec_length column
        for row in source_reader:
            sec_length = (int(row['loc.end']) - int(row['loc.start'])) 
            if(inclusive):
                sec_length += 1
            row['sec_length'] = str(sec_length)
            output_writer.writerow(row)
        output_file.close()

def runByArgs(args):
    # calls writeSewLength with up to four positional arguments
    if "?" in args:
        print("README.md") #TODO: acutally print it
    else:
        if 4 < len(args):
            raise SyntaxError("Too many arguments; please supply, by position: [source output suffix inclusive(boolean)], or ? for help.")
        writeSeqLength(*args)

runByArgs(sys.argv[1:])
