import argparse
import sys
import os
import re


# parse command line arguments
parser = argparse.ArgumentParser(description='Parse a pdbripper file and write the contents to files')
parser.add_argument('file', help='the file to parse')
parser.add_argument('struct', help='the class to find. Alternatively specifies the prefix if -prefix is specified')
parser.add_argument('-p', '--prefix', action='store_true', help='parse all classes with a specific prefix')
parser.add_argument('-s', '--outputsingle', action='store_true', help='output the contents to a single file')
parser.add_argument('-v', '--verbose', action='store_true', help='print out the classes as they are parsed')
args = parser.parse_args()



print(args.file)
print(args.struct)
print(args.prefix)
print(args.verbose)
print(args.outputsingle)

