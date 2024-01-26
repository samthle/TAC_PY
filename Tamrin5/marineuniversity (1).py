import argparse

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
        print("Invalid type")
        return

    if not user_id.isdigit():
        print("Invalid ID")
        return

    if ' ' in user_name:
        print("Invalid name")
        return

    if len(user_password) < 4 or ' ' in user_password or not any(char in '*.!@$%^&()' for char in user_password):
        print("Invalid password")
        return

    if user_type == 'S':
        user = Student(user_id, user_name, user_password)
    else:
        user = Professor(user_id, user_name, user_password)

    print("Signed up successfully!")

def login(user_id, user_password):
    # Validation logic for user login
    # Simulated logic for student or professor menu
    if isinstance(user, Student):
        current_menu = "student menu"
    elif isinstance(user, Professor):
        current_menu = "professor menu"
    else:
        print("Invalid user type")

    print("Logged in successfully!")
    print(f"Entered {current_menu}")

def add_course(course_name, course_id, capacity):
    # Validation logic for adding a course
    course = Course(course_id, course_name, capacity)
    print("Course added successfully!")

def show_course_list():
    # Display course list
    print("Course list:")

def get_course(course_id):
    # Retrieve course details
    print("Course details retrieved successfully!")

def log_out():
    # Logout logic
    print("Logged out successfully!")
    print("Entered log in/sign up menu")

def student_menu():
    # Logic for student menu
    print("Student menu")

def professor_menu():
    # Logic for professor menu
    print("Professor menu")

def main():
    parser = argparse.ArgumentParser(description="Educational Platform Simulation")
    parser.add_argument("--user_type", help="User Type (S for Student, P for Professor)")
    parser.add_argument("--user_id", help="User ID")
    parser.add_argument("--user_name", help="User Name")
    parser.add_argument("--user_password", help="User Password")
    parser.add_argument("--course_name", help="Course Name")
    parser.add_argument("--course_id", help="Course ID")
    parser.add_argument("--capacity", help="Course Capacity")

    args = parser.parse_args()

    if args.user_type and args.user_id and args.user_name and args.user_password:
        signup(args.user_type, args.user_id, args.user_name, args.user_password)
    else:
        print("Invalid command")

if __name__ == "__main__":
    main()
