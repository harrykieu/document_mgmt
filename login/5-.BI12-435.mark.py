import ast

class manager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.filename = "manager_data.txt"

#open and write initial value
    def input_students(self, num_students):
        with open(self.filename, "a") as file:
            for i in range(num_students):
                student_id = input("Enter student ID: ")
                student_name = input("Enter student name: ")
                student_dob = input("Enter student date of birth (DD/MM/YYYY): ")
                student = {"sid": student_id, "name": student_name, "dob": student_dob, "courses": {}} #add emty "courses" dictionary
                self.students.append(student)
                file.write(f"{student}\n")

    def input_courses(self, num_courses):
        with open(self.filename, "a") as file:
            for i in range(num_courses):
                course_id = input("Enter course ID: ")
                course_name = input("Enter course name: ")
                course = {"cid": course_id, "name": course_name, "marks": {}} #add empty "marks" dictionary
                self.courses.append(course)
                file.write(f"{course}\n")


#mark
    def input_marks(self):
        course_id = input("Enter course ID: ")
        student_id = input("Enter student ID: ")
        mark = input("Enter mark: ")
        with open(self.filename, "r") as file:
            lines = file.readlines()
        found = False
        for i, line in enumerate(lines):
            if course_id in line and student_id in line:
                found = True
                course_dict = ast.literal_eval(line.strip())
                if input("Would you like to change or append the mark? (c/a): ").lower() == "c":
                    old_mark = course_dict["marks"].get(student_id)
                    if old_mark:
                        old_mark_list = old_mark.split(", ")
                        try:
                            mark_index = old_mark_list.index(mark)
                            old_mark_list[mark_index] = input("Enter new mark: ")
                            new_mark_str = ", ".join(old_mark_list)
                            course_dict["marks"][student_id] = new_mark_str
                            line = str(course_dict)
                            lines[i] = line
                            print(f"Mark changed successfully! New marks: {new_mark_str}")
                        except ValueError:
                            print(f"Mark {mark} not found!")
                else:
                    if "marks" not in course_dict:
                        course_dict["marks"] = {}
                        course_dict["marks"][student_id] = course_dict["marks"].get(student_id, "") + f", {mark}"
                        line = str(course_dict)
                        lines[i] = line
                        print(f"Mark {mark} added successfully!")
                break
        else:
            student_dict = next((s for s in self.students if s['sid'] == student_id), None)
            course_dict = next((c for c in self.courses if c['cid'] == course_id), None)
            if student_dict and course_dict:
                if "marks" not in course_dict:
                    course_dict["marks"] = {}
                    course_dict["marks"][student_id] = mark
                    student_dict["courses"][course_id] = mark
                    course_str = str(course_dict)
                    lines.append(course_str + "\n")
                    print("Mark added successfully!")
            else:
                print("Wrong ID, Please try again!")
        with open(self.filename, "w") as file:
            file.writelines(lines)

#the left
    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(f"{student['sid']}: {student['name']}")

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(f"{course['cid']}: {course['name']}")

    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(f"{student['sid']}: {student['name']}")

    def show_student_marks(self):
        course_id = input("Enter course ID: ")
        student_id = input("Enter student ID: ")
        for course in self.courses:
            if course["cid"] == course_id:
                print(f"Marks for {course['name']}:")
                if student_id in course["marks"]:
                    mark = course["marks"][student_id]
                    print(f"{student_id}: {mark}")
                    break
                else:
                    print("Wrong ID, Please try again!")
                    break
        else:
            print("Wrong ID, Please try again!")


# main program
if __name__ == "__main__":
    manager = manager()

    num_students = int(input("Enter the number of students: "))
    manager.input_students(num_students)

    num_courses = int(input("Enter the number of courses: "))
    manager.input_courses(num_courses)

    while True:
        print("\nChoice: ")
        print("Select an option:")
        print("1. Input student marks")
        print("2. Show list courses")
        print("3. Show list students")
        print("4. Show student marks")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            manager.input_marks()
        elif choice == "2":
            manager.list_courses()
        elif choice == "3":
            manager.list_students()
        elif choice == "4":
            manager.show_student_marks()
        elif choice == "5":
            print("\nExited!")
            break
        else:
            print("\nError input")


   
