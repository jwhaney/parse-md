'''
this script will read markdown files from a directory, extract the front matter
fields and values and write them to a csv - field names and values.
'''

import os, re, csv

def main():

    directory = os.getcwd() + "/md_files"
    mdObject = {}
    count = 0
    bigList = []
    fieldList = []
    mdList = []
    lineArray = []
    master = {}
    multi = []

    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.md', '.markdown')):
                fileName = file
                print(fileName)
                file = os.path.join(subdir, file)
                f = open(file, 'r')
                line = f.readline()

                for line in f:
                    if line.rstrip() == "---":
                        break
                    line = line.rstrip()
                    #print(line)
                    s = line.find(':')
                    lineArray = line.split(line[s])
                    #print(lineArray)

                    #put the urls back together
                    if len(lineArray) > 2:
                        url = ':'.join(lineArray[1:])
                        for x in lineArray[1:]:
                            lineArray.pop()
                        print(lineArray)
                        lineArray.append(url)
                    print(lineArray)

                    for item in lineArray:
                        print(item)
                        #key = item[0]
                        #value = item[1]


                    #print(mdObject)
                    #print(multi)
                    #key = lineArray[0]
                    #value = lineArray[1]
                    #print(value)
                    #print(key, value)
                    #mdList.extend(key,value)
                    #master[mdList]

            print(mdObject)

    '''
    for line in f:
        if line.startswith("---"):
            pass
        elif line.startswith(""):
            descript = "description"
            dValue = line
        else:
            line = line.strip()
            s = line.find(':')
            if s != -1:
                lineArray = line.split(line[s])
        mdList.append(lineArray)

    f.close()
    '''
    #create list of unique field names
    '''
    for x in mdList:
        for i in x:
            if i ==
        fieldList.append(x[0])
    '''
    #print(mdList)
    #print(len(fieldList))
    #print(len(mdList))
    #print(mdList(set(mdList)))

#run it
main()
