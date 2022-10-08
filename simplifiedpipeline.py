

from email.errors import MisplacedEnvelopeHeaderDefect


caches = [-1,-1,-1,-1,-1]
caches_c = {1:0,2:0,3:0,4:0}
instructions = ['LI $1 4','LI $2 5','LI $3 6', 'MUL $1 $2 $4','MUL $3 $4 $4', 'MUL $1 $3 $1', 'MUL $2 $3 $4','ADD $1 $4 $2', 'LW $3 $104', 'ADD $2 $3 $4', 'ADD $4 $4 $1']
instr_len = len(instructions)
instr_list = {}
sources = {}
stall = {}
for idx in range(len(instructions)):
    stall[idx]=0
decodes = {}
executes = {}
mem_access = {}
destination = {}
destination[-1]=""
instr_c = 0
decodes_c = -1
executes_c = -2
mem_access_c = -3
reg_wb_c = -4





while instr_c < instr_len + 4:
    if instr_c < instr_len and stall[instr_c]!=1:
        instr_list[instr_c] = instructions[instr_c].split(" ")
        print(instr_list[instr_c])
        match instr_list[instr_c][0]:
            case "MUL":
                sources[instr_c] = [instr_list[instr_c][1],instr_list[instr_c][2]]
        break