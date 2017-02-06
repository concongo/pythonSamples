#The new "Avengers" movie has just been released! 
#There are a lot of people at the cinema box office standing in a huge line. 
#Each of them has a single 100, 50 or 25 dollars bill. A "Avengers" ticket costs 25 dollars.
#Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
#Can Vasya sell a ticket to each person and give the change if he initially has no money and 
#sells the tickets strictly in the order people follow in the line?
#Return YES, if Vasya can sell a ticket to each person and give the change. Otherwise return NO.

draw = [100,0,50,0,25,0]
draw_total = 0
cost = 25
clients = [25,100]

for i in range(0,len(clients)):
    if clients[i] == 25: 
         draw[5] = draw[5]+1
         res = 'YES'
    else:
        if clients[i] == 50 and draw[5]>0:
            draw[3] = draw[3] + 1
            draw[5] = draw[5] - 1
            res = 'YES'
        else:
            if clients[i] == 100:
                if draw[3]>= 1 and draw[5] >= 1:
                     draw[1] = draw[1] + 1
                     draw[3] = draw[3] - 1
                     draw[5] = draw[5] - 1
                     res = 'YES'
                else:
                    if draw[5]>= 3:
                        draw[1] = draw[1] + 1
                        draw[5] = draw[5] - 3  
                        res = 'YES'
                    else:
                        res = 'NO'
            else:
                res = 'NO'
                    
                    
                 
                 
            
print (draw)
print (res)
    