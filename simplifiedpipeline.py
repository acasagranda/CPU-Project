




caches = [-1,-1,-1,-1,-1]
memory = {100:0,101:0,102:0}
instructions = ['LI $1 4','LI $2 5','LI $3 6', 'MUL $1 $2 $4','MUL $3 $4 $4', 'MUL $1 $3 $1', 'MUL $2 $3 $4','ADD $1 $4 $2', 'LW $3 $104', 'ADD $2 $3 $4', 'ADD $4 $4 $1']
instr_len = len(instructions)
instr_var = {}
stall = {}
for idx in range(len(instructions)):
    stall[idx]=0
stall[-1] = 0
instr_c = 0
decodes_c = -1
executes_c = -2
mem_access_c = -3


class mul:
    def __init__(self,instr_list,instr_c):
        self.instr_c = instr_c
        self.instr_list = instr_list
        self.sources = [self.instr_list[1],self.instr_list[2]]
        self.destination = self.instr_list[3]
        self.decodes = f"Multiply value in {self.sources[0]} by value in {self.sources[1]} and put result into {self.destination}. "
        self.result = caches[int(self.sources[0][1])]*caches[int(self.sources[1][1])]
        self.executes = f"{caches[int(self.sources[0][1])]} x {caches[int(self.sources[1][1])]} = {self.result}"
        self.mem_access = f"{self.result} -> {self.destination} "

class add:
    def __init__(self,instr_list,instr_c):
        self.instr_c = instr_c
        self.instr_list = instr_list
        self.sources = [self.instr_list[1],self.instr_list[2]]
        self.destination = self.instr_list[3]
        self.decodes = f"Add value in {self.sources[0]} to value in {self.sources[1]} and put result into {self.destination}. "
        self.result = caches[int(self.sources[0][1])]+caches[int(self.sources[1][1])]
        self.executes = f"{caches[int(self.sources[0][1])]} + {caches[int(self.sources[1][1])]} = {self.result}"
        self.mem_access = f"{self.result} -> {self.destination} "

class li:
    def __init__(self,instr_list,instr_c):
        self.instr_c = instr_c
        self.instr_list = instr_list
        self.sources = []
        self.destination = self.instr_list[1]
        self.result = self.instr_list[2]
        self.decodes = f"Put value {self.result} into {self.destination}"
        self.executes = "no calculation"
        self.mem_access = f"{self.result} -> {self.destination} "

class sw:
    def __init__(self,instr_list,instr_c):
        self.instr_c = instr_c
        self.instr_list = instr_list
        self.sources = []
        self.destination = self.instr_list[2]
        self.result = self.instr_list[1]
        self.decodes = f"Take value from {self.result} and put into memory {self.destination}"
        self.executes = "no calculation"
        self.mem_access = f"NULL -> {self.result} "

class lw:
    def __init__(self,instr_list,instr_c):
        self.instr_c = instr_c
        self.instr_list = instr_list
        self.sources = []
        self.destination = self.instr_list[1]
        self.result = self.instr_list[2]
        self.decodes = f"Take value from memory {self.result} and put into {self.destination}"
        self.executes = "no calculation"
        self.mem_access = f"{self.result} -> {self.destination} "

for indx in range(instr_len):
    instr_list = instructions[indx].split(" ")
    match instr_list[0]:
        case "MUL":
            instr_var[indx]= mul(instr_list,indx)
        case "ADD":
            instr_var[indx]= add(instr_list,indx)  
        case "LI":
            instr_var[indx]= li(instr_list,indx)
        case "SW":
            instr_var[indx]= sw(instr_list,indx)  
        case "LW":
            instr_var[indx]= lw(instr_list,indx)
        case _:
            print(f"Invalid instruction: {instructions[indx]} ")
            instr_c +=10
for indx in range(1,instr_len-1):
    if instr_var[indx-1].destination in instr_var[indx].sources:
        stall[idx]= 1

#print intro here


print("-------------------------------------------")


while instr_c < instr_len + 4:
    input("Press ENTER to display the next cycle:")
    if instr_c < instr_len and stall[instr_c]!=1:
        print(f"fetch instruction {instr_c}: {instructions[instr_c]}")
    elif instr_c >= instr_len:
        print("fetch instruction: no more instructions to fetch")
    else:
        print("fetch instruction: stalling ...")
    if decodes_c > -1 and instr_c < instr_len + 1 and stall[instr_c]!=1:
        print(f"decode instruction {decodes_c}: {instr_var[decodes_c].decodes}")
        decodes_c +=1
    elif instr_c >= instr_len + 1:
        print("decode instruction: no more instructions to decode")
    elif decodes_c < 0:
        print("decode instruction: no instructions to decode yet")
    else:
        print("decode instruction: stalling ...")
    if executes_c > -1 and instr_c < instr_len + 2 and stall[instr_c]!=1:
        print(f"execute instruction {executes_c}: {instr_var[executes_c].executes}")
        executes_c +=1
    elif instr_c >= instr_len + 2:
        print("execute instruction: no more instructions to execute")
    elif executes_c < 0:
        print("execute instruction: no instructions to execute yet")
    else:
        print("execute instruction: stalling ...")

    if mem_access_c > -1 and stall[instr_c]!=1:
        print(f"memory access instruction {mem_access_c}: {instr_var[mem_access_c].mem_access}")
        mem_access_c +=1
    else:
        print("memory access instruction: no memory to access yet")
    if stall[instr_c]==1:
        stall[instr_c]==0
    else:
        instr_c += 1

    print("-------------------------------------------")