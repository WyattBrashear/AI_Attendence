import json
import datetime

#Mark the student Present (P), Tardy (T), or Absent (A)
def mark(type, studentname, class_name):
    try:
        with open(f"./attendence_{datetime.date.today()}.json", 'r') as f:
            atten_json = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        atten_json = []
    with open(f"./attendence_{datetime.date.today()}.json", 'w') as f:
        atten_student = {
            "name": studentname,
            "mark": type,
            "time_of_mark": str(datetime.datetime.now()),
            "class": class_name
        }
        atten_json.append(atten_student)
        json.dump(atten_json, f, indent=5)
#Example usage
#mark("P", "Jane Doe", "Math")