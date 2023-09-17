#Assignment 2
def addColumnLength(source):
    print(f"Added length column to {source}")

source_file = open("Assignment_2/source/brca_cnvs_tcga-1.csv", "r")
print("Hello")
print(f"Data type: {type(source_file)}")
addColumnLength(source_file)
source_file.close()
