from windowsbackup import *


import os.path

MAINPATH = os.path.join(os.getenv('APPDATA'),"Slack/")
PACKFILE = os.path.join(OUTPUTFOLDER, "slack.zip")


def do_pack():
    Archive(MAINPATH).add("storage") \
        .pack(PACKFILE)

        
def do_unpack():
    Archive(MAINPATH).unpack(PACKFILE)
    
    
do_unpack()
    
    