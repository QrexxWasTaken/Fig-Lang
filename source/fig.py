import os, sys, random, string
from source import simplefigloader
from source import randomloader
from time import sleep
global figversion
figversion = "0.5"
global simplefig
simplefig = 0
global randomimport
randomimport = 0

def line(line):
    global randomimport
    global simplefig
    if "//" in line:
        None
    elif "from system" in line:
        if "import simplefig" in line:
            if simplefig == 0:
                print(f"Import SimpleFig version {simplefigloader.sfv} from Fig System")
                simpfig = 1
                simplefig = simpfig
            else:
                print("Error: SimpleFig Alliney imported")
        elif 'import random' in line:
            if randomimport == 0:
                print(f"Imported Random version {randomloader.rv} from Fig System")
                randomimport = 1
            else:
                print(f"Error: Random Already imported")
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
            imprand = randomimport
            if imprand == 0:
                randomloader.load()
                randomimport = 1
            else:
                print("Error: Random is already imported")
    elif "sys.out" in line:
        linefinal = line.split("'")
        if ";" in linefinal[2]:
            print(linefinal[1])
        else:
            print("error. ; (semicolon) missing.")
            exit()
    elif "out" in line:
        if simplefig == 1:
            linefinal = line.split("'")
            if ";" in linefinal[2]:
                print(linefinal[1])
            else:
                print("error. ; (semicolon) missing.")
                exit()
        else:
            print("Unknown function 'out'")
    elif "sys.in" in line:
        linefinal = line.split("'")
        if ";" in linefinal[2]:
            var = input(linefinal[1] + "\n")
            print(var)
        else:
            print("error. ; (semicolon) missing.")
    elif "in" in line:
        if simplefig == 1:
            linefinal = line.split("'")
            if ";" in linefinal[2]:
                var = input(linefinal[1] + "\n")
                print(var)
            else:
                print("error. ; (semicolon) missing.")
        else:
            print("Unknown function 'in'")
    elif "sys.wait" in line:
        linefinal = line.split("(")
        if ";" in linefinal[1]:
            lineerfinal = linefinal[1].split(")")
            sleep(int(lineerfinal[0]))
        else:
            print("Error. ; (semicolon) missing")
    elif "wait" in line:
        if simplefig == 1:
            linefinal = line.split("(")
            if ";" in linefinal[1]:
                lineerfinal = linefinal[1].split(")")
                sleep(int(lineerfinal[0]))
            else:
                print("Error. ; (semicolon) missing")
        else:
            print("unrecognized function 'wait'")
    elif "random.int" in line:
        if randomimport == 1:
            if ";" in line:
                randomint = random.randint(0,2147483647)
                print(randomint)
        else:
            print("Unknown function 'random.int'")
    elif "int" in line:
        if randomimport == 1:
            if simplefig == 1:
                if ";" in line:
                    print(random.randint(0,2147483647))
            else:
                print("Unknown function 'int'")
        else:
            print("Unknown function 'random.int'")
    elif "random.str" in line:
        if randomimport == 1:
            if ";" in line:
                print(''.join(random.choice(string.ascii_lowercase) for i in range(12)))
        else:
            print("Unknown function 'random.str'")
    elif "str" in line:
        if randomimport == 1:
            if simplefig == 1:
                if ";" in line:
                    print(''.join(random.choice(string.ascii_lowercase) for i in range(12)))
        else:
            print("Unknown function 'str'")
class compile:
    file = open("main.fig","r").read()
    file = file.split("\n")
    for i in range(len(file)):
        if(file[i] != ""):
            line(file[i])