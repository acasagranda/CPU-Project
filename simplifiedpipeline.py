




caches = [-1,-1,-1,-1,-1]
memory = {100:0,101:0,102:0}
instructions = ['LI $1 4','LI $2 5','LI $3 6', 'MUL $1 $2 $4','MUL $3 $4 $4', 'MUL $1 $3 $1', 'MUL $2 $3 $4','ADD $1 $4 $2', 'LW $3 $104', 'ADD $2 $3 $4', 'ADD $4 $4 $1']
instr_len = len(instructions)
#instr_list = {}
#sources = {}
stall = {}
for idx in range(len(instructions)):
    stall[idx]=0
#decodes = {}
#executes = {}
#mem_access = {}
#destination = {}
#destination[-1]=""
instr_c = 0
decodes_c = -1
executes_c = -2
mem_access_c = -3
reg_wb_c = -4

class mul:
    def __init__(self,instr_list,instr_c):
        self.instr_c = instr_c
        self.instr_list = instr_list
        self.sources = [self.instr_list[1],self.instr_list[2]]
        self.destination = self.instr_list[3]
        self.decodes = f"Multiply value in {self.sources[0]} by value in {self.sources[1]} and put result into {self.destination}. "
        self.result = caches[int(self.sources[0][1])]*caches[int(self.sources[1][1])]
        self.execute = f"{caches[int(self.sources[0][1])]} x {caches[int(self.sources[1][1])]} = {self.result}"
        self.mem_access = f"{self.result} -> {self.destination} "

class add:
    def __init__(self,instr_list,instr_c):
        self.instr_c = instr_c
        self.instr_list = instr_list
        self.sources = [self.instr_list[1],self.instr_list[2]]
        self.destination = self.instr_list[3]
        self.decodes = f"Add value in {self.sources[0]} to value in {self.sources[1]} and put result into {self.destination}. "
        self.result = caches[int(self.sources[0][1])]+caches[int(self.sources[1][1])]
        self.execute = f"{caches[int(self.sources[0][1])]} + {caches[int(self.sources[1][1])]} = {self.result}"
        self.mem_access = f"{self.result} -> {self.destination} "

class li:
    def __init__(self,instr_list,instr_c):
        self.instr_c = instr_c
        self.instr_list = instr_list
        self.destination = self.instr_list[1]
        self.result = self.instr_list[2]
        self.decodes = f"Put value {self.result} into {self.destination}"
        self.execute = "no calculation"
        self.mem_access = f"{self.result} -> {self.destination} "

class sw:
    def __init__(self,instr_list,instr_c):
        self.instr_c = instr_c
        self.instr_list = instr_list
        self.destination = self.instr_list[2]
        self.result = self.instr_list[1]
        self.decodes = f"Take value from {self.result} and put into memory {self.destination}"
        self.execute = "no calculation"
        self.mem_access = f"NULL -> {self.result} "

class lw:
    def __init__(self,instr_list,instr_c):
        self.instr_c = instr_c
        self.instr_list = instr_list
        self.destination = self.instr_list[1]
        self.result = self.instr_list[2]
        self.decodes = f"Take value from memory {self.result} and put into {self.destination}"
        self.execute = "no calculation"
        self.mem_access = f"{self.result} -> {self.destination} "

# while instr_c < instr_len + 4:
#     if instr_c < instr_len and stall[instr_c]!=1:
#         instr_list[instr_c] = instructions[instr_c].split(" ")
#         print(instr_list[instr_c])
#         match instr_list[instr_c][0]:
#             case "MUL":
#                 sources[instr_c] = [instr_list[instr_c][1],instr_list[instr_c][2]]
#         break

instructions = ['LW $3 $100']
instr_list = instructions[0].split(" ")
IN1 = lw(instr_list,0)
print(IN1.decodes)
print(IN1.mem_access)

