#Assignment 2
import csv

def addColumnLength(source):
    print(f"Added length column to {source}")

with (open("Assignment_2/source/brca_cnvs_tcga-1.csv", "r") as file):
    data = csv.DictReader(file)
    for row in data:
        for cell in row['loc.start']:
            print(f"cell:{cell}")
#print(f"Data type: {type(source_file)}")
#addColumnLength(source_file)
#source_file.close()
