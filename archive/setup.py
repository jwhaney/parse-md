# module to get path, variables, etc for setup

def set_up():
    directory = input(os.getcwd("enter relative path to your markdown files: "))
    csv_file = input(os.getcwd("name your csv file output: "))

    lineArray = []
    fieldList = []
    master = {}


class parseMd(object):
    def __init__(self, directory, csv_file):
        self.directory = directory
        self.csv_file = csv_file
