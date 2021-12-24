from utils import Activity, Question, Machine_State, Screen
import datetime
import time
import os
import csv
import requests
from gpiozero import RotaryEncoder, Button

questions = [
Question(question="Fast ?", code = "FAST", anwsers = [["yes",1], ["no", -1]]),
Question(question = "Stretching ?", code = "STRETCH", anwsers = [["yes",1], ["no", -1]]),
Question(question = "Alcohol ?", code = "ALCO", anwsers = [["no",0],["some",-1], ["lots", -3]]),
Question(question = "Sexual activity ?", code = "SEX", anwsers = [["yes",-2],["no", 1]]),
Question(question = "Sugar ?", code = "SUGAR", anwsers = [["no",2],["some",-1], ["lots", -3]]),
Question(question = "Meat ?", code = "MEAT", anwsers = [["yes",-1], ["no", 1]]),
Question(question = "Sport ?", code = "SPORT", anwsers = [["yes",1], ["no", -1]]),

]

activities = [Activity(name="Sleep", category="LIFE", code="SLEEP", duration=1, description="sleeping", value=0), 
Activity(name="Eating", category="LIFE", code="EAT", duration=0.25, description="eating time", value=0),
Activity(name = "Cooking", category="LIFE", code="COOK", duration=0.25, description="cooking anything", value=0.5),
Activity(name = "Cleaning", category="LIFE", code="CLEAN", duration=0.25, description="cleaning myself and the flat", value=0),

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
Activity(name="Jujitsu" , category="SPO_HIG", code="JJB", duration=1, description="jujitsu classes", value=1),

Activity(name="Friends Hangout" , category="SOCIAL", code="FRIEND", duration=0.5, description="hanging with friends", value=0),
Activity(name="Party" , category="SOCIAL", code="PARTY", duration=1, description="party with friends", value=0),

Activity(name="Phone scrolling" , category="WASTE", code="PHONE", duration=1, description="scrolling some nonsense on my phone", value=-2),
Activity(name="Doing Nothing" , category="WASTE", code="NOTHING", duration=1, description="beoing so lost and unproductive that i dont do anything", value=-1),
Activity(name="Video Games and related" , category="WASTE", code="GAMES", duration=1, description="playing with no educational or social purpose", value=-1)]




#--------------------------- HARDWARE SETUP -------------------------------------------


screen = Screen()
rotor = RotaryEncoder(a=21, b=20, max_steps=len(activities)-1, wrap=True)
button = Button(15)

#--------------------------------------------------------------------------------------

def get_date():
    return datetime.datetime.date(datetime.datetime.now())

def get_time():
    return datetime.datetime.now().strftime('%H:%M')

def write_action(date, start_time, end_time, activity):
    with open('data/time/'+str(date)+'.csv', mode='a+') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([start_time, end_time, activity.code])
    return None

def read_csv(date):
    with open('data/time/'+str(date)+'.csv', mode='r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row)

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

def category_list(activities):
    categories = []
    for activity in activities:
        if activity.category not in categories:
            categories.append(activity.category)
    return categories

def filter_categories(activities, filter):
    filtered = []
    for activity in activities:
        if activity.category == filter:
            filtered.append(activity)
    return filtered

def questionAnwser(question, rotor, button, screen):
    rotor.close()
    screen.clear()
    screen.write_topline(question.question)
    choices = []
    valid = 0
    for anwser in question.anwsers:
        choices.append(anwser[0])

    index = 0
    selection = choices[index]
    rotor = RotaryEncoder(a=21, b=20, max_steps=len(choices)-1, wrap=False)

    while button.value != True:
        index = int(rotor.steps)
        selection = choices[index]
        screen.write_twolines(qestion.question, choices[index])
        

    return selection

def dailyQuestions(questions, rotor, button, screen):
    anwsers = []
    for question in questions:
        anwsers.append(questionAnwser(question, rotor, button, screen))
    return anwsers
    
def saveQuestionsAnwsers(date, questions, anwsers): 
    with open('data/questions/'+str(date)+'.csv', mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['question', 'anwser', 'points'])
        for i in range(len(questions)):
            writer.writerow([questions[i].question, anwsers[i][0], anwsers[i][1]])
    return None


def selectionMenuCategories(categories, rotor,  button, screen):
    rotor.close()
    rotor = RotaryEncoder(a=21, b=20, max_steps=len(categories)-1, wrap=False)
    index = 0
    while button.value != True:
        index = int(rotor.steps)
        selection = categories[index]
        screen.write(categories[index])

    return categories[index]

def selectionMenuActivities(category, activities, rotor, button, screen):
    rotor.close()
    index = 0
    valid_activities = filter_categories(activities, category)
    rotor = RotaryEncoder(a=21, b=20, max_steps=len(valid_activities)-1, wrap=True)
    while button.value != True:
        index = int(rotor.steps)
        selection = valid_activities[index]
        screen.write(valid_activities[index].code)

    return valid_activities[index]


def send_data():
    # if connexion internet stable
    today = get_date()
    url = "http://192.168.1.49:5000/upload"
    
    for filename in os.listdir("data/time"):
        try:
            with open("data/time/"+str(filename), "rb") as csvfile:
                response = requests.post(url, files = {"file": csvfile}, timeout=10)
                print("sent file")
                if response.ok:
                    if filename != today+str(".csv"):
                        #os.remove("data/time/"+str(filename))
                        print("Et hop on remove "+ str(filename)+ " de la carte SD de la pi")
        except: 
            print("error when sending file")
            
def get_quote():   # NOT WORKING, I MIGHT NEED TO USE BEAUTIFULSOUP
    url = "http://localhost:5000/quote"  
    try:
        response = requests.get(url)
        print(response)
        
        print("updated quote")
        print(response.text)
        return response.text

    except: pass


categories = category_list(activities)


last_time = time.time()
if __name__ == "__main__":

    while True:
        date = get_date()
        try:
            open('data/questions/'+str(date)+'.csv', mode='r')
        except:
            saveQuestionsAnwsers(date ,questions, dailyQuestions(questions, rotor, button, screen))
        try:
            open('data/time/'+str(date)+'.csv', mode='r')
        except:
            with open('data/time/'+str(date)+'.csv', mode='w') as csv_file:
                writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['start_time', 'end_time', 'activity'])

        start_time = get_time()
        screen.idle()
        rotor.wait_for_rotate()
        current_category = selectionMenuCategories(categories, rotor, button, screen)
        current_activity = selectionMenuActivities(category=current_category, activities=activities, rotor=rotor, button=button, screen=screen)
        last_activity = current_activity
        write_action(date, start_time, get_time(), last_activity)
        if time.time() - last_time > 10:
            send_data()
            last_time = time.time()
