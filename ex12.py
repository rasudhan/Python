"""i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "out of loop",i
print "The numbers: "

for num in numbers:
    print num
"""
print "NEW PROGRAM"

def print_func(x,inc):
    num=[]
    for inc in range(1,x):
        print "VALUE:",inc
        num.append(inc)
        inc+=1
    return num

print_func(6,1)
