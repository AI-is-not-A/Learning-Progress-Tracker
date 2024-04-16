import re

courses = ["Python", "DSA", "Databases", "Flask"]
points_to_complete = [600, 400, 480, 550]
students_dict = {}

errors = {"error credentials": "Incorrect credentials.",
          "error first name": "Incorrect first name.",
          "error last name": "Incorrect last name.",
          "error email": "Incorrect email.",
          "email already taken": "This email is already taken.",
          "error points format": "Incorrect points format."}


class Student:

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        # Python, DSA, Databases, Flask
        self.points = [0, 0, 0, 0]
        self.notified = [0, 0, 0, 0]

    @staticmethod
    def verify_name(name):
        # ACCEPTED characters in full name
        # Only ASCII characters accepted.
        # A-Z, a-z,
        # - (hyphens, 1+, not first and last of any part of the name, not adjacent to each other)
        # ´ (apostrophes, 1+, not first and last of any part of the name, not adjacent to each other)
        pattern = r"^[A-Za-z]+(?:['-]?[A-Za-z]+)+$"
        if not re.match(pattern, name):
            return False
        return True

    def set_first_name(self, first_name):
        # first name = first part of full name before the first blank space, at least 2 characters
        if not self.verify_name(first_name):
            raise Exception(errors["error first name"])
        self.first_name = first_name

    def set_last_name(self, last_name):
        # last name = second part of full name after first blank space, at least 2 characters
        for name in last_name.split():
            if not self.verify_name(name):
                raise Exception(errors["error last name"])
        self.last_name = last_name

    def set_email(self, email):
        # name part, @, domain part ??
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(pattern, email):
            raise ValueError(errors["error email"])
        self.email = email

    def add_points(self, points):
        is_new_in_course = [0, 0, 0, 0]
        for i in range(4):
            if points[i] > 0 and self.points[i] == 0:
                is_new_in_course[i] = 1
            self.points[i] += points[i]
        return is_new_in_course


class StudentManagement:

    def __init__(self):
        super().__init__()
        self.last_id = 20000
        self.students_added = 0

    def add_student(self, credentials):
        try:
            credentials_lst = credentials.strip().split()
            self.check_credentials(credentials_lst)

            # name part, @, domain part ??
            self.is_email_available(credentials_lst[-1])

            new_student = Student()
            # first name = first part of full name before the first blank space, at least 2 characters
            new_student.set_first_name(credentials_lst[0])
            # last name = second part of full name after first blank space, at least 2 characters
            new_student.set_last_name(' '.join(credentials_lst[1:-1]))
            # name part, @, domain part ??
            new_student.set_email(credentials_lst[-1])

            students_dict[self.last_id] = new_student
            self.students_added += 1
            self.last_id += 1
            print("The student has been added.")
        except Exception as e:
            print(e)

    def check_credentials(self, credentials_lst):
        if len(credentials_lst) < 3:
            raise Exception(errors["error credentials"])

    def print_added_students(self):
        print(f"Total {self.students_added} students have been added.")
        self.students_added = 0

    def is_email_available(self, email):
        for student in students_dict.values():
            if str(student.email).lower() == email.lower():
                raise Exception(errors["email already taken"])
        return False

    def print_list(self):
        print("Students:")
        if len(students_dict) == 0:
            print("No students found.")
        else:
            for _id in students_dict.keys():
                print(_id)

    def check_student_id(self, _id):
        if not _id.isdigit() or int(_id) not in students_dict:
            raise Exception(f"No student is found for id={_id}.")

    def check_points_format(self, points_format_lst):
        for i in range(1, 5):
            if not points_format_lst[i].isdigit() or int(points_format_lst[i]) < 0:
                raise Exception(errors["error points format"])

    def add_points(self, points):
        points_lst = points.strip().split()
        try:
            if len(points_lst) != 5:
                raise Exception(errors["error points format"])
            self.check_student_id(points_lst[0])
            self.check_points_format(points_lst)
        except Exception as e:
            print(e)
            return

        points_lst = [int(n) for n in points_lst]
        student = students_dict[points_lst[0]]
        is_new_in_course = student.add_points(points_lst[1:5])
        stats.update(is_new_in_course, points_lst[1:5])

        print("Points updated")

    def print_points(self, _id):
        student = students_dict[_id]
        print(f"{_id} points: "
              f"Python={student.points[0]}; "
              f"DSA={student.points[1]}; "
              f"Databases={student.points[2]}; "
              f"Flask={student.points[3]}")

    def find_student(self, _id):
        try:
            self.check_student_id(_id)
        except Exception as e:
            print(e)
            return
        self.print_points(int(_id))

    def filter_not_completed(self, item, course_index):
        key, value = item
        for i in range(4):
            if value.points[course_index] == points_to_complete[course_index]:
                return True
        return False

    def notify(self):
        # 0 = email, 1 = full_name, 2 = course
        mail_template = "To: {0}\nRe: Your Learning Progress\nHello, {1}! You have accomplished our {2} course!"

        notified_students = set()
        for course_index in range(4):
            to_notify_students = dict(filter(lambda item: self.filter_not_completed(item, course_index),
                                             students_dict.items()))

            for _id, student in to_notify_students.items():
                if not student.notified[course_index]:
                    print(mail_template.format(student.email,
                                               f"{student.first_name} {student.last_name}",
                                               courses[course_index]))
                    students_dict[_id].notified[course_index] = 1
                    notified_students.add(_id)

        print(f"Total {len(notified_students)} students have been notified.")


