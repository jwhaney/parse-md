'''
this script will read markdown files from a directory, extract the front matter
fields and values and write them to a csv - field names and values.
'''

import os, re, csv

def main():
    directory = os.getcwd() + "/md_files"
    mdObject = {}
    count = 0
    mdList = []
    fileName
    lineArray = []

    #directory, mdObject, count, mdList, lineArray = declareVariables()
    fileName = getFiles(fileName)
    file, f, line, s = stripIt(file, f, line, s)
    lineArray = organize(lineArray)
    printIt(lineArray)

'''
#declare variables function
def declareVariables():
    directory = os.getcwd() + "/md_files"
    mdObject = {}
    count = 0
    mdList = []
    lineArray = []

    return directory, mdObject, count, mdList, lineArray
    #print("current working directory is: " + directory)

    #getFiles()
'''

#iterate through files in directory; assign file names to fileName variable
def getFiles(fileName):
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.md', '.markdown')):
                fileName = file
                #print(fileName)
    return fileName
    #stripIt()

def stripIt(file, f, line, s):
    file = os.path.join(subdir, file)
    f = open(file, 'r')
    line = f.readline()
    for line in f:
        line = line.strip()
        s = line.find(':')
        print(s)
    return file, f, line, s
    #organize()

def organize(lineArray):
    if s != -1:
        lineArray = line.split(line[s])
        print(lineArray)
        if len(lineArray) > 2:
            lineArray[1] = lineArray[1] + ':' + lineArray[2]
        print(lineArray)
    else:
        pass
    f.close()
    return lineArray

def printIt(lineArray):
    print(lineArray)

#run it
main()
