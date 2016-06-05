from sys import argv
from json import dumps

########## CONSTANTS ##############
SEPARATORS = [' ', ' - ', ' "', '" ', ' "', '" "', '"']
UNIMPORTANT_SEPARATORS = {'" "'}
DATA_DICT = {	0: 'IP',
				1: 'domain',
				2: 'dateTime',
				3: 'HTTPRequest',
				4: 'responseStatus',
				5: 'client'
			}
FILE_NAME = 'out_%04d.json'

## donno if it is a good idea, but wanted to print 
## number of created files at the and
CREATED_FILES_NUM = 0

###### Helper functions ###########
def parse_lines(line):

	data = []
	for sep in SEPARATORS:

		if sep not in UNIMPORTANT_SEPARATORS:
			to_separate = line.find(sep)
			data.append(line[:to_separate])
			line = line[to_separate + len(sep):]

		## filter unimportant data
		else:
			to_separate = line.find(sep)
			line = line[to_separate + len(sep):]
	return data

def convert_to_dict(data):
	json_element = {}
	for i in range(len(data)):
		json_element[DATA_DICT[i]] = data[i]
	return json_element

###### Main Function ################
def write_json(file, size):
	elements_added = 0
	files_order = 1
	json_list = []

	for line in file:

		data = parse_lines(line)
		json_element = convert_to_dict(data)
		json_list.append(json_element)

		elements_added += 1

		if elements_added >= size:

			## convert to json
			json_list = dumps(json_list)

			## write json list
			to_write = open(FILE_NAME % (files_order), 'w')
			to_write.write(json_list)
			to_write.close()

			## empty variables
			json_list = []
			elements_added = 0
			files_order += 1

			# for testing.. 
			# decides how many files to write
			# if files_order > 3:
			# 	break

	global CREATED_FILES_NUM
	CREATED_FILES_NUM = files_order - 1

###### Process flow #################

## take the name of the file from first argument to script call
file_name = str(argv[1])

## take the number of values that are supposed to be in 
## generated JSON file from second argument to script call
size = int(argv[2])

## open file and do magic
with open(file_name, 'r') as log:
	## initialize variables
	write_json(log, size)
	print ('Succesfully created %s json files from %s' % (
				CREATED_FILES_NUM, file_name))


# #### Some stress testing ############
# f= open(file_name, 'r')

# for i in range(100000):
# 	line = f.readline()

# 	if len(parse_lines(line)) != 6:
# 		print line
# 		print parse_lines(line)
# 		break
# f.close()
