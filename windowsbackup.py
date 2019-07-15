import re
import os.path
import zipfile
import configparser

OUTPUTFOLDER = "output"

class Archive:

    def __init__(self, wdir = "."):
        self.files = []
        self.wdir = wdir
        
    def add(self, *kwargs):
        file = os.path.join(*kwargs)
        
        self.files += [file]
    
        return self
        
    def addifexist(self, *kwargs):
        file = os.path.join(*kwargs)
        
        if os.path.isfile(file):
            self.add(*kwargs)
        return self
        
    def pack(self, name):
        with zipfile.ZipFile(name, 'w') as myzip:
            olddir = os.getcwd()
            os.chdir(self.wdir)
            for file in self.files:
                myzip.write(file)
                
            os.chdir(olddir)
                
    def unpack(self, name):
        with zipfile.ZipFile(name, 'r') as myzip:
            olddir = os.getcwd()
            os.chdir(self.wdir)
            myzip.extractall()
            os.chdir(olddir)
        
