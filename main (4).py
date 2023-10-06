'''
Implement a functiion called sort_students that takes a list of student objects as input and sorts the
list based on their CGPA (Cumalative Grade Point Average) in descending order. Each student object
has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function
with different input lists of studies.
'''

class Student:
  
  def __init__(self,name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
                          key=lambda student: student.cgpa,
                          reverse=True)
  # Syntax - lambda arg;exp
  return sorted_students


# Example usage:
students = [
  Student("Jerinedison", "122CSA01", 8.7),
  Student("Kathir", "122CSA02", 9.0),
  Student("Yogesh", "122CSA03", 9.5),
  Student("Nithish", "122CSA04", 9.6),
  Student("Narayanan", "122CSA05", 9.9)
]

sorted_students = sort_students(students)

# Print the sorted list of  students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
student.roll_number,
                                                     student.cgpa))