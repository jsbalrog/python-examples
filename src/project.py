import os
import fileinput
import sys

WORKSPACE_DIR = ''
SEARCH_LIST = ''
RESULT_FILE = 'results.txt'

def parse(fileList, searchFile):
	newFile = open(RESULT_FILE, 'a')
	for token in searchFile:
		token = token.replace('\n', '')
		print "Checking token: " + token
		for f in fileList:
			file = open(f)
			for line in file:
#				print "Checking line: " + line
				if line.find(token) != -1 and not os.path.samefile(f, SEARCH_LIST):
					print "Found in", f
					newFile.write(f)
					newFile.write('\n')
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

	for root, subFolders, files in os.walk(WORKSPACE_DIR):
		for file in files:
			fileList.append(os.path.join(root,file))
			
	parse(fileList, searchFile)
	
	searchFile.close()