'''
this script will read markdown files from a sub-directory, extract the front matter
key/values, and write them to a csv using only unique keys for fields.
'''

import os, csv

def main():
    # get current working directory + subdirectory of markdown files and create
    # empty csv to write to later.
    directory = os.getcwd() + "/md_files/test_batch"
    csv_file = os.getcwd() + "/master.csv"

    lineArray = []
    fieldList = []
    master = {}

    # iterate through markdown files in subdirectory
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            # test to make sure all files in subdirectory are markdown
            if file.endswith(('.md', '.markdown')):
                hold = []
                fileName = file
                print(fileName)
                # open and read each markdown file line by line
                file = os.path.join(subdir, file)
                f = open(file, 'r')
                line = f.readline()

                mdObject = {}

                for line in f:
                    # catch line with dashes and scoop up all text at the bottom
                    # to use in the description key/field
                    if line.startswith("---"):
                        for line in f:
                            hold.append(line.strip())
                            mdObject["description"] = ''.join(hold)
                        break

                    # if line doesn't have dashes, split line at colon and then
                    # populate list for each line (lineArray)
                    line = line.strip()
                    s = line.find(':')
                    lineArray = line.split(line[s])

                    # splitting by colon separates urls, so put them back
                    # together here
                    if len(lineArray) > 2:
                        url = ':'.join(lineArray[1:])
                        for x in lineArray[1:]:
                            lineArray.pop()
                        lineArray.append(url)

                    # create dict for each file using lineArray
                    mdObject[lineArray[0]] = lineArray[1]

                # use filename as key for each nested file dict
                master[fileName] = mdObject

    # iterate through master dict, populate fieldList with only unique names
    for k, v in master.items():
        for item in v:
            if item not in fieldList:
                fieldList.append(item)

    # create csv from master dictionary and use unique field names from fieldList
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldList)
        writer.writeheader()
        for k, v in master.items():
            writer.writerow(v)

#run it!
main()
