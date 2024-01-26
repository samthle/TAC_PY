class DoctorAppointmentSystem:
    def __init__(self):
        self.patients = {}
        self.visits = {}

    def add_patient(self, id, name, family_name, age, height, weight):
        if id in self.patients:
            return "error: this ID already exists"
        if age < 0 or height < 0 or weight < 0:
            return "error: invalid input"
        
        self.patients[id] = {
            "name": name,
            "family_name": family_name,
            "age": age,
            "height": height,
            "weight": weight
        }
        return "patient added successfully"

    def display_patient(self, id):
        if id not in self.patients:
            return "error: invalid ID"
        
        patient_info = self.patients[id]
        return f"patient name: {patient_info['name']}\npatient family name: {patient_info['family_name']}\npatient age: {patient_info['age']}\npatient height: {patient_info['height']}\npatient weight: {patient_info['weight']}"

    def add_visit(self, id, beginning_time):
        if id not in self.patients:
            return "error: invalid id"
        if beginning_time < 9 or beginning_time >= 18:
            return "error: invalid time"
        if beginning_time in self.visits.values():
            return "error: busy time"
        
        self.visits[id] = beginning_time
        return "visit added successfully!"

    def delete_patient(self, id):
        if id not in self.patients:
            return "error: invalid id"
        
        del self.patients[id]
        for key, value in list(self.visits.items()):
            if value == id:
                del self.visits[key]
        return "patient deleted successfully!"

    def display_visit_list(self):
        schedule = "SCHEDULE:\n"
        for key, value in self.visits.items():
            patient_info = self.patients[key]
            time_str = f"{value:02d}:00"
            schedule += f"{time_str}: {patient_info['name']} {patient_info['family_name']}\n"
        return schedule

system = DoctorAppointmentSystem()

while True:
    command = input()
    parts = command.split()
    
    if parts[0] == "add" and parts[1] == "patient":
        result = system.add_patient(int(parts[2]), parts[3], parts[4], int(parts[5]), int(parts[6]), int(parts[7]))
        print(result)
    
    elif parts[0] == "display" and parts[1] == "patient":
        result = system.display_patient(int(parts[2]))
        print(result)
    
    elif parts[0] == "add" and parts[1] == "visit":
        result = system.add_visit(int(parts[2]), int(parts[3]))
        print(result)
    
    elif parts[0] == "delete" and parts[1] == "patient":
        result = system.delete_patient(int(parts[2]))
        print(result)
    
    elif parts[0] == "display" and parts[1] == "visit" and parts[2] == "list":
        result = system.display_visit_list()
        print(result, end="")
    
    elif parts[0] == "exit":
        break
    
    else:
        print("invalid command")