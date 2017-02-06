#Given a list lst and a number N, create a new list that contains each number of lst at
#most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], 
#you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3
#times, and then take 3, which leads to [1,2,3,1,2,3].

def delete_nth(order,max_e):
    i=0
    rep=0
    res=[]

    for i in range(0,len(order)):
        rep=order.count(order[i])
        if rep > max_e and  res.count(order[i])< max_e: res.append(order[i])
        if rep <= max_e and res.count(order[i])< max_e: res.append(order[i])
    return res

print delete_nth([1,1,1,1,3,3,1,1],3)
