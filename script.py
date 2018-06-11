'''
this script will read markdown files from a directory, extract the front matter
fields and values and write them to a csv - field names and values.
'''

import os, csv

def main():

    directory = os.getcwd() + "/md_files"
    csv_file = os.getcwd() + "/test.csv"
    mdList = []
    lineArray = []
    fieldList = []
    count = 0
    master = {}
    dash = ''

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
                    if line.strip() == "---":
                        dash = str(dash + (count + 1))
                        print(dash)
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

                    # add functionality for scraping all text below '---' for
                    # value of long description key


                master[fileName] = mdObject

    for k, v in master.items():
        for item in v:
            if item not in fieldList:
                fieldList.append(item)

    #add functionality for creating csv from master dictionary
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldList)

        writer.writeheader()

        for k, v in master.items():
            writer.writerow(v)

#run it!
main()
