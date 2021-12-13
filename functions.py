# Create a function
def sayHello(name = "Sam"):
    print(f'Hello {name}')

# sayHello('Jake Ike')

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

# print(getSum(3, 4))
num = getSum(3, 4)
print(num)

# Lambda function
getSum = lambda num1, num2 : num1 + num2
