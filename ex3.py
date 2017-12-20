from sys import argv
#script,fname=argv


fname=raw_input("Enter a filename:")
txt=open(fname,'w')
print "File Name:%r"%fname
print "Do you want to delete?"
raw_input("Sure?")
txt.truncate()
print "File Deleted Successfully!"
line1=raw_input("Enter a line1:")
line2=raw_input("Enter a line2:")
line3=raw_input("Enter a line3:")
print "Lines are placed in new file!"
lines=line1+"\n"+line2+"\n"+line3
txt.write(line1+"\n"+line2+"\n"+line3)
print "New Contents"
txt=open(fname)
print txt.read()
txt.close()
print "File Closed"
