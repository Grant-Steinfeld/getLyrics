#convert files under into valid python dictionaries

import json
import os
from fnmatch import fnmatch

class Transformer():
    def __init__(self, start='gn', pattern="*.txt"):
        files = self.getFiles(start,pattern)



    def turnIntoDict(self, filePath):

        contents = None
        strPy = None
        with open(filePath,'r') as f:
            contents = f.read()
            #print contents[0:250]
            strPy = "contents={}".format(contents)
            strPy = strPy + "\r\n if __name__ == '__main__': \r\n \t print contents"

        with open( filePath.replace('txt','py'),'w') as newfile:
            newfile.write(strPy)




    def getFiles(self, start, pattern):
        cd = os.getcwd()
        root = os.path.join(cd,start)
        for path, subdirs, files in os.walk(root):
            for name in files:
                if fnmatch(name, pattern):
                    filePath = os.path.join(path, name)
                    self.turnIntoDict(filePath)


if __name__ == '__main__':
    t = Transformer()
