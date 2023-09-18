# SC0039_Exercise_MA, Mats Andersson. Should run with just "python lengthen"; output from source in output folder.
# For more details, please examine README.md, accessible by "python lengthen ?"
import csv
import os
import sys


def fileOK(file):
    # Attempts to create a file, or raises an error. Used to detect invalid paths.
    try:
        with open(file, 'w'):
            pass
        return True
    except OSError:
        return False


def writeSeqLength(source=None, output=None, suffix="-seq_length", inclusive=False):
    '''
        Reads a .csv file that must have the columns 'loc.end' and 'loc.start', which must contain data that can be parsed as integers.
        Writes a new .csv file, by default in the "output" subfolder, that also has the column 'sec_length', containing each row's (loc.end - loc.start).
        
        args:
            source = csv to read from, defaults to brca_cnvs_tcga-1.csv in the source folder
            output = filename of the output file (in the output subfolder). Defaults to same as source filename
            suffix = appended to a default filename before the extension, to facilitate distinction from source file. Defaults to -seq_length.
                suffix is ignored if the function is also passed an explicit output path
            inclusive is a manual override to prevent off-by-one error:
                True:  assumes loc points to nucleotides (i.e. loc.start == loc.end should be length 1)
                False: asummes loc points the space between them (in which case loc.start == loc.end is length 0)
        
    '''
    # write arguments, mostly for debug purposes
    print(f"writeSeqLength(source={source}, output={output}, suffix={suffix}, inclusive={inclusive})")
    # if no source is supplied, create a default path
    if source is None or source == "":
        source = "source/brca_cnvs_tcga-1.csv"

    # if there's a source file, open it
    if not os.path.exists(source):
        raise FileExistsError("Source file not found")
    with (open(source, "r") as source_file):
        source_reader = csv.DictReader(source_file) #get headers from source file
        headers = source_reader.fieldnames + ['sec_length'] # create new header

        # if no output is supplied, build default folder and filename
        if output is None or output == "": # if there's no output argument, create a default
            output_dir = "output/"
            if not os.path.exists(output_dir): # ensure the default output directory exists
                os.mkdir(output_dir)
            output, csv_ext = os.path.splitext(os.path.basename(source)) # strip extension from output, so that suffix can be added
            output = output_dir + output + suffix + csv_ext # compile final default output (path)

        # if output is a valid path, open it for writing
        if not fileOK(output):
            raise SyntaxError("Output is not a valid filename; incorrect path or suffix?")
        output_file = open((output), "w")
        output_writer = csv.DictWriter(output_file, fieldnames=headers) # set new headers
        output_writer.writeheader() # write new headers

        # calculate and append sec_length column
        for row in source_reader:
            sec_length = (int(row['loc.end']) - int(row['loc.start'])) 
            if(inclusive):
                sec_length += 1 # counter potential off-by-one error
            row['sec_length'] = str(sec_length) # convert to string for storage
            output_writer.writerow(row)

        output_file.close()
    print(f"A new column 'sec_length' added to {output}.")


def printText(text_file):
    # prints a textfile (row by row) in current working directory, or raises an error if it's not found
    if not os.path.exists(text_file):
        raise FileExistsError(f"Failed to locate {text_file}; lengthen.py not in expected environment?")
    else:
        with open(text_file, "r") as printer:
            for row in printer:
                print(row)        


def runByArgs(args):
    # calls writeSeqLength with up to four positional arguments
    if "?" in args:
        printText("README.md")
    else:
        if 4 < len(args): # ensure allowed number of arguments
             raise SyntaxError("Too many arguments; please supply, by position: [source output suffix inclusive(boolean)], or ? for help.")
        writeSeqLength(*args)


runByArgs(sys.argv[1:]) # execute
