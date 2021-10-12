import os, sys, random, string
from source import simplefigloader
from source import randomloader
from source import mathloader
from time import sleep
global figversion
figversion = "1.1.0"
global simplefig
simplefig = 0
global randomimport
randomimport = 0
global mathimport
mathimport = 0

global inIf
inIf = False

variables = {

}

def addvar(name,value):
    variables[name] = value

def line(line):
    global randomimport
    global simplefig
    global mathimport
    global inIf
    if "//" in line:
        None
    elif "from system" in line:
        if "import simplefig" in line:
            if simplefig == 0:
                print(f"Import SimpleFig version {simplefigloader.sfv} from Fig System")
                simpfig = 1
                simplefig = simpfig
            else:
                print("Error: SimpleFig Already imported")
        elif 'import random' in line:
            if randomimport == 0:
                print(f"Imported Random version {randomloader.rv} from Fig System")
                randomimport = 1
            else:
                print(f"Error: Random Already imported")
        elif "import math" in line:
            if mathimport == 0:
                print(f"Imported Math version {mathloader.mv} from Fig System")
                mathimport = 1
            else:
                print("Error: Math Already imported")
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
        elif "math" in line:
            impmath = mathimport
            if impmath == 0:
                mathloader.load()
                mathimport = 1
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
    elif "sys.input" in line:
        linefinal = line.split("'")
        if ";" in linefinal[2]:
            var = input(linefinal[1] + "\n")
            print(var)
        else:
            print("error. ; (semicolon) missing.")
    elif "input" in line:
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
    elif "sys.setvar" in line:
        linefinal = line.split("(")
        lineefinal = linefinal[1].split(",")
        lineerfinal = lineefinal[1].split(")")
        linerfinal = [lineerfinal,lineefinal[0]]
        if ";" in linerfinal[0][1]:
            addvar(str(linerfinal[1]),str(linerfinal[0][0]))
            print("Set variable",'"'+str(linerfinal[1])+'"',"to",variables[str(linerfinal[1])])
        else:
            print("Error: missing ; (semicolon)")
    elif "setvar" in line:
        if simplefig == 1:
            linefinal = line.split("(")
            lineefinal = linefinal[1].split(",")
            lineerfinal = lineefinal[1].split(")")
            linerfinal = [lineerfinal,lineefinal[0]]
            if ";" in linerfinal[0][1]:
                addvar(str(linerfinal[1]),str(linerfinal[0][0]))
                print("Set variable",'"'+str(linerfinal[1])+'"',"to",variables[str(linerfinal[1])])
            else:
                print("Error: missing ; (semicolon)")
        else:
            print("Unknown function 'setvar'")
    elif "sys.getvar" in line:
        linefinal = line.split("(")
        lineefinal = linefinal[1].split(")")
        if ";" in lineefinal[1]:
            print(variables[lineefinal[0]])
        else:
            print("Error: missing ; (semicolon)")
    elif "getvar" in line:
        if simplefig == 1:
            linefinal = line.split("(")
            lineefinal = linefinal[1].split(")")
            if ";" in lineefinal[1]:
                print(variables[lineefinal[0]])
            else:
                print("Error: missing ; (semicolon)")
        else:
            print("Unknown function 'getvar'") 
    elif "sys.vars" in line:
        if ";" in line:
            print("Defined Variables:")
            for i in variables:
                print(str(i)+": "+str(variables[i]))
            print("")
        else:
            print("Error: missing ';' (semicolon)")
    elif "vars" in line:
        if simplefig == 1:
            if ";" in line:
                print("Defined Variables:")
                for i in variables:
                    print(str(i)+": "+str(variables[i]))
                print("")
            else:
                print("Error: missing ';' (semicolon)")
        else:
            print("Unknown function 'vars'")
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
    elif "math.add" in line:
        if mathimport == 1:
            linefinal = line.split("(")
            if ";" in linefinal[1]:
                linerfinal = linefinal[1].split(")")
                lineerfinal = linerfinal[0].split(",")
                print(int(lineerfinal[0])+int(lineerfinal[1]))
        else:
            print("Unknown function 'math.add'")
    elif "math.sub" in line:
        if mathimport == 1:
            linefinal = line.split("(")
            if ";" in linefinal[1]:
                linerfinal = linefinal[1].split(")")
                lineerfinal = linerfinal[0].split(",")
                print(int(lineerfinal[0])-int(lineerfinal[1]))
        else:
            print("Unknown function 'math.sub'")
    elif "math.div" in line:
        if mathimport == 1:
            linefinal = line.split("(")
            if ";" in linefinal[1]:
                linerfinal = linefinal[1].split(")")
                lineerfinal = linerfinal[0].split(",")
                print(int(lineerfinal[0])/int(lineerfinal[1]))
        else:
            print("Unknown function 'math.div'")
    elif "math.mult" in line:
        if mathimport == 1:
            linefinal = line.split("(")
            if ";" in linefinal[1]:
                linerfinal = linefinal[1].split(")")
                lineerfinal = linerfinal[0].split(",")
                print(int(lineerfinal[0])*int(lineerfinal[1]))
        else:
            print("Unknown function 'math.mult'")
    elif "mult" in line:
        if simplefig == 1:
            if mathimport == 1:
                linefinal = line.split("(")
                if ";" in linefinal[1]:
                    linerfinal = linefinal[1].split(")")
                    lineerfinal = linerfinal[0].split(",")
                    print(int(lineerfinal[0])*int(lineerfinal[1]))
            else:
                print("Unknown function 'mult'")
        else:
            print("Unknown function 'mult'")
    elif "div" in line:
        if simplefig == 1:
            if mathimport == 1:
                linefinal = line.split("(")
                if ";" in linefinal[1]:
                    linerfinal = linefinal[1].split(")")
                    lineerfinal = linerfinal[0].split(",")
                    print(int(lineerfinal[0])/int(lineerfinal[1]))
            else:
                print("Unknown function 'div'")
        else:
            print("Unknown function 'div'")
    elif "add" in line:
        if simplefig == 1:
            if mathimport == 1:
                linefinal = line.split("(")
                if ";" in linefinal[1]:
                    linerfinal = linefinal[1].split(")")
                    lineerfinal = linerfinal[0].split(",")
                    print(int(lineerfinal[0])+int(lineerfinal[1]))
            else:
                print("Unknown function 'add'")
        else:
            print("Unknown function 'add'")
    elif "sub" in line:
        if simplefig == 1:
            if mathimport == 1:
                linefinal = line.split("(")
                if ";" in linefinal[1]:
                    linerfinal = linefinal[1].split(")")
                    lineerfinal = linerfinal[0].split(",")
                    print(int(lineerfinal[0])+int(lineerfinal[1]))
            else:
                print("Unknown function 'sub'")
        else:
            print("Unknown function 'sub'")
    elif "math.pow" in line:
        if mathimport == 1:
            linefinal = line.split("(")
            if ";" in linefinal[1]:
                linerfinal = linefinal[1].split(")")
                lineerfinal = linerfinal[0].split(",")
                print(int(lineerfinal[0])**int(lineerfinal[1]))
        else:
            print("Unknown function 'math.pow'")
    elif "pow" in line:
        if simplefig == 1:
            if mathimport == 1:
                linefinal = line.split("(")
                if ";" in linefinal[1]:
                    linerfinal = linefinal[1].split(")")
                    lineerfinal = linerfinal[0].split(",")
                    print(int(lineerfinal[0])**int(lineerfinal[1]))
            else:
                print("Unknown function 'pow'")
        else:
            print("Unknown function 'pow'")
class compile:
    file = open("main.fig","r").read()
    file = file.split("\n")
    for i in range(len(file)):
        if(file[i] != ""):
            line(file[i])