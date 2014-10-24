# Program to check the contents of all files in a given directory structure for 
# occurrences of tokens listed in a provided text file. If a token is found, the
# token, along with the name of the file in which it is found, is written to a
# file called 'results.txt' in the same directory as this program.

import os
import fileinput
import sys

WORKSPACE_DIR = ''
SEARCH_LIST = ''
RESULT_FILE = 'results.txt'

def parse(fileList, searchFile):
	"""
	Method takes a list of files as well as a token source file, and searches
	the list of files for each token in the source file.
	"""
	newFile = open(RESULT_FILE, 'a')
	for token in searchFile:
		token = token.replace('\n', '')
		print "Checking token: " + token
		for f in fileList:
			file = open(f)
			for line in file:
				if line.upper().find(token.upper()) != -1 and not os.path.samefile(f, SEARCH_LIST):
					print 'Found in', f
					newFile.write('Token ' + token + ' found in ' + f + '\n')
					break;
			file.close()	
	newFile.close()

if __name__ == "__main__":
	if len(sys.argv) < 3:
		raise Exception("Usage: python project.py <full/path/to/examine> <full/path/of/search/string/file>")
	WORKSPACE_DIR = sys.argv[1]
	SEARCH_LIST = sys.argv[2]
	fileList = []
	searchFile = open(SEARCH_LIST)
	# Create a list of files, based on the directory path supplied as the
	# first argument
	for dirpath, subFolders, files in os.walk(WORKSPACE_DIR):
		for name in files:
			# Append the directory path onto the name, to get the full path of each file.
			fileList.append(os.path.join(dirpath, name))			
			# Don't include .svn directories
			if '.svn' in subFolders:
				subFolders.remove('.svn')
	# Pass the list of files and the token source file to the parse() method.
	parse(fileList, searchFile)
	searchFile.close()