from String import course

course = ["MIT","Cybersecurity","Datascience"]
print(course)


# Accessing an element
print(course[2])


# looping through an array
for x in course:
    print("Course is", x)

# Adding a new element into an array
course.append("Laravel")
print(course)

# Removing an element
course.remove("Cybersecurity")
print(course)




