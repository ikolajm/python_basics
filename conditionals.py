x = 10
y = 5

if x > y:
    print(f'{10} is greater than {y}')
elif x==y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')

if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')

if x > 2 and x <=10:
    print(f'{x} is greater than 2 and less than or equal to 10')

if x > 2 or x <=10:
    print(f'{x} is greater than 2 or less than or equal to 10') 

if not x == y:
    print(f'{x} is not equal to {y}')

numbers = [1,2,3,4,5]

if x in numbers:
    print(x in numbers)

if x not in numbers:
    print(x not in numbers)

if x is y:
    print(x is y)

if x is not y:
    print(x is not y)