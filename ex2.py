from sys import argv
a,b,c=argv

print"FILENAME:",a
print"V1=",b
print"V2=",c

prompt='-->'
print "Enter your name:"
name=raw_input(prompt)
print "Welcome" ,name
print """
welcome anand
this is a
multiline trial %s
""" %name