class Stats:
    TEMPLATE = "Most popular: {0}\n" \
               "Least popular: {1}\n" \
               "Highest activity: {2}\n" \
               "Lowest activity: {3}\n" \
               "Easiest course: {4}\n" \
               "Hardest course: {5}"
    N_A = "n/a"

    def __init__(self):
        self.num_students = 0
        self.num_enrolled_students = [0, 0, 0, 0]
        self.num_completed_tasks = [0, 0, 0, 0]
        self.total_points = [0, 0, 0, 0]

    def update(self, is_new_in_course, points):
        for i in range(4):
            if is_new_in_course[i] == 1:
                self.num_enrolled_students[i] += 1
            if points[i] != 0:
                self.num_completed_tasks[i] += 1
                self.total_points[i] += points[i]

    def get_min_max_course(self, list_obj):
        # if no students have enrolled in any of the courses or data can't be retrieved, print n/a
        if sum(list_obj) == 0:
            return [self.N_A, self.N_A]
        minimum = min(list_obj)
        maximum = max(list_obj)
        results = [[], []]
        # if multiple courses qualify for any category, list the names of all such courses.
        # If any course is already included in a category, it cannot be included in the opposite category.
        for i in range(4):
            if list_obj[i] == maximum:
                results[0].append(courses[i])
            if list_obj[i] == minimum:
                results[1].append(courses[i])
        if minimum == maximum:
            return [', '.join(results[0]), self.N_A]
        return [', '.join(results[0]), ', '.join(results[1])]

    def print_general_statistics(self):
        # The most popular has the biggest number of enrolled students;
        popularity = self.get_min_max_course(self.num_enrolled_students)
        # Higher student activity means a bigger number of completed tasks (number of submissions)
        activity = self.get_min_max_course(self.num_completed_tasks)

        # The easiest course has the highest average grade per assignment (average score)
        average_score = [0, 0, 0, 0]
        for i in range(4):
            if self.num_completed_tasks[i] != 0:
                average_score[i] = self.total_points[i] / self.num_completed_tasks[i]
        difficulty = self.get_min_max_course(average_score)

        print(
            self.TEMPLATE.format(popularity[0], popularity[1], activity[0], activity[1], difficulty[0], difficulty[1]))

    def print_course_statistics(self, asked_course):
        course_index = -1
        for i in range(4):
            if courses[i].lower() == asked_course.strip().lower():
                course_index = i
                break

        if course_index == -1:
            print("Unknown course.")
            return

        print(courses[course_index])
        print("id    points    completed")

        sorted_ids = sorted(students_dict,
                            key=lambda i2: students_dict[i2].points[course_index],
                            reverse=True)

        for _id in sorted_ids:
            student_points = students_dict[_id].points[course_index]
            if student_points == 0:
                break
            student_points_str = str(student_points) + ((9 - len(str(student_points))) * " ")
            percentage_completed = student_points / points_to_complete[course_index]
            print(_id, student_points_str, f"{round(percentage_completed * 100, 1)}%")


stats = Stats()
