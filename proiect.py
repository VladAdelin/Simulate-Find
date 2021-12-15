
import re
import sys

from os import path, listdir


def compareFileName(pcFile, searchFile):
    if '.' in searchFile:
        searchFile = searchFile.replace(".", "\\.")
        searchFile = "^(" + searchFile + ')$'
    if '*' in searchFile:
        searchFile = searchFile[:searchFile.find("*")] + "." + searchFile[searchFile.find("*"):]
    if re.match(str.encode(searchFile), str.encode(pcFile)) is not None:
        return True
    return False


def find(directory, file):
    searchFileHasExtencion = False
    if path.exists(directory):
        try:
            if path.splitext(file)[1] != "":
                searchFileHasExtencion = True

            for item in listdir(directory):
                name, extension = path.splitext(item)
                if extension != "" and searchFileHasExtencion:
                    if compareFileName(item, file):
                        print(directory + "\\" + item)
                else:
                    if not searchFileHasExtencion:
                        if name == file:
                            print(directory + "\\" + file)
                    find(directory + "\\" + name, file)
        except:
            # access is denied
            #print("Acces is denied")
            pass



def main():
    params = sys.argv
    if len(params) != 3:
        print("This command requires 2 parameters!")

    else:
        directory = params[1]
        file = params[2]
        find(directory, file)


main()