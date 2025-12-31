s1 = int(input('Enter a speed: '))
s2 = int(input('Enter a speed: '))
s3 = int(input('Enter a speed: '))
speedavg = (s1+s2+s3)/3
if s1>speedavg:
    print(s1, 'is higher than the average speed.')
if s2>speedavg:
    print(s2, 'is higher than the average speed.')
if s3>speedavg:
    print(s3, 'is higher than the average speed.')