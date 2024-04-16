from learning_progress_tracker import *

stu_ma = StudentManagement()


def process_user_input(action):
    while True:
        user_input = input()
        if user_input == "back" and action == "add_student":
            stu_ma.print_added_students()
            break
        elif user_input == "back":
            break
        elif action == "add_student":
            stu_ma.add_student(user_input)
        elif action == "add_points":
            stu_ma.add_points(user_input)
        elif action == "find_student":
            stu_ma.find_student(user_input)
        elif action == "statistics":
            stats.print_course_statistics(user_input)


def main():
    messages = {"no input": "No input",
                "bye": "Bye!",
                "back": "Enter 'exit' to exit the program.",
                "enter student": "Enter student credentials or 'back' to return:",
                "enter exit": "Enter 'exit' to exit the program.",
                "add points": "Enter an id and points or 'back' to return:",
                "find": "Enter an id or 'back' to return:",
                "unknown command": "Unknown command!",
                "statistics": "Type the name of a course to see details or 'back' to quit:"}

    print("Learning progress tracker")

    while True:
        command = input().strip()

        if command == "add students":
            print(messages["enter student"])
            process_user_input("add_student")

        elif command == "exit":
            print(messages["bye"])
            break

        elif command == "":
            print(messages["no input"])

        elif command == "back":
            print(messages["back"])

        elif command == "list":
            stu_ma.print_list()

        elif command == "add points":
            print(messages["add points"])
            process_user_input("add_points")

        elif command == "find":
            print(messages["find"])
            process_user_input("find_student")

        elif command == "statistics":
            print(messages["statistics"])
            stats.print_general_statistics()
            process_user_input("statistics")

        elif command == "notify":
            stu_ma.notify()

        else:
            print(messages["unknown command"])
    exit()


if __name__ == '__main__':
    main()
