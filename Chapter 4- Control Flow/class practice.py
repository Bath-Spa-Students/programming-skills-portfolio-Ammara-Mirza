''' books=float(input("enter no of books:"))
people = 8
if books > 700 :
    people=300
else:
    people=8
    print("your people:" +str(people)) '''

Temp = int(input ("enter the temp"))
if Temp<40:
    print("nice weather we're having")
else:
    print("a little cold isn't it?")

# nested desicion structure
salary=int(input("enter your salary per year:"))
work_experience = float (input("enter your work experience:"))

if salary > 80000:
    if work_experience >=5:
        print("you are eligible for taking advance salary")
    else:
        print("sorry your work experience is less than 5 years") 
    
else :
 print("your salary is less than 80000")