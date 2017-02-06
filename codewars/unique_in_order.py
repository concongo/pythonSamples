#Implement the function unique_in_order which takes as argument a sequence and 
#returns a list of items without any elements with the same value next to each 
#other and preserving the original order of elements.

#For example:

#unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
#unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
#unique_in_order([1,2,2,3,3])       == [1,2,3]

#FUNCTIONS USED: len(), range(), str(),int(), list()

_sequence = 'AAAABBBCCDAABBB'
_lastchar = ""
_seqtemp = ""
_seqinttemp = []
for i in range(0,len(_sequence)):
    
    if str(_sequence[i]) != str(_lastchar):
        _lastchar=str(_sequence[i])
        if _lastchar not in ['1','2','3','4','5','6','7','8','9','0']:
            _seqtemp = _seqtemp + str(_sequence[i])
        else:
            _seqinttemp.append(int(_lastchar))
        

_seqtemp = list(_seqtemp)
#if _seqtemp len >0 use it, if not the other one        
       
print("ans ", _seqtemp,_seqinttemp)
