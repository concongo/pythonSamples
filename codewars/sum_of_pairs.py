

ints = [1, 4, 8, 7, 3, 15]
s = 8
found = []

for i in range(len(ints)):
    x1 = ints[i]
    x2 = s - x1
    substr= ints[i+1:len(ints)]
    try:
        pos_2 = substr.index(x2)
        found.append({"pos_1": i, "val_1": x1, "pos_2": pos_2+i+1, "val_2": x2 })
    except:
        pos_2 = -1
        pass

min_index = len(ints) #here we assume tha the min_index is the len in order to find the minimum index of the the pos_2 which will be returned


for pair in found:
       if pair["pos_2"] < min_index: 
           min_index = pair["pos_2"]
           ans = [pair["val_1"],pair["val_2"]]
if len(found) == 0: ans = None

print ans   

