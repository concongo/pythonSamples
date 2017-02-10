ints = [5, 9, 13, -3]
s = 10
found = []

def find_a_pair(r_list,i):
    x1 = r_list[0]
    x2 = s - x1
    #print i
    #print r_list
    #print len(r_list)
    try:
        pos_x2 = r_list[1:].index(x2)
        found.append({"pos_1": i, "val_1": x1, "pos_2": pos_x2+i, "val_2": x2 })
    except:
        pass
    #print r_list[1:]
    if len(r_list)>1:
        find_a_pair(r_list[1:],i+1)

find_a_pair(ints,0)

min_index = len(ints) #here we assume tha the min_index is the len in order to find the minimum index of the the pos_2 which will be returned


for pair in found:
       if pair["pos_2"] < min_index: 
           min_index = pair["pos_2"]
           ans = [pair["val_1"],pair["val_2"]]
if len(found) == 0: ans = None

print ans   