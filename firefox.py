from windowsbackup import *

import re
import os.path
import configparser



PROFILEFILE = os.path.join(os.getenv('APPDATA'),"Mozilla/Firefox/profiles.ini")
MAINPATH = os.path.join(os.getenv('APPDATA'),"Mozilla/Firefox/")
PACKFILE = os.path.join(OUTPUTFOLDER, "firefox.zip")

def get_profile_folder():
    config = configparser.ConfigParser()
    config.read(PROFILEFILE)
    
    return config['Profile0']["Path"]

def do_pack():
    profile_folder = get_profile_folder()
        

    Archive(MAINPATH).add("profiles.ini") \
        .add( profile_folder, "places.sqlite") \
        .pack(PACKFILE)
            
            
    
    
        
def do_unpack():
    Archive(MAINPATH).unpack(PACKFILE)
    
    
    
#do_pack()   
do_unpack()
    
    