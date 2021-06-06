from schedule_display.excel_displayer import save_possible_schedules_on_workbook
from schedule_core.schedule_generator import get_possible_schedule
from schedule_core.utils import json_utils

if __name__ == "__main__":
    user_subjects = json_utils.load_data_from_json_file("my_schedule_info.json")
    possible_schedules = get_possible_schedule(user_subjects)
    save_possible_schedules_on_workbook(possible_schedules)