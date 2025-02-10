from classobject import stundent1


class student:
    def __init__(self,name,gender, age):
        self.name = name
        self.gender = gender
        self.age =age



    def study(self):
        print(self.name,"is studying")


student1 = student("Innocent","Male",23)
print(student1.name,stundent1.gender,student1.age)
student2 = student("Abigail","Female",20)
print(student2.name,student2.gender,student2.age)
student3 = student("Peter","Male",17)
print(student3.name,student3.gender,student3.age)