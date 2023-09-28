import statistics as st

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
base = int(input('Enter the length of base in cm: ' ))
height = int(input('Enter the length of height in cm: ' ))

area = 0.5 * base * height
print('****************')
print(f'the area of triangle is: {area}cm^2')
print('****************')


marks = [45,6,43,45,53,35,24,74,78,75,3,8,35,89,99]
mean = st.mean(marks)
print(round(mean,2))

