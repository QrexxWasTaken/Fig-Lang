import random
from time import sleep
import os
sfv = "0.7"
kb = ["45","355","133","448","846"]

def load():
    kb2 = random.choice(kb)
    global s
    if kb2 == 846:
        s = 0.1
    elif kb2 == 448:
        s = 0.2
    elif kb2 == 355:
        s = 0.3
    elif kb2 == 133:
        s = 0.8
    else:
        s = 1
    print(">> fig -i main.fig \ninstall simplefig --import")
    sleep(2)
    os.system("clear")
    print(">> fig -i main.fig \ninstall simplefig --import")
    print("Fig Package Installer |------")
    sleep(s)
    os.system("clear")
    print(">> fig -i main.fig \ninstall simplefig --import")
    print("Fig Package Installer ||-----")
    sleep(s)
    os.system("clear")
    print(">> fig -i main.fig \ninstall simplefig --import")
    print("Fig Package Installer |||----")
    sleep(s)
    os.system("clear")
    print(">> fig -i main.fig \ninstall simplefig --import")
    print("Fig Package Installer ||||---")
    sleep(s)
    os.system("clear")    
    print(">> fig -i main.fig \ninstall simplefig --import")
    print("Fig Package Installer |||||--")
    sleep(s)
    os.system("clear")
    print(">> fig -i main.fig \ninstall simplefig --import")
    print("Fig Package Installer ||||||-")
    sleep(s)
    os.system("clear")
    print(">> fig -i main.fig \ninstall simplefig --import")
    print("Fig Package Installer |||||||")
    sleep(s)
    os.system("clear")
    print(">> fig -i main.fig \ninstall simplefig --import")
    print(f"Successfully Imported SimpleFig Version {sfv}\nWith a speed of {kb2}kb/s")
    sleep(4)
    os.system("clear")