
with open("input.txt") as fid:
    data = fid.read()
data = data.strip()

#    add a b 
#    mul a b 
#    div a b - Divide the value of a by the value of b, truncate the result to an integer, then store the result in variable a. (Here, "truncate" means to round the value toward zero.)
#    mod a b 
#    eql a b


def input_iter(value):
    i = 0
    l = len(value)
    while True:
        yield int(value[i])
        i += 1



def inp():
    return next(input_itr)
def add(x,y):
    return x + y
def mul(x,y):
    return x * y

def div(x,y):
    return x // y

def mod(x,y):
    return x % y 

def eql(x,y):
    return (x == y)


cmd_dic = {"inp":0 , "add":add, "mul":mul, "div":div, "mod":mod, "eql":eql }


def parse_args(d):
    if d == "x":
        return 0
    elif d == "y":
        return 1
    elif d == "z":
        return 2
    elif d ==  "w":
        return 3
    else:
        return 4




def validate(value, z):
    x = y =  w = 0
    regs = [0,0,z,0]

    input_itr = input_iter(value)

    for line in data.split("\n")[-18:]:
        cmd, *args = line.split(" ")
        if cmd == "inp":

            regs[3] = next(input_itr )

        else:
            idx0 = parse_args(args[0])
            idx1 = parse_args(args[1])
            if idx1 == 4:
                val = int(args[1])
            else:
                val = regs[idx1]
            regs[idx0] = cmd_dic[cmd](regs[idx0] , val)
    return regs


import functools
words = [0 for _ in range(14)]

            
@functools.lru_cache(maxsize=25000)
def step_calc_min(step,x ,y,z,w):
    for w in range(1, 9): 
        if z > 1e9:
            continue
        if step == 0:
            x = y = z = 0
            
        words[step] = w
        regs = [x, y, z, w]
        for line in data.split("\n")[step * 18: (step +1) * 18]:
            cmd, *args = line.split(" ")
            if cmd == "inp":
                pass
            else:
                idx0 = parse_args(args[0])
                idx1 = parse_args(args[1])
                if idx1 == 4:
                    val = int(args[1])
                else:
                    val = regs[idx1]
                regs[idx0] = cmd_dic[cmd](regs[idx0] , val)
        if step == 13:
            if regs[2] == 0:
                print(f"finished{regs[2]}")
                print("".join(map(str,words)))
                return regs[2]
            else:
                # print(words)
                pass
        else:
            rem =  step_calc_min(step + 1, *regs)
            

@functools.lru_cache(maxsize=25000)
def step_calc_max(step,x ,y,z,w):
    for w in range(9, 0, -1): 
        if z > 1e8:
            continue
        if step == 0:
            x = y = z = 0
            
        words[step] = w
        regs = [x, y, z, w]
        # print(f"{step} {regs}")
        for line in data.split("\n")[step * 18: (step +1) * 18]:
            cmd, *args = line.split(" ")
            if cmd == "inp":
                pass
            else:
                idx0 = parse_args(args[0])
                idx1 = parse_args(args[1])
                if idx1 == 4:
                    val = int(args[1])
                else:
                    val = regs[idx1]
                regs[idx0] = cmd_dic[cmd](regs[idx0] , val)
        if step == 13:
            if regs[2] == 0:
                print(f"finished{regs[2]}")
                print("".join(map(str,words)))
                return regs[2]
            else:
                return False
                pass
        else:
            rem =  step_calc_max(step + 1, *regs)
            





