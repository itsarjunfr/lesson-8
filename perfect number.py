num = int(input('Enter a number: '))
factor = 0
for i in range(1,num):
    if num%i==0:
        factor = factor+i

if factor == num:
    print(num, 'is a perfect number.')
else:
    print(num, 'is not a perfect number.')