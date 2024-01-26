class User:
    def __init__(self, user_id, user_name, user_password):
        self.id = user_id
        self.name = user_name
        self.password = user_password

class Student(User):
    def __init__(self, user_id, user_name, user_password):
        super().__init__(user_id, user_name, user_password)
        self.courses_taken = []

class Professor(User):
    def __init__(self, user_id, user_name, user_password):
        super().__init__(user_id, user_name, user_password)
        self.courses_taught = []

class Course:
    def __init__(self, course_id, course_name, capacity):
        self.course_id = course_id
        self.course_name = course_name
        self.capacity = capacity
        self.students_enrolled = []

def signup(user_type, user_id, user_name, user_password):
    if user_type not in ['S', 'P']:
        print("invalid type")
        return
    if not user_id.isdigit():
        print("invalid id")
        return
    if ' ' in user_name:
        print("invalid name")
        return
    if len(user_password) < 4 or ' ' in user_password or not any(char in '*.!@$%^&()' for char in user_password):
        print("invalid password")
        return
    print("signed up successfully!")

def login(user_id, user_password):
    print("logged in successfully!")
    print(f"entered {'student' if isinstance(user, Student) else 'professor'} menu")

def add_course(course_name, course_id, capacity):
    if ' ' in course_name:
        print("invalid course name")
        return
    if not course_id.isdigit():
        print("invalid course id")
        return
    if not capacity.isdigit():
        print("invalid course capacity")
        return
    print("course added successfully!")
    
def show_course_list():
    print("course list:")

def get_course(course_id):
    print("course added successfully!")

def log_out():
    print("logged out successfully!")
    print("entered log in/sign up menu")

def main():
    current_menu = "log in/sign up menu"
    while True:
        command = input("edu ")
        if command == "edu exit edu":
            print("Program terminated.")
            break
        if command == f"edu current menu edu":
            print(current_menu)
            continue
        if current_menu == "log in/sign up menu":
            command_parts = command.split()
            if len(command_parts) < 4 or command_parts[0] != "edu" or command_parts[3] != "-i" or command_parts[5] != "-n" or command_parts[7] != "-p" or command_parts[8] != "edu":
                print("invalid command")
                continue
            signup(command_parts[2], command_parts[4], command_parts[6], command_parts[8])
        elif current_menu == "student menu":
            pass
        elif current_menu == "professor menu":
            pass
        else:
            print("invalid command")
if __name__ == "__main__":
    main()
