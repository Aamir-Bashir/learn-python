Courses = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'Computer Science'] #this is a list of courses
Numbers = [1, 2, 3, 4, 5] #this is a list of numbers

#Methods of Lists
Courses.append('English') #adds 'English' to the end of the list
Courses.remove('Biology') #removes 'Biology' from the list
Courses.extend(['History', 'Geography']) #adds multiple items to the end of the list
Courses.insert(2, 'Art') #inserts 'Art' at index 2
Courses.pop() #removes the last item from the list
Courses.sort() #sorts the list in alphabetical order
Numbers.reverse() #sorts the list in descending order
Numbers.sort(reverse=True) #we can also sort the list in descending order by this method
print(Courses)
print(Numbers)
print(Courses.index('Mathematics')) #returns the index of 'Mathematics' in the list
#output of the print(Courses.index('Mathematics')) wil be 5 because after sorting the list, 'Mathematics' is at index 5

# looping through a list
Students = ['Alice', 'Bob', 'Charlie', 'David'] #this is a list of students
for student in Students: #this will loop through the list of students
    print(student) #this will print each student in the list

Teachers = ['Mr. Smith', 'Ms. Johnson', 'Dr. Brown'] #this is a list of teachers
for index, teacher in enumerate( Teachers): #this will loop through the list of teachers
    print(index, teacher) #this will print the index and each teacher in the list
#but if we want to start the index from 1 instead of 0, we can use the start parameter in enumerate
for index, student in enumerate(Students, start=1): #this will loop through the list of students starting the index from 1
    print(index, student) #this will print the index starting from 1 and each student in the list

# printing list as a string
print(', '.join(Students)) #this will print the list of students as a string separated by commas
print(' | '.join(Teachers)) #this will print the list of teachers as a string 
#we can separate the items in the list with any character we want, here we used ' | ' and ', 'to separate the items in the list of teachers