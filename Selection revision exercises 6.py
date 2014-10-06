print("this program will ask for three numbers and display the bigger number.")
first_number = int(input("please enter your first number: "))
second_number = int(input("please enter your second number: "))
third_number = int(input("please enter your third number: "))
if first_number > second_number and first_number > third_number:
    print(first_number)
elif second_number > first_number and second_number > third_number:
    print(second_number)
else:
    print(third_number)
print("thanks for using this program")

