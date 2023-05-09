
# Timetable Scheduling Algorithm

from course.model import Course
from utils.enums.Language import Language
from utils.enums.Program import Program
from utils.enums.Semester import Semester
from utils.enums.Year import Year

class TimetableScheduling():
    """Auto & Manual Scheduling
    Auto-scheduling steps:
    - Collect input parameters from the user.
    - Create a list of all available time slots for each instructor.
    - Sort the list of time slots for each instructor in ascending order of time.
    - All instructor courses will be in (Lecture/Section) table, waitting to be updated with time and room
    - Initialize the schedule with an empty list of tables.
    ******** Loop:
    - For each table to be generated, select one instructor from the list of available instructors.
    - For the selected instructor, select the earliest available time slot that does not conflict with any already scheduled time slots.
    - If a suitable time slot is found, assign the instructor to the table and add the table to the schedule.
    - If no suitable time slot is found, try the next instructor in the list.
    - If all instructors have been tried and no suitable time slot has been found, reschedule a conflicting table with a lower priority to a later time slot.
    - Loop until all tables have been generated and scheduled.
    ********


    """

    def __init__(self, year, semester, language, regulation, department, num_tables=0, lecture=True, *args, **kwargs):
        super(TimetableScheduling, self).__init__(*args, **kwargs)
        self.year = year # 1 or 2 or 3 or 4
        self.semester = semester
        self.language = language # 'ar' or 'en' or 'fr'
        self.regulation = regulation
        self.department = department
        self.lecture = lecture
        self.num_tables = num_tables # the number of tables to be generated
        self.instructors = [] # the available instructors
        self.instructors_availability  = {} # all instructors with a sorted list for each one with their available times.
        self.table_courses = []
        self.instructors_courses  = {} # all instructors with their courses.
        # Initialize the schedule with an empty list of tables.
        self.schedule  = []

    #######################################################################################################################
    ### Auto
    #######################################################################################################################
    # Main Functon
    def auto_scheduling(self):
        pass

    def get_instructors_availability(self):
        """
            - Create a list of all available time slots for each instructor from InstructorTime table
            - Sort the list of time slots for each instructor in ascending order of time.
            - Repeat those steps on all instructurs and add to dict
        """
        # Get all doctors those match the constraints for this table
        all_instructors = self.get_table_instructors()
        for each_instructor in all_instructors:
            # Get instructor free time sorted in ascending order
            sorted_available_time = self.get_instructor_sorted_available_time(each_instructor.id)
            self.instructors_availability[each_instructor.name] = sorted_available_time

    def get_table_instructors(self):
        """ Get all doctors those match the constraints for this table """
        # Get the courses those match the constraints
        self.table_courses = Course.query.filter(
            semester=self.semester,
            year=self.year,
            language=self.language,
            regulation_id=self.regulation,
            department_id=self.department
        ).all()
        # Get records from lecture/section table by got courses
        records = []
        if self.lecture:
            for each_course in self.table_courses:
                records = records + Lecture.query.filter_by(course_id=each_course.id).all()
        else:
            for each_course in self.table_courses:
                records = records + Section.query.filter_by(course_id=each_course.id).all()
        self.instructor_listing(records)

    def instructor_listing(self, records):
        """ Make instructors list from db records """
        instructors_list = []
        for each_record in records:
            instructors_list.append(Instructor.query.get(each_record.instructor_id))
        self.instructors = instructors_list

    def get_instructor_sorted_available_time(self, instructor_id):
        """ Get instructor free time sorted in ascending order """
        # Create a list of all available time slots for each instructor from InstructorTime table
        return Inst







    #######################################################################################################################
    ### Manual
    #######################################################################################################################
    # Main Functon
    def manual_scheduling(self, num_tables):
        pass




