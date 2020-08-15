import os
import tempfile
import json
import argparse
import sys

DEBUG = True


def print_path(storage_path):
	print("Storage path is: ", storage_path)


def key_check(key):
	if (arguments.key):
		return True
	else:
		return False

def value_check(value):
	if (arguments.value):
		return True
	else:
		return False



def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("--key")
	parser.add_argument("--value")
	args = parser.parse_args() #parsing arguments
	ARGS_CHK = False # flag for determining whether the input of arguments was correct
	print("\n\n\n") # for easier log view
	if DEBUG:
		if (args.key and args.value):
			print("both key and val arguments passed")
			print("key argument:", args.key)
			print("value argument:", args.value, "\n\n\n")
		elif (args.key):
			print("only key argument passed")
			print("key argument:", args.key, "\n\n\n")
		elif (args.value):
			print("only value argument passed")
			print("value argument:", args.value, "\n\n\n")
		else:
			print("None of the arguments were passed", "\n\n\n")
	if (args.key and args.value):
		ARGS_CHK = True # input OK
		if DEBUG:
			print("key and value passed")
			print("key: ", args.key, "value: ", args.value, "\n\n\n")
	elif (args.key and args.value == None):
		ARGS_CHK = True # input OK
		if DEBUG:
			print("key passed")
			print("key: ", args.key, "\n\n\n")
	elif (args.key == None and args.value):
		ARGS_CHK = False # input not OK
		print("Error: incorrect input.")
		print("Entering value without key is not allowed. Key option expected.", "\n\n\n")
	else:
		ARGS_CHK = False
		print("Error: incorrect input. Key option expected", "\n\n\n")

	if ARGS_CHK == True:
		print("Processing input...", "\n\n\n")
	else:
		print("Exit with code 1", "\n\n\n")
		sys.exit(1)

def main(): #main function
	# if DEBUG: 
	# 	storage_path = os.path.join(tempfile.gettempdir(), "storage.data") # not in the current directory

	# if DEBUG:
	# 	print_path(storage_path)
	get_arguments()




main() #start of main function


#with open(storage_path, "w") as file:
