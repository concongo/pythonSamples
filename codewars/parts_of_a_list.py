#title              :queue_time.py
#description        :Write a function partlist that gives all the
#                    ways to divide a list (an array) of at least two elements 
#                    into two non-empty parts.

#author             : Jose Fernando Gonzalez
#date               : 20170220
#version            : 0.1
#usage              : python parts_of_a_list.py
#notes              : Kata from codewars
#python_version     : 3.4.3

def partlist(arr):
    s = ' '
    res = ['']*(len(arr)-1)
    for i in range(0,len(arr)-1):
        if s.join(arr[0:i]) == '': 
            res[i]=(arr[i], s.join(arr[i+1:len(arr)]))
        else:
            res[i] = (s.join(arr[0:i+1]), s.join(arr[i+1:len(arr)]))
    return res
    
sample = ["I", "wish", "I", "hadn't", "come"]

print partlist(sample)
