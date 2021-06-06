import xlwt

MARGIN = 2
CHUNK_SIZE = 10

DAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)

HOURS = (
    "6:30 AM",
    "7:30 AM",
    "8:30 AM",
    "9:30 AM",
    "10:30 AM",
    "11:30 AM",
    "12:30 PM",
    "1:30 PM",
    "2:30 PM",
    "3:30 PM",
    "4:30 PM",
    "5:30 PM",
    "6:30 PM",
    "7:30 PM",
)


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def get_sheet_base(work_book, name):
    work_sheet = work_book.add_sheet(name)
    for j, day in enumerate(DAYS, start=MARGIN + 1):
        work_sheet.write(MARGIN, j, day)
    for i, hour in enumerate(HOURS, start=MARGIN + 1):
        work_sheet.write(i, MARGIN, hour)

    return work_sheet


def put_set_of_courses_on_worksheet(work_sheet, set_of_courses):

    subject_list_jpos = MARGIN + len(DAYS) + 3
    subject_list_ipos = MARGIN

    for course in set_of_courses:
        work_sheet.write(subject_list_ipos, subject_list_jpos, course.name)
        work_sheet.write(
            subject_list_ipos, 
            subject_list_jpos + 1, 
            int(course.nrc)
        )
        for pos in course.schedule:
            work_sheet.write(
                MARGIN + 1 + pos[0], 
                MARGIN + 1 + pos[1], 
                int(course.nrc))
        subject_list_ipos += 1


def save_possible_schedules_on_workbook(possible_schedules):

    possible_schedules_by_chunks = chunks(possible_schedules, CHUNK_SIZE)
    schedule_number = 1

    for i, schedule_chunk in enumerate(possible_schedules_by_chunks, start=1):
        workbook = xlwt.Workbook()
        for schedule in schedule_chunk:
            sheet = get_sheet_base(workbook, f"Schedule {schedule_number}")
            put_set_of_courses_on_worksheet(sheet, schedule)
            schedule_number += 1
        workbook.save(f"my_schedules/schedule-group-number-{i}.xls")
