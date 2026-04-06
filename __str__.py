class dami_class:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    # def __str__(self):
    #     return f"{self.name} ({self.grade})"


class_obj = dami_class("piyash", "A+")

print(class_obj.__str__())
# print(str(class_obj).__str__())


# class Employee:
#     def __init__(self, name, age, id):
#         self.name = name
#         self.age = age
#         self.id = id
#
#     def __str__(self):
#         return f'{self.name} {self.age} {self.id}'
#
#
# employeeObject = Employee('employeeName', 20, 1101)
#
# print(employeeObject.__str__())
# print(employeeObject)
# print(str(employeeObject))
# print(employeeObject.__repr__())
