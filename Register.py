from RegisterDetails import *
def sf(a):
    a= str(a)
    b= a.strip("("+")")
    return b
'''Courses = ['python','arduino','game development','circuits','java']
Students = ['amishi bisht','nayonika de','shaili dutta','zoha dhanani','siddharth dhawen','sravya reddy','anirudh misra','sara crewe']
Days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
Trainer = ["ajay gupta","bhavani sambaraju","siobhan roy","saher sharma","janaki mamtura"]'''
def reg():
    n= input("Please enter your full name ")
    n=n.lower()
    x=input("Hello "+n+"! Would you like to Enroll as a student or apply for the position of a trainer? ")
    x= x.lower()
    if x =="trainer":
        for i in Trainer:
            if i == n:
                print("You are already a Trainer, Thank you.")
                c2= input("Would you like to to apply to teach a new course? If so please state the name of the course ")
                c2= c2.lower()
                c2= c2.strip("."+" ")
                if c2=="no" or c2=="nope" or c2 =="no thanks" or c2=="nah" or c2=="no thank you":
                    print("Okay, Good Bye")
                else:
                    c=input("Ok, may we know what course you'd like to teach- Python, Arduino, Game development, Circuits or Java? ")
                    c=c.lower()

                    try:
                        for i in Courses:
                            if i==c:
                                print("Welcome! You have applied for the position of a trainer in the",c,"course. We will contact you with your class details shortly ")
                                a=ClassSchedule[c]
                                print("You will be training along with",(str(tuple(a.get("Trainers")))).strip("("+")"))
                                print("You will be training",(str(tuple(a.get("Students")))).strip("("+")"))
                                print("You will be training on",(str(tuple(a.get("Days")))).strip("("+")"))
                                #  (a.get("Trainers")).append(n)
                                qwe=input("Please enter your email or mobile number so we can send you the further details about",c,"course. Thank you for your time and we hope to see you again soon")
                    except NameError:
                            print("We are sorry but we do not currently have a course on",c)
                            qwe=input("Please enter your phone number or email so we can contact you for future update on the course on",c,"Thank you for your time and we hope to see you again soon")


            else:
                c=input("Ok, may we know what course you'd like to teach- Python, Arduino, Game development, Circuits or Java? ")
                c=c.lower()

                try:
                    for i in Courses:
                        if i==c:
                            print("Welcome! You have applied for the position of a trainer in the",c,"course. We will contact you with your class details shortly ")
                            a=ClassSchedule[c]
                            print("You will be training along with",(str(tuple(a.get("Trainers")))).strip("("+")"))
                            print("You will be training",(str(tuple(a.get("Students")))).strip("("+")"))
                            print("You will be training on",(str(tuple(a.get("Days")))).strip("("+")"))
                            #  (a.get("Trainers")).append(n)
                            qwe=input("Please enter your email or mobile number so we can send you the further details about "+c+" course. Thank you for your time and we hope to see you again soon")
                except NameError:
                        print("We are sorry but we do not currently have a course on",c)
                        qwe=input("Please enter your phone number or email so we can contact you for future update on the course on",c,"Thank you for your time and we hope to see you again soon")
    if x=="student":
        for i in Students:
            if n in Students:
                print("You are already enrolled, Thank you.")
                c2= input("Would you like to learn a new course? If so please state the name of the course ")
                c2= c2.lower()
                c2= c2.strip("."+" ")
                if c2=="no" or c2=="nope" or c2 =="no thanks" or c2=="nah" or c2=="no thank you":
                    print("Okay, Good Bye")
                else:
                    c=input("Ok, may we know what course you would like to enroll in- Python, Arduino, Game development, Circuits or Java? ")
                    c=c.lower()
                try:
                        for i in Courses:
                            if i==c:
                                print("Welcome! You have been enrolled in",c,"course. We will contact you with class details shortly ")
                                a=ClassSchedule[c]
                                print("You will be trained by",(str(tuple(a.get("Trainers")))).strip("("+")"))
                                print("You will be training with",(str(tuple(a.get("Students")))).strip("("+")"))
                                print("You will be training on",(str(tuple(a.get("Days")))).strip("("+")"))
                                (a.get("Students")).append(n)
                                qwe=input("Please enter your parent's email or mobile number so we can send you the further details about",c,"course. Thank you for your time and we hope to see you again soon")
                        
                except NameError:
                            print("We are sorry but we do not currently have a course on",c)
                            qwe=input("Please enter your phone number or email so we can contact your parents for future update on the course on "+c+". Thank you for your time and we hope to see you again soon.")
                
            else:
                c=input("Ok, may we know what course you would like to enroll in- Python, Arduino, Game development, Circuits or Java? ")
                c=c.lower()
                try:
                        for i in Courses:
                            if i==c:
                                print("Welcome! You have been enrolled in",c,"course. We will contact you with class details shortly ")
                                print("You will be trained by",(str(tuple(a.get("Trainers")))).strip("("+")"))
                                print("You will be training with",(str(tuple(a.get("Students")))).strip("("+")"))
                                print("You will be training on",(str(tuple(a.get("Days")))).strip("("+")"))
                        (a.get("Students")).append(n)
                        qwe=input("Please enter your parent's email or mobile number so we can send you the further details about",c,"course. Thank you for your time and we hope to see you again soon")
                        
                except NameError:
                            print("We are sorry but we do not currently have a course on",c)
                            qwe=input("Please enter your phone number or email so we can contact your parents for future update on the course on "+c+". Thank you for your time and we hope to see you again soon.")
#reg()
def cs():
    n= input("Course name: ")
    n= n.lower()
    a=tuple(ClassSchedule[n].get("Students"))
    a= str(a)
    a= a.strip("("+")")
    print("Students in",n,"are",a)
#cs()
def sd():
    dow= Days.copy()
    sn= input("Student Name: ")
    space= sn.index(" ")
    sn= sn[0].upper()+sn[1:space].lower()
    for i in ClassSchedule:
        for x in i:
            if x=="Students":
                print("A")
                
    dow= str(dow)
    dow=dow.strip("["+"]")
    print(sn,"does not attend classes on",dow)
sd()
def td():
    dow= Days.copy()
    sn= input("Trainer Name: ")
    space= sn.index(" ")
    sn= sn[0].upper()+sn[1:space].lower()
    for i in ClassSchedule:
        for x in i:
            if x=="Trainers":
                        for days in "Days":
                            d=dow.index(days)
                            dow=dow.remove(d)
    dow= str(dow)
    dow=dow.strip("["+"]")
    print(sn,"does not teach classes on",dow)

'''def spec():
    dow= Days.copy()
    sn= input("Day: ")
    sn= sn[0].upper()+sn[1:].lower()
    for i in ClassSchedule:
        for x in i:
            if x=="Trainers":
                    for days in "Days":
                            d=dow.index(days)
                            dow=dow.remove(d)
    dow= str(dow)
    dow=dow.strip("["+"]")
    print(sn,"does not teach classes on",dow)'''
"cs()"
'''Homework(Use this file to import):
1. Use the Register module to practise the concepts taught so far
2. Write functions which can help you find if a Student is enrolled or a trainer is registered with Little Inventors.
3. Write a function to display the names of the students enrolled for a course. Input to the function is course name and the function should return the names of the enrolled students.
4. Write a function that returns the days a kid/student has no classes
5. Write a function that returns the days a trainer has no classes
6. Write a function to get the names of trainers and students who have classes on a speific day.'''
 