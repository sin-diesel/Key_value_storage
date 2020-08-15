import os
import tempfile
import json
import argparse

DEBUG = True


def print_path(storage_path):
	print("Storaga path is: ", storage_path)


def main():
	storage_path = os.path.join(tempfile.gettempdir(), "storage.data") # not in the current directory

	if DEBUG:
		print_path(storage_path)




main()


#with open(storage_path, "w") as file:
