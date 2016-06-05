from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read();open(to_file, "w").write(indata)

#########################################
# we could do these two on one line, how? 
#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exists? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CRTL-C to abort."
#raw_input()



#print "Alright, all done."

#out_file.close()
