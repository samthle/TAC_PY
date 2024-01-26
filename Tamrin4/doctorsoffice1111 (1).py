class DoctorAppointmentSystem:
    def __init__(self):
        self.patients = {}
        self.visits = {}

    def get_patient_info(self, id):
        # Renamed from display_patient for clarity
        if id not in self.patients:
            return "error: invalid ID"
        
        patient_info = self.patients[id]
        return f"patient name: {patient_info['name']}\npatient family name: {patient_info['family_name']}\npatient age: {patient_info['age']}\npatient height: {patient_info['height']}\npatient weight: {patient_info['weight']}"

    def get_visit_schedule(self):
        # Renamed from display_visit_list for clarity
        schedule = "SCHEDULE:\n"
        for key, value in self.visits.items():
            patient_info = self.patients[key]
            time_str = f"{value:02d}:00"
            schedule += f"{time_str}: {patient_info['name']} {patient_info['family_name']}\n"
        return schedule

def parse_command(command):
    parts = command.split()
    if not parts:
        return None, []

    return parts[0], parts[1:]

def main():
    system = DoctorAppointmentSystem()

    while True:
        command = input("Enter command: ")
        action, args = parse_command(command)

        if action == "add" and args[0] == "patient":
            result = system.add_patient(int(args[1]), args[2], args[3], int(args[4]), int(args[5]), int(args[6]))
            print(result)

        elif action == "display" and args[0] == "patient":
            result = system.get_patient_info(int(args[1]))
            print(result)

        elif action == "add" and args[0] == "visit":
            result = system.add_visit(int(args[1]), int(args[2]))
            print(result)

        elif action == "delete" and args[0] == "patient":
            result = system.remove_patient(int(args[1]))
            print(result)

        elif action == "display" and args[0] == "visit" and args[1] == "list":
            result = system.get_visit_schedule()
            print(result, end="")

        elif action == "exit":
            break

        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
