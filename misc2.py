"""import misc
print(misc.pi)
print(misc.gravity)"""

a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)


x = True
y = False
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)


y="sumanth"
for x in y:
    print(x)


num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str:",type(num_str))

print(num_int+int(num_str))

print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))



print(range(10))

print(list(range(10)))

print(list(range(2, 8)))

print(list(range(20, 2,-2)))



genre = [1,2,3,4]

# iterate over the list using index
for i in genre:
	continue


student_name = 'Jules'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')