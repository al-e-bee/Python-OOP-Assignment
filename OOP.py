# Created the class of Student with the attributes of name, email, and grades. The class has methods for adding a grade, calculating the average grade, and displaying the student's information.

class Student:
    def __init__(self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades
        
    def add_grade(self, grade):
        self.grades.append(grade)
        
    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def display_info(self):
       print(f"Name: {self.name}, Email: {self.email}, Grades: {self.grades}, Average Grade: {self.average_grade()}")
   
# Built a method called grades_tuple that returns the grades as a tuple. Attempted to modify the tuple by appending a new grade to demonstrate that they are immutable. Using a try-except block to catch the TypeError that occurs when trying to modify a tuple.     
    def grades_tuple(self):
        grades_tuple = tuple(self.grades)    
        try:
            grades_tuple[0] = 100
        except TypeError:
            print("Cannot modify a tuple. Tuples are immutable.")
        return grades_tuple

# Added a __repr__ method to the Student class that returns a string representation of the Student object for the get_student_by_email function that appears later in the code. This is useful for debugging and logging purposes by providing clarity on whether the function returns the student's name and email or a "Student not found." message.
    def __repr__(self):
        return f"Student(Name: {self.name}, Email: {self.email})"


# 3 Student Ojects created with the name, email, and grades attributes. The grades are stored in a list.
student1 = Student("Jessica Day", "jessica.day@example.com",[92, 97, 88])
student2 = Student("Nick Miller", "nick.miller@example.com", [77, 89, 94])
student3 = Student("Winston Bishop", "winston.bishop@example.com", [88, 79, 95])


# Added two new grades to each Student Object using the add_grade method
student1.add_grade(99)
student1.add_grade(92)

student2.add_grade(85)
student2.add_grade(82)

student3.add_grade(89)
student3.add_grade(87)


# Prints each students info using the display_info method, as well as printing the average grade for each student using the average_grade method.
student1.display_info()
student2.display_info()
student3.display_info()


# Created a dictionary called student_dict that maps each student's email to their corresponding Student object. 
student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}

# Developed a function called get_student_by_email that takes an email as input and returns the student's name and email if found in the student_dict. If no email matches, it returns a "Student not found." message. 
def get_student_by_email(email):
    return student_dict.get(email, "Student not found.")
      
print(get_student_by_email("jessica.day@example.com"))
print(get_student_by_email("winston.bishop@example.com"))
print(get_student_by_email("schmidt@example.com"))


# Created a set of all the unique grades across all students
unique_grades = set(student1.grades + student2.grades + student3.grades)
print("All unique grades across all students:", unique_grades)

# Calling the grades_tuple method for each student to demonstrate that the grades are returned as a tuple and cannot be modified.
print(student1.grades_tuple())
print(student2.grades_tuple())
print(student3.grades_tuple())


# Performed list operations to remove the last grade from each student's grades list using the .pop() method. Followed by accessing and printing the first and last grade for each student using indexing. Lastly, printed the number of grades weach student as using the len() function.
student1.grades.pop()
student2.grades.pop()
student3.grades.pop()

print("First and last grade for each student:")
print(f"{student1.name}: First Grade: {student1.grades[0]} Last Grade: {student1.grades[-1]}")
print(f"{student2.name}: First Grade: {student2.grades[0]} Last Grade: {student2.grades[-1]}")
print(f"{student3.name}: First Grade: {student3.grades[0]} Last Grade: {student3.grades[-1]}")

print(f"Number of grades for {student1.name}: {len(student1.grades)}")
print(f"Number of grades for {student2.name}: {len(student2.grades)}")
print(f"Number of grades for {student3.name}: {len(student3.grades)}")


# Using regular expressions to validate the email format for each student. The regex pattern checks the validity of the email format. If it is valid, it prints a message indicating that the email is valid; otherwise, it prints a message indicating that the email is invalid. 
import re 
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def validate_email(email):
    if re.match(email_pattern, email):
        return f"Email {email} is valid."
    else:
        return f"Email {email} is not a valid email address."

print(validate_email(student1.email))
print(validate_email(student2.email))
print(validate_email(student3.email))
print(validate_email("does_notwork_at.example_dotcom"))


# Using regex to count how many grades are above 90 for all students. The regex pattern checks for grades that are 90 or above, counts the total number of matches, and prints the count. 
grade_pattern = r'\b([9][0-9]|100)\b'

def count_grades_above_90(students):
    count = 0
    for student in students:
        grades_str = ' '.join(map(str, student.grades))
        count += len(re.findall(grade_pattern, grades_str))
    return count

print(f"The total count of grades above 90 for all students is: {count_grades_above_90([student1, student2, student3])}")

