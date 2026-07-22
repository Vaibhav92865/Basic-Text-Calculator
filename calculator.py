print("================================")
print("      BASIC TEXT CALCULATOR     ")
print("================================")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("\nChoose Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter your choice (1-4): ")
if choice == "1":
    result = num1 + num2
    print("Answer =", result)

elif choice == "2":
    result = num1 - num2
    print("Answer =", result)

elif choice == "3":
    result = num1 * num2
    print("Answer =", result)

elif choice == "4":
    result = num1 / num2
    print("Answer =", result)

else:
    print("Invalid Choice")
