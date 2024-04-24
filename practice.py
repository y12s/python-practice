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
age = 44
if age>18:
    print('elgible')
else:
    print('not')

year = 2024
if  year%4 == 0 or year%100 == 0 and year%400 == 0:
    print('leap')
else:
    print('not leap')

for count in [1, 2, 3, 4, 5]:
    print(count)

for i in range(5, 5):
    print(i, end ="")

no = int(input('enter no. : '))
for i in range(11):
    mul = no*i
    print(f'{no} x {i} = {mul}')

count = 1
while count <= 5:
    print('hello')
    count += 1


ans = 'y'
while ans == 'y':
    num = int(input('enter no. '))
    if num%2 == 0:
        print('even number')
    else:
        print('odd number')
    ans = input('do you want to continue? : ')

n = int(input('enter number: '))
sum = 0 
i = 1
while i<= n:
    sum = sum + i
    i += 1
print(sum)

age = int(input('enter the no. :'))

if age>=18:
    print('you are eligible for driving')
else:
    print('you are not eligible for driving')

for j in range(1, 11, 3):
    print(j)

i = 1
sum = 0
n = 45
while i<=n:
    sum = sum+n
    i += 1
    print(sum)

print('hlo yatharth')
i = 1
sum = 0
n = 45
while i<n:
    sum = sum+n
    i += 1
    print(sum)


