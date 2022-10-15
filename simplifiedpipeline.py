
instructions = ['LI $1 4','LI $2 5','LI $3 6', 'MUL $1 $2 $4','SW $4 $100','MUL $3 $4 $4', 'MUL $1 $3 $1', 'MUL $2 $3 $2','ADD $1 $2 $1', 'LW $3 $100', 'ADD $1 $3 $2', 'ADD $2 $2 $3']
instr_len = len(instructions)
#simulate the cache with a dictionary
caches = {}
#split up the instructions 
instr_var = {}
#keep track of when to stall - initialize with 0s
stall = {}
for idx in range(len(instructions)+5):
    stall[idx]=0
stall[-1] = 0
stall[-2] = 0
#keeps track of which instruction is current at each stage
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
        self.executes = ''
        self.result = 0
        self.mem_access = ''
        self.decodes = f"Multiply value in {self.sources[0]} by value in {self.sources[1]} and put result into {self.destination}. "
        
    def calc_executes(self):
        self.result = int(caches[self.sources[0]]*caches[self.sources[1]])
        self.executes = f"{caches[self.sources[0]]} x {caches[self.sources[1]]} = {self.result}"
        self.mem_access = f"{self.result} -> {self.destination} "
        

class add:
    def __init__(self,instr_list,instr_c):
        self.instr_c = instr_c
        self.instr_list = instr_list
        self.sources = [self.instr_list[1],self.instr_list[2]]
        self.destination = self.instr_list[3]
        self.executes = ''
        self.result = 0
        self.mem_access = ''
        self.decodes = f"Add value in {self.sources[0]} to value in {self.sources[1]} and put result into {self.destination}. "
        
    def calc_executes(self):
        self.result = int(caches[self.sources[0]]+caches[self.sources[1]])
        self.executes = f"{caches[self.sources[0]]} + {caches[self.sources[1]]} = {self.result}"
        self.mem_access = f"{self.result} -> {self.destination} "

class li:
    def __init__(self,instr_list,instr_c):
        self.instr_c = instr_c
        self.instr_list = instr_list
        self.sources = []
        self.destination = self.instr_list[1]
        self.result = int(self.instr_list[2])
        self.decodes = f"Put value {self.result} into {self.destination}"
        self.executes = "no calculation"
        self.mem_access = f"{self.result} -> {self.destination} "
    
    def calc_executes(self):
        return

class sw:
    def __init__(self,instr_list,instr_c):
        self.instr_c = instr_c
        self.instr_list = instr_list
        self.sources = [self.instr_list[1]]
        self.destination = self.instr_list[2]
        self.result = 0
        self.decodes = f"Take value from {self.instr_list[1]} and put into memory {self.destination}"
        self.executes = "no calculation"
        self.mem_access = "no change in cache"

    def calc_executes(self):
        self.result = int(caches[self.instr_list[1]])

class lw:
    def __init__(self,instr_list,instr_c):
        self.instr_c = instr_c
        self.instr_list = instr_list
        self.sources = []
        self.destination = self.instr_list[1]
        self.result = 0
        self.decodes = f"Take value from memory {self.instr_list[2]} and put into {self.destination}"
        self.executes = "no calculation"
        self.mem_access = " "

    def calc_executes(self):
        self.result = int(caches[self.instr_list[2]])
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
for indx in range(1,instr_len):
    if instr_var[indx-1].destination in instr_var[indx].sources:
        stall[indx]= 1
      
    
      
stall1 = False
stall2 = False

print("This program simulates a simplified version of pipelining in a CPU taking instructions in assembly language.")
print("To keep it simple it has no branching and does not do the write-back.")
print(' ')
print("The instructions input the length, width and height of a box then calculates the box's Volume and Surface Area.")
print(" ")
print("-------------------------------------------")


while mem_access_c < instr_len:
    input("Press ENTER to display the next cycle:")
    if instr_c < instr_len and not stall1:
        print(f"fetch instruction {instr_c}: {instructions[instr_c]}")
        instr_c += 1
    elif instr_c >= instr_len:
        print("fetch instruction: no more instructions to fetch")
    else:
        print("fetch instruction: stalling ...")

    if decodes_c > -1 and decodes_c < instr_len and not stall1:
        print(f"decode instruction {decodes_c}: {instr_var[decodes_c].decodes}")
        decodes_c +=1
    elif decodes_c >= instr_len:
        print("decode instruction: no more instructions to decode")
    elif decodes_c < 0:
        print("decode instruction: no instructions to decode yet")
        decodes_c +=1
    else:
        print("decode instruction: stalling ...")
    

    if executes_c > -1 and executes_c < instr_len and not stall1: 
        instr_var[executes_c].calc_executes()
        print(f"execute instruction {executes_c}: {instr_var[executes_c].executes}")
        executes_c +=1
    elif executes_c >= instr_len:
        print("execute instruction: no more instructions to execute")
    elif executes_c < 0:
        print("execute instruction: no instructions to execute yet")
        executes_c +=1
    else:
        print("execute instruction: stalling ...")
        #instr_var[executes_c].calc_executes()
    
    if mem_access_c > -1 and mem_access_c < instr_len and not stall2:
        print(f"memory access instruction {mem_access_c}: {instr_var[mem_access_c].mem_access}")
        caches[instr_var[mem_access_c].destination] = int(instr_var[mem_access_c].result)
        mem_access_c +=1
    elif mem_access_c >= instr_len:
        print("memory access instruction: no more instructions")
    elif mem_access_c < 0:
        print("memory access instruction: no memory access yet")
        mem_access_c +=1
    else:
        print("memory access instruction: no change in cache")

    if stall[instr_c-2]==1:
        stall1 = not stall1
    if stall[mem_access_c]==1:
        stall2 = not stall2


    print("-------------------------------------------")


