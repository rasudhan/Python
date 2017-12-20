from sys import argv
from os.path import exists

script,fname1,fname2=argv
f1data=open(fname1,'r')
f1datas=f1data.read()
print "%s" %f1datas
print "Input file %s length is %s" %(fname1,len(f1datas))

print "Output file exists??? %r" %exists(fname2)
f2data=open(fname2,'w+')
f2data.write(f1datas)
f2data.close()

f2data=open(fname2,'r')
f2data=f2data.read()
print "New file"
print "%s" %f2data
