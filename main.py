from course import Course
from student import Student

roster = []

math = Course("Algebra I")
language = Course("Spanish I")
science = Course("Earth Science")
history = Course("U.S. History I")
phys_ed = Course("Physical Education I")
comsci = Course ("Computer Science")
napping = Course("Napping")

# TODO: Add two more courses of your choosing✅

test_student = Student("Jill", "Sample")
test_student.add_course(math)
test_student.add_course(language)
test_student.add_course(science)
test_student.add_course(history)

test_student2 = Student("Bill", "Sample")
test_student2.add_course(math)
test_student2.add_course(phys_ed)
test_student2.add_course(science)
test_student2.add_course(history)

# TODO Add a third test student and assign them four classes✅
test_student1 = Student("Miguel", "Baez")
test_student1.add_course(math)
test_student1.add_course(phys_ed)
test_student1.add_course(science)
test_student1.add_course(comsci)

# TODO Add all the test students to a list of your own creation✅
roster.append(test_student)
roster.append(test_student1)
roster.append(test_student2)

# TODO print student_list✅
print(roster)
# TODO iterate over each of the students in the list and print their names and course schedules.
    # Each iteration should:
        # print the student
for eachStudent in roster:
    print(eachStudent.get_first_name())
    print(eachStudent.courses)

"""
 for this part you may need to review the other skeleton code to:
    - see how to get items from a list
    - see if there is code (like a function) in that file you can call in this file
    - verify that running this file gets you the correct output with information from that file
  Also, review syntax of pulling items from a list from other activities 
"""