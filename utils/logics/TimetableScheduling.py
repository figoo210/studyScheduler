
# Timetable Scheduling Algorithm

class TimetableScheduling():
    """Auto & Manual Scheduling
    Auto-scheduling:
    1- Collect input parameters from the user, such as the doctors' available times and the number of tables to be generated.
    2- Create a list of all available time slots for each doctor.
    3- Sort the list of time slots for each doctor in ascending order of time.
    4- Initialize the schedule with an empty list of tables.
    5- For each table to be generated, select one doctor from the list of available doctors.
    6- For the selected doctor, select the earliest available time slot that does not conflict with any already scheduled time slots.
    7- If a suitable time slot is found, assign the doctor to the table and add the table to the schedule.
    8- If no suitable time slot is found, try the next doctor in the list.
    9- If all doctors have been tried and no suitable time slot has been found, reschedule a conflicting table with a lower priority to a later time slot.
    10- Repeat steps 5-9 until all tables have been generated and scheduled.


    """

    def __init__(self, *args, **kwargs):
        super(TimetableScheduling, self).__init__(*args, **kwargs)
        # Collect input parameters from the user
        self.num_tables = 0 # the number of tables to be generated
        self.num_doctors = 0 # the number of available doctors
        self.doctor_availability  = {}

    #######################################################################################################################
    ### Auto
    #######################################################################################################################
    # Main Functon
    def auto_scheduling(self):
        pass

    def get_each_doctor_availability(self):
        pass

    #######################################################################################################################
    ### Manual
    #######################################################################################################################
    # Main Functon
    def manual_scheduling(self):
        pass




