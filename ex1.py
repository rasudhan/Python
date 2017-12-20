g = "This is my python program"
print "Yay! "
print 'Works perfectly!'
#anadn

print 7/4
print 7/4.0

cars=5

print "there are ",cars ," cars altogether", 5+5

print "hey %s there" % "you"

a = 5
print "a=%d" %(a+5)

print "I said: %r" %cars
print "I said: %s" %g

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" %hilarious
print joke_evaluation

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

print "How old are you?",
#age=raw_input()
#print "You are %r years old." %age

height="6'2\""
#print "%r" %height

print "Enter a number:",
num=int(raw_input()) #dont use input() security pbm!
print "%r" %num

newnum=raw_input("Enter a new number:")
print newnum
