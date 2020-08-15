import os
import tempfile
import json
import argparse
import sys

DEBUG = True


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

def add_to_storage(key, value):

	data = {key:value}

	if DEBUG:
		with open ("debug_storage.data", "a") as debug_storage:
			json.dump(data, debug_storage)

	#storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

	#with open(storage_path, 'w') as file:
	#	json.dump(data, file)


#def retrieve_from_storage(key):




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

		add_to_storage(args.key, args.value)

	elif (args.key and args.value == None):
		ARGS_CHK = True # input OK

		if DEBUG:
			print("key passed")
			print("key: ", args.key, "\n\n\n")

		retrieve_from_storage(args.key)

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

	get_arguments()




main() #start of main function


#with open(storage_path, "w") as file:
