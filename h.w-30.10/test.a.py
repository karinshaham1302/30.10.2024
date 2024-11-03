# start

total_students: int = int(input('Enter the total number:'))
students_class: int = 30

full_class = total_students // students_class
student_remain = total_students % students_class

print(f'number of full class: {full_class}')
print(f'number of student remain: {student_remain}')

# stop
