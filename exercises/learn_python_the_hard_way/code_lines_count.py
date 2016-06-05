import os

def count_lines(dir):
	num_lines = 0
	# dir = os.getcwd()
	file_list = os.listdir(dir)
	# print file_list
	for i in file_list:
		if ".py" in i:
			file_lines = 0
			file = open(str(dir)+ "/" + str(i))
			for l in file:
				if l != "\n":
					num_lines +=1
					file_lines +=1
			print "This is %s file, number of lines is %d, total is \
		%d lines" % (i, file_lines, num_lines)
			file.close()
	return num_lines

all_lines = count_lines(os.getcwd()) + count_lines( "../Ubuntu/courses/Udacity/Python1/")

print "So total is: " + str(all_lines)