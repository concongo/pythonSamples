ints = [1, 3, 8, 5, 3, 7]
s = 8
found = []
ints = tuple(ints)

def memoize(f):
    memo = {}
    
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def find_a_pair(x):
    
    i=x

    x1 = ints[x]
    x2 = s - x1
    #print i
    #print r_list
    #print len(r_list)
    try:
        pos_x2 = tuple(ints[i+1:]).index(x2)
        found.append({"pos_1": i, "val_1": x1, "pos_2": pos_x2+i, "val_2": x2 })
    except:
        pass
    #print r_list[1:]
    if i+1<len(ints):
        find_a_pair(i+1)

find_a_pair(0)

min_index = len(ints) #here we assume tha the min_index is the len in order to find the minimum index of the the pos_2 which will be returned


for pair in found:
       if pair["pos_2"] < min_index: 
           min_index = pair["pos_2"]
           ans = [pair["val_1"],pair["val_2"]]
if len(found) == 0: ans = None



print ans   