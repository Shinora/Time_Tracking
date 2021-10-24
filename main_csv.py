from utils import Activity, Question, Machine_State
import datetime
import time
import json
import os
import csv
from gpiozero import RotaryEncoder, Button


questions = [
Question(question="Fast ?", code = "FAST", anwsers = [["yes",1], ["no", -1]]),
Question(question = "Stretching ?", code = "STRETCH", anwsers = [["yes",1], ["no", -1]]),
Question(question = "Alcohol ?", code = "ALCO", anwsers = [["no",0],["some",-1], ["lots", -3]]),
Question(question = "Sexual activity ?", code = "SEX", anwsers = [["yes",-2],["no", 1]]),
Question(question = "Sugar ?", code = "SUGAR", anwsers = [["no",2],["some",-1], ["lots", -3]]),
Question(question = "Meat ?", code = "MEAT", anwsers = [["yes",-1], ["no", 1]])
]

activities = [Activity(name="Sleep", category="LIFE", code="SLEEP", duration=1, description="sleeping", value=0), 
Activity(name="Eating", category="LIFE", code="EAT", duration=0.25, description="eating time", value=0),
Activity(name = "Cooking", category="LIFE", code="COOK", duration=0.25, description="cooking anything", value=0.5),

Activity(name="Reeding", category="CULTURE", code="REE", duration=0.25, description="reeding books", value=1),

Activity(name="School", category="STUDIES", code="SCHOOL", duration=1.42, description="class time", value=0),
Activity(name="School Work", category="STUDIES",code="SCHOOL_WO", duration = 0.5, description="homeworks", value=2 ),
Activity(name="School Revisions", category="STUDIES", code="SCHOOL_RE",duration = 0.5, description="working for upcoming exams", value=2),

Activity(name="Personal projects informatics", category="PROJECTS", code="PRO_INFO",duration= 0.5, description="working on an informatics project", value=1),
Activity(name="Personal projects electronics", category="PROJECTS", code="PRO_ELEC", duration=0.5, description="working on an electronics project", value=1),
Activity(name="Personal projects embedded", category="PROJECTS", code="PRO_EMBE", duration=0.5, description="working on an embedded project", value=1),
Activity(name="Repair & Re-use", category="PROJECTS", code="PRO_REP", duration=0.5, description="repairing an old or non working thing", value=1),
Activity(name="Personal projects others", category="PROJECTS", code="PRO_OTH", duration=0.5, description="working on a project", value=1),

Activity(name="Walking", category="SPO_LOW", code="WALK", duration=0.25, description="walking between two locations", value=0.1),
Activity(name="Yoga" , category="SPO_LOW", code="YOGA", duration =0.25, description="yoga session", value=1),
Activity(name="Stretching" , category="SPO_LOW", code="STRETCH", duration=0.25, description="stretching", value=1),
Activity(name="Volley" , category="SPO_MID", code="VOLLEY", duration=0.5, description="playing volley ball", value=0),
Activity(name="Home training" , category="SPO_HIG", code="SPO_HOM", duration=0.25, description="high intensity cardio and workout at home", value=1),

Activity(name="Friends Hangout" , category="SOCIAL", code="FRIEND", duration=0.5, description="hanging with friends", value=0),
Activity(name="Party" , category="SOCIAL", code="PARTY", duration=1, description="party with friends", value=-2)]

def get_date():
    return datetime.datetime.date(datetime.datetime.now())

def get_time():
    return datetime.datetime.now().strftime('%H:%M')

def write_action(date, start_time, end_time, activity):
    with open('data/time/'+str(date)+'.csv', mode='a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([start_time, end_time, activity.code])
    return None

def read_csv(date):
    with open('data/time/'+str(date)+'.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row)

def findInstanceQuestions(code, questions, activities):
    for instance in questions:
        if instance.code == code:
            return instance
    for instance in activities:
        if instance.code == code:
            return instance

    return False

def findInstanceQuestions(code, questions):
    for instance in questions:
        if instance.code == code:
            return instance

    return False

def findInstanceActivities(code,activities):
    for instance in activities:
        if instance.code == code:
            return instance

    return False

def QuestionAnwser(question):
    print(question.question)  # LCD
    choices = []
    valid = 0
    for anwser in question.anwsers:
        print(anwser[0])  # LCD
        choices.append(anwser[0])
    while valid != 1:
        selection = str(input(" Entrez votre choix : ")).lower()   # Rotary encoder
        print(selection)
        if selection in choices:
            valid = 1
    
    return anwser

def dailyQuestions(questions):
    anwsers = []
    for question in questions:
        anwsers.append(QuestionAnwser(question))
    return anwsers
    
def saveQuestionsAnwsers(date, questions, anwsers): 
    with open('data/questions/'+str(date)+'.csv', mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['question', 'anwser', 'points'])
        for i in range(len(questions)):
            writer.writerow([questions[i].question, anwsers[i][0], anwsers[i][1]])
    return None

def SelectionMenuActivities(activities):
    rotor = RotaryEncoder(a=17, b=18, max_steps=len(activities))
    select = 0
    while select != 1:
        t0 = time.time()
        rotor.wait_for_rotate()
        selection = activities[rotor.values]
        print(activities[rotor.value].code)

        if time.time()- t0 > 10:
            return findInstanceActivities(selection, activities)


def wait_for_action():  # TODO
    a = input()
    
'''write_action(datetime.datetime.date(datetime.datetime.today()), "10:15", "11:25", "SLEEP")
write_action(datetime.datetime.date(datetime.datetime.today()), "11:25", "12:25", "WORK")'''

'''read_csv(datetime.datetime.date(datetime.datetime.today()))'''


if __name__ == "__main__":
    while True:
        date = get_date()
        
        try:
            open('data/questions/'+str(date)+'.csv', mode='r')
        except:
            saveQuestionsAnwsers(date ,questions, dailyQuestions(questions))

        try:
            open('data/time/'+str(date)+'.csv', mode='r')
        except:
            with open('data/time/'+str(date)+'.csv', mode='w') as csv_file:
                writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['start_time', 'end_time', 'activity'])

        current_activity = SelectionMenuActivities(activities)
        start_time = get_time()
        current_activity, last_activity = SelectionMenuActivities(activities), current_activity
        write_action(date, start_time, get_time(), last_activity)
