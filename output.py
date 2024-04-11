# script that removes all comment and empty lines from a txt file

fileIn = "AtAGlance_edit.txt"
fileOut = "output.txt"

with open(fileIn, "r") as f:
    temp = f.readlines()

with open(fileOut, "w") as f:
    for l in temp:
        if l.strip() and not (l.strip().startswith('#')):
            f.write(l)