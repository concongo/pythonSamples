import re

textFile = open('regex_sum_353150.txt')
runningtotal = 0

for line in textFile:
    line = line.rstrip()
    number_found = list(map(int,re.findall('[0-9]+',line)))
    runningtotal = sum(number_found) + runningtotal
    
print("Total: ", runningtotal)
    
    