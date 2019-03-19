""" Program: filesys.py
    Author: Malachi Perrin
    Date: 3/19/19

Provide a menu-driven tool for navigating a file system and gathering information on files.
"""

import os, os.path

# Constants for this program
QUIT = '7'
COMMANDS = ('1', '2', '3', '4', '5', '6', '7')
MENU = """1 List the current directory
2 Move up
3 Move down
4 Number of files in the directory
5 Size of the directory in bytes
6 Search for a filename
7 Quit the program"""

# Main function will handle input, output and calls to other functions
def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print("Have a nice day!")
            break

# This acceptCommand() function gets fired off by main()
def acceptCommand():
    """Inputs and returns a legitimate command number"""
    command = input("Enter a number: ")
    if command in COMMANDS:
        return command
    else:
        print("Error: Command not recognized")
        return acceptCommand()

# This runCommand function also gets fired off by main()
def runCommand(command):
    """ Selects and runs a command."""
    if command == '1':
        listCurrentDir(os.getcwd())
    elif command == '2':
        moveUp()
    elif command == '3':
        moveDown(os.getcwd())
    elif command == '4':
        print("The total number of files is", countFiles(os.getcwd()))
    elif command == '5':
        print("The total number of bytes is", countBytes(os.getcwd()))
    elif commmand == '6':
        target = input("Enter the search string: ")
        fileList = findFiles(target, os.getcwd())
        if not fileList:
            print("Error: String not found")
        else:
            for file in fileList:
                print(file)

# These are all the functions called by runCommand()
def listCurrentDir(dirName):
    """Prints a list of the cwd's contents"""
    l = os.listdir(dirName) # l = list
    for element in l:
        print(element)

def moveUp():
    """Moves up to the parent directory"""
    os.chdir("..")

def moveDown(currentDir):
    """Moves down to the named subdirectory if it exists."""
    newDir = input("Enter the directory name: ")
    if os.path.exists(currentDir + os.sep + newDir) and os.path.isdir(newDir):
        os.chdir(newDir)
    else:
        print("Error: no such directory")

def countFiles(path):
    """Returns the number of files in the cwd and all its subdirectories"""
    count = 0
    l = os.listdir(path) # l = list
    for element in l:
        if os.path.isfile(element):
            count += 1
        else:
            os.chdir(element)
            count += countFiles(os.getcwd())
            os.chdir("..")
        return count

def countBytes(path):
    """Returns the number of bytes in the cwd and all its subdirectories"""
    count = 0
    l = os.listdir(path) # l = list
    for element in l:
        if os.path.isfile(element):
            count += os.path.getsize(element)
        else:
            os.chdir(element)
            count += countBiles(os.getcwd())
            os.chdir("..")
        return count

def findFiles(target, path):
    """Returns a list of the filenames that contain the target string in the cwd and all of its subdirectories."""
    files = []
    l = os.listdir(path)
    for element in l:
        if os.path.isfile(element):
            if target in element:
                files.append(path + os.sep + element)
            else:
                os.chdir(element)
                files.extend(findFiles(target, os.getcwd()))
                os.chdir("..")
        return files

main()
