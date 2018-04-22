#!/usr/bin/env python3

import argparse
import sys
import getpass
from subprocess import Popen, PIPE, STDOUT


parser = argparse.ArgumentParser(
	description='Shell for keepassxc-cli, '
	'so you don\'t have to put the password every time.')
parser.add_argument('database', help='Path to the database')

args = parser.parse_args()
if len(sys.argv) < 2:
	print("No database selected.")
	sys.exit(1)

database = sys.argv[1]
password = getpass.getpass("Insert password: ")

keepassxcBinary = "keepassxc-cli"


def getNextCommand():
	requested = input('> ').split(' ', 1)
	command = [keepassxcBinary]
	if requested[0] in ['help', '?']:
		command.append('--help')
	else:
		command += [requested[0], database]

	if len(requested) > 1:
		command.append(requested[1])

	return command


while True:
	process = Popen(getNextCommand(), stdin=PIPE)
	process.communicate(input=bytes(password, 'utf-8'))
	print()
