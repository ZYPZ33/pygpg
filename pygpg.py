#!/usr/bin/env python3
from os import name, listdir, system as runsh
from subprocess import check_output
from getpass import getpass
from sys import argv
if name != "posix":
    print("Sorry, this is only going to work on a posix system")
    exit()

def clear():
    _=runsh('clear')

def run(argv):
    file = argv[len(argv)-1]
    if file == '.':
        print("ERROR: Requires a filename")
        exit()

    if file not in listdir():
        print("ERROR: File does not exist")
        exit()
    if runsh("command -v file"):
        print("ERROR: Requires file command")
    
    clear()
    type = check_output(f"file {file}", shell=True)
    if "Zip" not in type and "GPG" not in type:
        print("Not a Zip archive or GPG file")
    password = getpass('Enter Password: ')
    if "GPG" in type:
        _ = runsh(f"gpg {file} --passphrase {password}")
    else:
        _ = runsh(f"unzip {file} -P {password}")
    
        # Valid values: Zip* & GPG&
        # use file to check if is zip or gpg
        # unzip {file} -P {password}
        # gpg {file} --passphrase {password}

if __name__ == "__main__":
    run(argv)
