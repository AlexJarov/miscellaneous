#Programm deleting empty lines from text document.
#Runs from console by command
#python noemptylines.py -i input/file.txt -o output/file.txt
#Where input/file.txt is path to input file
#and output/file.txt is path to output file.
#It can be the same file if you need re-write it.

#Importing neccessery package
import argparse

#Providing the ability to specify the name of
#the file being processed and resulting file
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="path to input textfile")
ap.add_argument("-o", "--output", required=True, help="path to output textfile")
args = vars(ap.parse_args())

# Reading the input file
with open(args["input"], "r") as text:
    lines = text.readlines()
#Opening or creating the output file
with open(args["output"], "w") as text:
#Writing there only lines with symbols
    for line in lines:
        if len(line.strip("\n")) != 0:
            text.write(line)
