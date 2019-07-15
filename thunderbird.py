from windowsbackup import *


import re
import os.path
import configparser


PROFILEFILE = os.path.join(os.getenv('APPDATA'),"Thunderbird/profiles.ini")
MAINPATH = os.path.join(os.getenv('APPDATA'),"Thunderbird/")
PACKFILE = os.path.join(OUTPUTFOLDER, "thunderbird.zip")

def get_profile_folder():
    config = configparser.ConfigParser()
    config.read(PROFILEFILE)
    
    return config['Profile0']["Path"]

def do_pack():
    profile_folder = get_profile_folder()
        

    Archive(MAINPATH).add("profiles.ini") \
        .add( profile_folder, "prefs.js") \
        .addifexist( profile_folder, "user.js") \
        .add( profile_folder, "key3.db") \
        .add( profile_folder, "logins.json") \
        .add( profile_folder, "cert8.db") \
        .pack(PACKFILE)

        
def clean_pref_file():
    profile_folder = get_profile_folder()
    
    preffile = os.path.join(MAINPATH, profile_folder, "prefs.js")
    
    allowed_keys = [
        "mail.account",
        "mail.accountmanager",
        "mail.identity",
        "mail.server",
        "mail.smtpserver",
        "mail.smtpservers"]
        
    remove_keys = ["mail\.server\.*\.directory","mail\.server\.*\.directory-rel"]
       

    lines = []
       
    with open(preffile, "r") as pfile:
        r_lines = pfile.readlines()
        for line in r_lines:
        
            allowed = False
            
            for k in allowed_keys:
                if k in line:
                    allowed = True
                    
            if allowed:
                if not re.search("mail.server.server[0-9]*.directory", line):
                
                    lines += [line]
                
    with open(preffile, "w") as pfile:
        for l in lines:
            pfile.write(l)
            pfile.write("\n")
            
            
    
    
        
def do_unpack():
    Archive(MAINPATH).unpack(PACKFILE)
    
    
    profile_folder = get_profile_folder()
    
    clean_pref_file()
    
    
do_unpack()
    
    