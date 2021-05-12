import sys
import hive

def save(): 
    sys.stdout = open("log.txt", "w")
    sys.stdout.close()
    exit
