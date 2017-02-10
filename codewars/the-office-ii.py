#title              :the-office-ii.py
#description        :Every now and then people in the office moves teams or departments. 
#                    Depending what people are doing with their time they can become more or less boring. 
#                    Time to assess the current team.
#                    You will be provided with an object(staff) containing the staff names as keys, 
#                    and the department they work in as values.
#                    Each department has a different boredom assessment score, as follows:
#
#                       accounts = 1
#                       finance = 2 
#                       canteen = 10 
#                       regulation = 3 
#                       trading = 6 
#                       change = 6
#                       IS = 8
#                       retail = 5
#                       cleaning = 4
#                       pissing about = 25
#
#                    Depending on the cumulative score of the team, return the appropriate sentiment:
#
#                       <=80: 'kill me now'
#                       < 100 & > 80: 'i can handle this'
#                       100 or over: 'party time!!'
#author             : Jose Fernando Gonzalez
#date               : 20170210
#version            : 0.1
#usage              : python the-office-ii.py
#notes              : Kata from codewars
#python_version     : 3.4.3

dept = {"tim": "change", "jim": "accounts","randy": "canteen", "sandy": "change", "andy": "change", "katie": "IS","laura": "change", "saajid": "IS", "alex": "trading", "john": "accounts","mr": "finance" }



def boredom(staff):
    
    
    class Staff:
        
        
        dept_points = {"accounts": 1, "finance": 2,  "canteen": 10, "regulation": 3, "trading": 6, "change": 6, "IS": 8,"retail": 5, "cleanning": 4, "pissing about": 25}
        
        def __init__(self, staff):
            self.staff = staff
            
        
        def assestment(self):
            points = 0
            for employee,department in self.staff.items(): #using to variable assume key, value
               points += Staff.dept_points[department]                        
            if points <= 80:
                return "kill me now"
            elif points >= 100:
                return "party time!!"
            elif points < 100 and points > 80:
                return "i can handle this"
            
            
    vdshop = Staff(staff)
    return vdshop.assestment()

boredom(dept)

    