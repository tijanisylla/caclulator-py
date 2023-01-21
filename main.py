# Select an operation
print("========= Select an operation =========")

print("1. ADD (+)")
print("2. SUBTRACT (-)")
print("3. MULTIPLY (X)")
print("4. DIVIDE (/)")

# Create a function to handle the operation.
def calculator():
    operation = input()
    
    if operation == str(1) :
      num1 = input("Enter the first number : ")
      num2 = input("Enter the second number : ")
      print("The result is : " + str(int(num1) + int(num2)))
    elif operation == str(2) :
        num1 = input("Enter the first number : ")
        num2 = input("Enter the second number : ")
        print("The result is : " + str(int(num1) - int(num2)) )
    elif operation == str(3) :
        num1 = input("Enter the first number : ")
        num2 = input("Enter the second number : ")
        print("The result is : " + str(int(num1) * int(num2)) )
    elif operation == str(4) :
        num1 = input("Enter the first number : ")
        num2 = input("Enter the second number : ")
        print("The result is : " + str(int(num1) / int(num2)) )
    else:
        print("Invalid Entry")

if __name__ == "__main__":
    calculator()
    