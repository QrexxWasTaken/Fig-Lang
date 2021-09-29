import os, sys
from source import simplefigloader
from source import randomloader
from time import sleep
global figversion
figversion = "0.5"
global simplefig
simplefig = 0
global randomimport
randomimport = 0

def read(line):
    if "//" in line:
        None
    elif "from system" in line:
        if "import simplefig" in line:
            global simplefig
            if simplefig == 0:
                print(f"Import SimpleFig version {simplefigloader.sfv} from Fig System")
                simpfig = 1
                simplefig = simpfig
            else:
                print("Error: SimpleFig Already imported")
        elif 'import random' in line:
            print(f"Imported Random version {randomloader.rv} from Fig System")
    elif "import" in line:
        if "simplefig" in line:
            simpfig = simplefig
            if simpfig == 0:
                simplefigloader.load()
                simpfig = 1
                simplefig = simpfig
            else:
                print("Error: SimpleFig is already imported")
        elif "random" in line:
            imprand = importrand
            if imprand == 0:
                importrand.load()
                imprand = 1
                importrand = imprand
            else:
                print("Error: Random is already imported")
    elif "sys.out" in line:
        readfinal = line.split("'")
        if ";" in readfinal[2]:
            print(readfinal[1])
        else:
            print("error. ; (semicolon) missing.")
            exit()
    elif "out" in line:
        if simplefig == 1:
            readfinal = line.split("'")
            if ";" in readfinal[2]:
                print(readfinal[1])
            else:
                print("error. ; (semicolon) missing.")
                exit()
        else:
            print("Unknown function 'out'")
    elif "sys.in" in line:
        readfinal = line.split("'")
        if ";" in readfinal[2]:
            var = input(readfinal[1] + "\n")
            print(var)
        else:
            print("error. ; (semicolon) missing.")
    elif "in" in line:
        if simplefig == 1:
            readfinal = line.split("'")
            if ";" in readfinal[2]:
                var = input(readfinal[1] + "\n")
                print(var)
            else:
                print("error. ; (semicolon) missing.")
        else:
            print("Unknown function 'in'")
    elif "sys.wait" in line:
        readfinal = line.split("(")
        if ";" in readfinal[1]:
            readerfinal = readfinal[1].split(")")
            sleep(int(readerfinal[0]))
        else:
            print("Error. ; (semicolon) missing")
    elif "wait" in line:
        if simplefig == 1:
            readfinal = line.split("(")
            if ";" in readfinal[1]:
                readerfinal = readfinal[1].split(")")
                sleep(int(readerfinal[0]))
            else:
                print("Error. ; (semicolon) missing")
        else:
            print("unrecognized function 'wait'")
    elif "random.int" in read:
        if randomimport == 1:
            if ";" in read:
                randomint = random.randint(0,2147483647)
                print(randomint)
        else:
            print("Unknown function 'random.int'")
    elif "int" in read:
        if randomimport == 1:
            if simplefig == 1:
                if ";" in read:
                    print(random.randint(0,2147483647))
            else:
                print("Unknown function 'int'")
        else:
            print("Unknown function 'random.int'")
    elif "random.str" in read:
        if randomimport == 1:
            if ";" in read:
                print(''.join(random.choice(string.ascii_lowercase) for i in range(12)))
        else:
            print("Unknown function 'random.int'")
    elif "str" in read:
        if randomimport == 1:
            if simplefig == 1:
                if ";" in read:
                    print(''.join(random.choice(string.ascii_lowercase) for i in range(12)))
        else:
            print("Unknown function 'random.int'")
class compile:
    file = open("main.fig","r").read()
    file = file.split("\n")
    for i in range(len(file)):
        if(file[i] != ""):
            read(file[i])