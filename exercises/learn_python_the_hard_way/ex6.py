x= "There are %d types of people." %10
binary = "binary" 
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I sad: %r." % x
print "I also sad: '%s'." % y

hilarious = True
joke_evaluation = "Isn't that joke so funy?! %r"

print joke_evaluation % hilarious

w = "This is left side of..." 
e = "a string with a right side"

print w + e