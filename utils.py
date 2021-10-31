
class Activity:
    name = ""
    category = ""
    code = ""
    duration = 0.5
    description = ""
    value = 0

    def __init__(self, name, category, code, duration, description, value):
        self.name = name
        self.category = category
        self.code = code
        self.duration = duration
        self.description = description
        self.value = value


class Question:
    code = ""
    question = ""
    anwsers =  []

    def __init__(self, code, question, anwsers):
        self.code = code
        self.question = question
        self.anwsers = anwsers


class Machine_State():
    current_date = 0
    date_last_record = 0
    hour_last_record = 0
    

    def __init__(self, date, date_last_record, hour_last_record):
        self.current_date = date
        self.date_last_record = date_last_record
        self.hour_last_record = hour_last_record