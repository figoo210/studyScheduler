
# Timetable Scheduling Algorithm

class TimetableScheduling():
    """Auto & Manual Scheduling
    Auto-scheduling:
    1- Collect input parameters from the user.
    2- Create a list of all available time slots for each instructor.
    3- Sort the list of time slots for each instructor in ascending order of time.
    4- Initialize the schedule with an empty list of tables.
    5- For each table to be generated, select one instructor from the list of available instructors.
    6- For the selected instructor, select the earliest available time slot that does not conflict with any already scheduled time slots.
    7- If a suitable time slot is found, assign the instructor to the table and add the table to the schedule.
    8- If no suitable time slot is found, try the next instructor in the list.
    9- If all instructors have been tried and no suitable time slot has been found, reschedule a conflicting table with a lower priority to a later time slot.
    10- Repeat steps 5-9 until all tables have been generated and scheduled.


    """

    def __init__(self, year, language, regulation, department, *args, **kwargs):
        super(TimetableScheduling, self).__init__(*args, **kwargs)
        self.year = year # 1 or 2 or 3 or 4
        self.language = language # 'ar' or 'en' or 'fr'
        self.regulation = regulation
        self.department = department
        self.num_tables = 0 # the number of tables to be generated
        self.num_instructors = 0 # the number of available instructors
        self.instructors_availability  = {} # all instructors with a sorted list for each one with their available times.

    #######################################################################################################################
    ### Auto
    #######################################################################################################################
    # Main Functon
    def auto_scheduling(self):
        pass

    def get_each_instructor_availability(self):
        pass

    #######################################################################################################################
    ### Manual
    #######################################################################################################################
    # Main Functon
    def manual_scheduling(self, num_tables):
        pass




