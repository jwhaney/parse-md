'''
this script will read markdown files from a directory, extract the front matter
fields and values and write them to a csv - field names and values.
'''

import os, csv

def main():

    directory = os.getcwd() + "/md_files"
    csv_file = os.getcwd() + "/test.csv"

    lineArray = []
    fieldList = []
    hold = []
    addThis = []
    master = {}

    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.md', '.markdown')):
                fileName = file
                print(fileName)
                file = os.path.join(subdir, file)
                f = open(file, 'r')
                line = f.readline()

                mdObject = {}

                for line in f:
                    if line.startswith("---"):
                        for line in f:
                            hold.append(line.strip())
                        mdObject["description"] = ''.join(hold)
                        break

                    line = line.strip()
                    s = line.find(':')
                    lineArray = line.split(line[s])

                    # put the urls back together
                    if len(lineArray) > 2:
                        url = ':'.join(lineArray[1:])
                        for x in lineArray[1:]:
                            lineArray.pop()
                        lineArray.append(url)

                    mdObject[lineArray[0]] = lineArray[1]
                    #mdObject['description'] = addThis[0]

                master[fileName] = mdObject

    for k, v in master.items():
        for item in v:
            if item not in fieldList:
                fieldList.append(item)

    #create csv from master dictionary and unique field names from fieldList
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldList)
        writer.writeheader()
        for k, v in master.items():
            writer.writerow(v)

#run it!
main()
