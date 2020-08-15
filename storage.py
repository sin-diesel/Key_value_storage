import os
import tempfile
import json
import argparse

DEBUG = True


def print_path(storage_path):
	print("Storage path is: ", storage_path)

def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("--key")
	parser.add_argument("--value")
	args = parser.parse_args()
	if DEBUG:
		if (args.key and args.value):
			print("both key and val arguments passed")
		if (args.key):
			print("key argument passed")
		if (args.value):
			print("value argument passed")
		else:
			print("None of the arguments were passed")


def main(): #main function
	# if DEBUG: 
	# 	storage_path = os.path.join(tempfile.gettempdir(), "storage.data") # not in the current directory

	# if DEBUG:
	# 	print_path(storage_path)
	get_arguments()




main() #start of main function


#with open(storage_path, "w") as file:
