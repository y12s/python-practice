import statistics as st
import cmath

print('hello world')
a = 45
b = 67
sum = a + b
print(f'the sum of two numbers is: {sum}')

#area of rectangle 

l = 45
b = 56
area = l * b
print(f'the area of given rectangle is {area}cm')

'''
area of triangle when the value is to be taken from user
'''
# base = int(input('Enter the length of base in cm: ' ))
# height = int(input('Enter the length of height in cm: ' ))

# area = 0.5 * base * height
# print('****************')
# print(f'the area of triangle is: {area}cm^2')
# print('****************')


marks = [45,6,43,45,53,35,24,74,78,75,3,8,35,89,99]
mean = st.mean(marks)
print(round(mean,2))

# practice for school practicals 

a = 4+5
print(a)

yatharth_singh = 'Yatharth Singh Rajput'
print(yatharth_singh)

arhar = 'dal'
x = 5
y = 6
complex_test = complex(x, y)
print(complex_test)

None_test = None

string_test = 'dummy string'
list_test = [34, 66, 76, 4545, 34455, 'sneha', 'raghav']
print(list_test)

list_test[1] = 99

print(list_test)

boolean_test = 112>23
print(boolean_test)