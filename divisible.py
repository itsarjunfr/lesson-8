dividend = int(input('Enter dividend: '))
divisor = int(input('Enter divisor: '))
if dividend%divisor==0:
    print(dividend, 'is divisible by', divisor)
else:
    print(dividend, 'is not divisible by', divisor)