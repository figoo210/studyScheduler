# Collect input parameters from the user
num_tables = int(input("Enter the number of tables to be generated: "))
num_doctors = int(input("Enter the number of available doctors: "))
doctor_availability = {}
for i in range(num_doctors):
    doctor_name = input("Enter the name of doctor {}: ".format(i+1))
    availability = input("Enter the doctor's available times (comma-separated): ")
    availability = [int(x) for x in availability.split(",")]
    doctor_availability[doctor_name] = availability

# Create a list of all available time slots for each doctor
available_slots = {}
for doctor in doctor_availability:
    available_slots[doctor] = []
    for i in range(0, len(doctor_availability[doctor]), 2):
        start_time = doctor_availability[doctor][i]
        end_time = doctor_availability[doctor][i+1]
        for j in range(start_time, end_time):
            available_slots[doctor].append(j)

# Sort the list of time slots for each doctor
for doctor in available_slots:
    available_slots[doctor].sort()

# Initialize the schedule with an empty list of tables
schedule = []

# Generate and schedule each table
for i in range(num_tables):
    table_scheduled = False
    for doctor in available_slots:
        for slot in available_slots[doctor]:
            conflicts = False
            for scheduled_table in schedule:
                if scheduled_table['doctor'] == doctor and slot in scheduled_table['time']:
                    conflicts = True
                    break
            if not conflicts:
                table = {'doctor': doctor, 'time': [slot]}
                schedule.append(table)
                table_scheduled = True
                break
        if table_scheduled:
            break
    if not table_scheduled:
        # Reschedule a conflicting table with lower priority
        for scheduled_table in schedule:
            for doctor in available_slots:
                if scheduled_table['doctor'] == doctor:
                    for slot in available_slots[doctor]:
                        if slot not in scheduled_table['time']:
                            scheduled_table['time'].append(slot)
                            scheduled_table['time'].sort()
                            table_scheduled = True
                            break
                    if table_scheduled:
                        break
                if table_scheduled:
                    break
            if table_scheduled:
                break

# Print the schedule
for i, table in enumerate(schedule):
    print("Table {}: Doctor {} at time {}".format(i+1, table['doctor'], table['time']))