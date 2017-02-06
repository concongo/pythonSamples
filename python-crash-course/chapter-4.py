number = 0
#print the numbers from 1 to 20
for number in range(1,21):
    print(number)
    
#make a list of numbers from to one million
#4-6
listofnumbers=[]
for number in range(1,1000001):
    listofnumbers.append(number)
    
#for i in range(1,1000):
#    print (listofnumbers[i])

#4-5
print(min(listofnumbers))
print(max(listofnumbers))
print(sum(listofnumbers))
  
#4-6
listofoddnumbers=list(range(1,20,2))
for i in listofoddnumbers:
    print (i)

#4-7
listofthrees=list(range(3,33,3))
for i in listofthrees:
    print(i)
    
#4-8
listofcubes=list(range(1,11,1))
for i in range(1,10):
    listofcubes[i]=listofcubes[i]**3

for cube in listofcubes:
    print(cube)
    
#4-9
cubes = [value**3 for value in range(1,11)]
print (cubes)