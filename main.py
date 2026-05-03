def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        
        else:
            return "Error: Not divisible by zero"



while True:
    num1 = float(input("Enter your first number: "))
    operator = input("Choose your operation (+,  -,  *,  /): ")
    num2 = float(input("Enter your second number: "))
    result = calculate(num1, num2, operator)
    print(f"{num1}, {operator}, {num2} = {result}\n")
    user_answer = input("do you want to continue? (y/n): ")
    print("\n")
    if user_answer == "n":
        print("Goodbye!")
        break

print("Thank you for using the calculator!")