def printer(arg):
    print "Hello Anand! %r" %arg

printer("sudhan")

print "Working with files and functions"

from sys import argv
script, fname=argv
def printfile(f):
    print f.read()
def rewindfile(f):
    f.seek(0)
def printline(line,f):
    print line,f.readline()
file1=open(fname)
print "PRINTING FILE..."
printfile(file1)
print "REWINDING FILE..."
rewindfile(file1)
print "PRINTING LINE BY LINE..."
line=1
printline(line,file1)
line+=1
printline(line,file1)
