j=0
s=0
x=0
n=0
firstPass = True
while firstPass or j<6:
    firstPass = False
    x=(int)(raw_input())
    if x < 75:
        s=s+x
        n=n+1
        j=j+1
        
print "S=%r" %s
print "N=%r" %n
print "J=%r" %j
