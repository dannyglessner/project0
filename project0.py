def WB(out, cyclecount):
    if (len(str(cyclecount+5)) == 2):
        out.write(","+str(cyclecount+5) + "\n")
    else:
        out.write(",0" + str(cyclecount+5) + "\n")
    return 0
def issue(out, cyclecount):
    if (len(str(cyclecount+4)) == 2):
        out.write(","+str(cyclecount + 4))
    else:
        out.write(",0" + str(cyclecount+4))
    return 0
def dispatch(out, cyclecount):
    if (len(str(cyclecount+3)) == 2):
        out.write(","+str(cyclecount + 3))
    else:
        out.write(",0" + str(cyclecount+3))
    return 0
def rename():
    if (len(str(cyclecount+2)) == 2):
	out.write(","+str(cyclecount + 2))
    else:
	out.write(",0" + str(cyclecount+2))
def Decode(instruction, reg1, reg2, dest, cyclecount, out):
    instruction = instruction.split(",") #split the instruction by commas
    instruction[3] = instruction[3].replace("\n", "")
    inst1 = int(instruction[1])
    inst2 = int(instruction[2])
    inst3 = int(instruction[3])
    if ((instruction[0] == "R" and (inst1 != int(dest) and inst2 != int(dest) and inst3 != int(dest)))): #if the dest register is being used again there is a fault (only R type)
        dest = int(instruction[1]) #dest for rtype
        reg1 = int(instruction[2]) #reg1 for rtype
        reg2 = int(instruction[3]) #reg2 for rtype
        imm = -1
    elif (instruction[0] == "L" and (inst3 != int(dest))):
        dest = int(instruction[1])
        imm1 = int(instruction[2])
        reg1 = int(instruction[3])
        reg2 = -1
    elif (instruction[0] == "I"):
        dest = int(instruction[1])
        reg1 = int(instruction[2])
        imm1 = int(instruction[3])
        reg2 = -1
    elif (instruction[0] == "S" and (inst3 != int(dest))):
        reg1 = int(instruction[1])
        imm1 = int(instruction[2])
        reg2 = int(instruction[3])
        dest = -1 
    else:
        if (instruction[0] == "R"): #to find instruction type
            dest = int(instruction[1])
            reg1 = int(instruction[2])
            reg2 = int(instruction[3])
            imm = -1
            cyclecount+=1
        elif (instruction[0] == "L"):
            dest = int(instruction[1])
            imm1 = int(instruction[2])
            reg1 = int(instruction[3])
            reg2 = -1
            cyclecount+=1
        elif (instruction[0] == "S"):
            reg1 = int(instruction[1])
            imm1 = int(instruction[2])
            reg2 = int(instruction[3])
            dest = -1
            cyclecount+=1
    if (len(str(cyclecount+1)) == 2):
        out.write(","+str(cyclecount + 1))
    else:
        out.write(",0" + str(cyclecount+1))
    return dest, cyclecount

def Fetch(file, out, cyclecount):
    instruction = file.readline() #read the next instruction
    if (len(str(cyclecount)) == 2):
        out.write(str(cyclecount))
    else:
        out.write("0" + str(cyclecount))
    return instruction

def initStructuresAndCounts():
    file = open("test.in", "r") #open input file
    out = open("out.txt", "w") # open output file
    cyclecount = 0 #initialize cyclecount to 0
    completedInsts = 0 #initialize completed instances to 0
    icount = len(file.readlines()) #icount = amount of lines in input file
    reg1 = -1
    reg2 = -1
    dest = -1 #initialize register values

#we are taking in a file that holds 
def main():#argc, argv):
    file = open("test.in", "r") #open input file
    out = open("out.txt", "w") # open output file
    cyclecount = 0 #initialize cyclecount to 0
    completedInsts = 0 #initialize completed instances to 0
    icount = len(file.readlines()) #icount = amount of lines in input file
    file.close()
    file = open("test.in","r")
    given = split(",",file.readline()) #first line of input file has number of regs and issue width separated by a comma
    numregs = given[0]
    issuewidth = given[1]
    if (int(numregs) < 32)
	exit
    reg1 = -1
    reg2 = -1
    dest = -1 #initialize register values
    while(completedInsts<icount):
        instruction = Fetch(file,out,cyclecount)
        dest, cyclecount = Decode(instruction, reg1, reg2, dest, cyclecount, out)
        rename
	dispatch(out, cyclecount)
        issue(out, cyclecount)
        WB(out, cyclecount)
        completedInsts += 1
        cyclecount += 1
    return 0

if __name__ == '__main__':
    main()
