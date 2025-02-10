num1 = int(input("Enter first number:"))
operation = input("Enter operation(*,+,-,/:)")
num2 = int(input("Enter second number:"))


if operation =="*":
    ans = (num1*num2)
    print(ans)

elif operation =="+":
    ans = (num1 + num2)
    print(ans)

elif operation =="-":
    ans = (num1 - num2)
    print(ans)

elif operation =="*":
    ans = (num1 * num2)
    print(ans)

elif operation =="/":
    ans = (num1 / num2)
    print(ans)

else:
    print("invalid operation")