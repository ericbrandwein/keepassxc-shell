#!/usr/bin/env python3

import argparse
import sys
import getpass
from subprocess import Popen, PIPE, STDOUT
import shlex

parser = argparse.ArgumentParser(
	description='Shell for keepassxc-cli, '
	'so you don\'t have to put the password every time.')
parser.add_argument('database', help='Path to the database')

args = parser.parse_args()
if len(sys.argv) < 2:
	print("No database selected.")
	sys.exit(1)

database = sys.argv[1]
passwordMesssage = "Insert password for {}: ".format(database)
password = getpass.getpass(passwordMesssage)

keepassxcBinary = "keepassxc-cli"


def parseCommand(requested):
	arguments = shlex.split(requested)
	command = [keepassxcBinary]
	if arguments[0] in ['', 'help', '?']:
		command.append('--help')
	else:
		command += [arguments[0], database]

	if len(arguments) > 1:
		command += arguments[1:]

	return command


while True:
	command = parseCommand(input('KeepassXC> '))
	process = Popen(command, stdin=PIPE)
	process.communicate(input=bytes(password, 'utf-8'))
	print()
