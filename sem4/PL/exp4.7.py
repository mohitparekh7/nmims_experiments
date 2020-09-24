java_course = {"John", "Jack", "Jill", "Joe"}
python_course = {"Jake", "John", "Eric", "Jill"}
print(python_course)
print(java_course)
d1 = python_course.difference(java_course)
d2 = python_course.union(java_course)
print(d1)
print(d2)
print(d2-d1)
print(java_course|python_course)
