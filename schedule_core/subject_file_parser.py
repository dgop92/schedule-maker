from dataclasses import dataclass
from typing import List

day_index_dict = {
    "M": 0,
    "T": 1,
    "W": 2,
    "R": 3,
    "F": 4,
    "S": 5,
}


""" 

The JSON subject a structure is the following

{
  "0": {
    "name": str,
    "nrc": str,
    "professors": [
        { "first_name": str, "last_name": str },
        ...
    ],
    "schedule": [
      {
        "day": str,
        "interval": { "start": str, "end": str },
      },
      ...
    ]
  },
  "1": {
     ...
  }
},

day: M|T|W|R|F|S
hour: HHMM, HH: military hour, MM: minutes
"""


def get_courses_from_subject(json_subject):

    json_courses = json_subject.values()
    courses = []
    for json_course in json_courses:

        professors = get_professors_from_class(json_course["professors"])
        schedule = get_schedule_from_course_class(json_course["schedule"])

        course = UniCourse(
            name=json_course["name"],
            nrc=json_course["nrc"],
            professors=professors,
            schedule=schedule,
        )
        courses.append(course)

    return courses


def get_schedule_from_course_class(course_schedules):
    schedule = []
    for course_class in course_schedules:
        class_schedule = get_schedule_form_class(course_class)
        schedule.extend(class_schedule)
    return schedule


def get_schedule_form_class(course_class):
    interval = course_class["interval"]
    day = course_class["day"]

    day_index = day_index_dict[day]
    start = interval["start"]
    end = interval["end"]
    start_idx = int(start[0:2]) - 6
    end_idx = int(end[0:2]) - 6

    return [(hour_index, day_index) for hour_index in range(start_idx, end_idx)]


def get_professors_from_class(professors):

    new_professors = []
    for professor in professors:
        full_name = professor["first_name"] + " " + professor["last_name"]
        new_professors.append(full_name)

    return new_professors

""" 
schedule: a list of tuples that represents the position in a matrix.
where columns are the days of the week and rows are the hour of the day

- days goes from monday to sunday
- hours goes from 6:30 to 19:30
"""
@dataclass
class UniCourse:
    name: str
    nrc: int
    professors: List[str]
    schedule: List[tuple]
