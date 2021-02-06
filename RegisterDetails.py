# This file contains details of students enrolled for our course
Courses = ['python','arduino','game development','circuits','java']
Students = ['amishi bisht','nayonika de','shaili dutta','zoha dhanani','siddharth dhawen','sravya reddy','anirudh misra','sara crewe']
Days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
Trainer = ['ajay gupta','bhavani sambaraju','siobhan roy','saher sharma','Janaki mamtura']

'''def IsEnrolled(name):
    for i in Students:
        if(name == i):
            print("You are already enrolled!")
            break
    else:
        print("Hello there!, Would you like to check out our courses")
    return
    
     The following dictionary named "ClassSchedule" gives information about Students and Trainers 
     and the days during which they're occupied with a certain course'''

ClassSchedule = {
    'python':
    {
        'Students':['Amishi','Nayonika','Shaili','Zoha'],'Trainers':['Bhavani'],'Days':['Saturday','Sunday']
    },
    'arduino':
    {
        'Students':['Sara','Amishi','Shaili','Sravya'],'Trainers':['Siobhan','Ajay'],'Days':['Monday','Sunday']
    },
    'game development':
    {
        'Students':['Sara','Amishi','Zoha','Nayonika'],'Trainers':['Saher','Janaki'],'Days':['Monday','Wednesday']
    },
    'circuits':
    {
        'Students':['Siddharth','Sravya','Zoha','Anirudh'],'Trainers':['Janaki','Ajay'],'Days':['Friday','Wednesday']
    },
    'java':
    {
        'Students':['Siddharth','Sravya','Anirudh'],'Trainers':['Bhavani'],'Days':['Tuesday','Thursday']
    }
}

