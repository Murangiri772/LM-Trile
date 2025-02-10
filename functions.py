# Built-In functions/Standard-Library

y = max(45,80,55,43,21,12,11)
print("The maximum value is", y)

x = min(65,98,34,76,98,22,42)
print("The minimum value is",x)


# User-defined functions

def school ():
    print("eMobilis")

school()

def add():
    num1 = 5
    num2 = 3
    print(num1+num2)
add()

# Parameter/variable and Argument/value stored
def multiply(a , b):
    print(a *b )
multiply(10,56)
multiply(15,56)
multiply(10,5)
multiply(10,6)




def students(name,age,gender,fees,position):
    print(name,age,gender,fees,position)
students("Brandon", 25, "male",5000,1)
students("Brian", 21, "male",5000,2)
students("Brenda", 22, "female",5000,3)
students("Mawira", 23, "male",5000,4)
students("Edwine", 20, "male",5000,5)
students("Belinda", 19, "female",5000,6)

# A program to display details of five patients
# Using a user-defined function,implement parameter and argument

def patient(fullname, gender, age ,disease):
    print(fullname, gender, age, disease)
patient("Otieno Murithi", "male", 35, "bilhazia")
patient("Jeniffer Rupezz", "male", 40, "maleria")
patient("Ann Waiguru", "male", 29, "malaria")
patient("othiambo onyango", "male", 30, "cholera")
patient("Kenneth Matiba", "male", 35, "typhoid")














