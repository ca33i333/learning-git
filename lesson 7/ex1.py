student = {
    "name" : "Nguyen Van A",
    "class_" : "12A1",
    "student_id" : 12345678
}

del student["name"]
print(student)

class_ = student.pop("class_")
print(student)


student.clear()
print(student)
