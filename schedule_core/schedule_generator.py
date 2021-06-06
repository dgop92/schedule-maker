import itertools
from schedule_core.subject_file_parser import get_courses_from_subject
from schedule_core.utils import json_utils

def any_element_inside_list1_in_list2(list1, list2):
    return any(item in list1 for item in list2)


def is_schedule_no_overlapped(set_of_courses):

    all_schedules = []
    for course in set_of_courses:
        all_schedules.extend(course.schedule)

    set_schedules = set(all_schedules)

    return len(all_schedules) == len(set_schedules)


def get_possible_schedule(list_of_user_subjects):
    list_of_set_of_courses = get_list_of_set_of_courses(list_of_user_subjects)
    combinations = itertools.product(*list_of_set_of_courses)
    possible_combinations = filter(is_schedule_no_overlapped, combinations)
    return list(possible_combinations)

def get_list_of_set_of_courses(list_of_user_subjects):

    list_of_set_of_courses = []

    for user_subject in list_of_user_subjects:

        subject_path = user_subject["subject_file_path"]

        courses_from_subject = get_courses_from_subject(
            json_utils.load_data_from_json_file(subject_path)
        )
        professors_to_ignored = user_subject.get("professors_to_ignored", [])
        nrcs_to_ignored = user_subject.get("nrc_to_ignored", [])

        if professors_to_ignored:
            courses_from_subject = filter(
                lambda course: not any_element_inside_list1_in_list2(
                    professors_to_ignored, course.professors
                ),
                courses_from_subject,
            )
        if nrcs_to_ignored:
            courses_from_subject = filter(
                lambda course: course.nrc not in nrcs_to_ignored, courses_from_subject
            )

        list_of_set_of_courses.append(list(courses_from_subject))

    return list_of_set_of_courses
