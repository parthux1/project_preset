"""
Command line script for expanding markdown references.
Text refering to a header of another file will be linked to it.
1. Scan all passed files and register their header names
2. SCan all text-paragraphes for header-names and replace them with references
"""

import sys
import os
import re

########
#config#
########

# output dir
_dir = "autoref_out"


###############
# script start#
###############

files = []
help_str = """
-h --help 		shows this text
-f --files		1 or more files which should be modified. These values will be saved as exp_[filename]
"""

# current state of the statemachine
prearg_current = ''

# used for aborting argument parser
def panic(arg: str):
	"""
	Prints state information and aborts the script
	"""
	print(f'Invalid argument "{arg}" with preargument {prearg_current} found.\
	For more information use --help.')
	sys.exit()

resolvable = ['-h', '--help',
			  '-f', '--files']

# current replacement-dictfile
# will link dict-files to textfiles
files = []

######################################
# statemachine for handling arguments#
######################################
for i, arg in enumerate(sys.argv[1:]):

	# maybe change state if arg is resolvable
	if arg in resolvable:
		if arg == '-h' or arg == '--help':
			print(help_str)
		else:
			prearg_current = arg

	# try to handle input according to current state
	else:
		# map file to current replacement-dict
		if prearg_current == '-f' or prearg_current == '--files':
			files.append(arg)	

		else:
			panic(arg)

###################################
# Step 1. generate header reference
# Pair (text, source)
headers = []

def register_matches(matches:list, filename:str):
	for _match in matches:
		headers.append((_match, filename))

def read_file(filename:str):
	return open(filename, 'r').read()

for filename in files:
	content = read_file(filename)

	#########################
	# locate markdown headers
	regex_header = re.compile(r'#{1,4} [\w\d# -äöüß]*')
	
	matches = re.findall(regex_header, content)

	# preprocess: compile to-string and cleanse #+
	matches = [re.search(r'\w[\w -äöüß]*', _match)[0] for _match in matches]

	register_matches(matches, filename)
	
	########
	# Titles
	regex_title = re.compile(r'[\w -äöüß]*\n=+')
	matches = re.findall(regex_title, content)
		
	# preprocess: remove prev. filtered \n=+
	matches = [re.match(r'[\w -äöüß]*', _match)[0] for _match in matches]

	register_matches(matches, filename)

print(f'Resolved {len(headers)} headers:\n{headers}')

################################################
# 2. Replace References for all non-source files

os.mkdir(_dir)

for filename in files:
	content = read_file(filename) 
	
	file_out_name = os.path.basename(filename)
	file_out_loc = _dir + '/' + file_out_name

	# check for each key in fulltext
	for key, source in headers:
		

		src_stripped = os.path.basename(source)

		# don't modify source file so we can link against somethin	
		if src_stripped == file_out_name:
			continue

		# if not aborted replace with linker
		# build markdown-ref string
		hit_amount = len(re.findall(key, content))
	
		# TODO: trying to ref with file#section does currently not work
		ref = f'[{key}](doc/autoref_out/{src_stripped})'##{key.lower().replace(" ", "-")})'

		if hit_amount > 0:

			print(f'applying key:{key} with ref:{ref}')

			# only hit on whole words
			content = re.sub(r'\b' + key + r'\b', ref, content)
			

	# save content at choosen location
	with open(file_out_loc, 'w+') as f_out:
		print(f'saving at {file_out_loc}')

		f_out.write(content)

	
