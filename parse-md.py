'''
this script will read markdown files from a sub-directory, extract the front matter
key/values, and write them to a csv using only unique keys for fields.

author: john haney
date: june, 2018
'''

import os, csv

class ParseMd(object):

    def __init__(self, directory, csv_file, lineArray, fieldList, master):
        self.directory = directory
        self.csv_file = csv_file
        self.lineArray = lineArray
        self.fieldList = fieldList
        self.master = master

    # iterate through markdown files in directory
    def workhorse(self):
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
    def field_pop(self):
        for k, v in master.items():
            for item in v:
                if item not in fieldList:
                    fieldList.append(item)

    # create csv from master dictionary and use unique field names from fieldList
    def output_csv(self):
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldList)
            writer.writeheader()
            for k, v in master.items():
                writer.writerow(v)


if __name__ == '__main__':
    print("starting to parse markdown files...")

    # get current working directory + subdirectory of markdown files and create empty csv to write to later.
    # edit this path and file name to whatever you choose.
    directory = os.getcwd() + "/md_files"
    csv_file = os.getcwd() + "/master.csv"

    # create variables to be used later; do not change these
    lineArray = []
    fieldList = []
    master = {}

    # initialize
    app = ParseMd(directory, csv_file, lineArray, fieldList, master)

    # run it
    print("riding the workhorse...")
    app.workhorse()
    print("populating fields...")
    app.field_pop()
    print("creating output csv...")
    app.output_csv()
    print("completed successfully.")
