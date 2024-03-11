#list indexing in python
Languages=["Turkish","English","Somali","Swahili"]
print(Languages[0])
print(Languages[-1])
print(Languages[-1])
print(Languages[-1:4])
print(Languages[0:4])
#numbers append
numbers=[1,2,3,4,5]
numbers.append(10)
print("After append:",numbers)
student_marks=[10,40,50,60]
assessment=[20,30,40,50]
student_marks.extend(assessment)
print("List after append:",student_marks)
Languages=['English','Kiswahili','Swahili']
Languages[0]='Somali'
print(Languages)
del Languages[1]
print(Languages)
print(Languages[-2])
for language in Languages:
    print(language)
my_tuple=('a','b','c','d','e','f','c',)
print(my_tuple.count('c'))
print(my_tuple.index('c'))