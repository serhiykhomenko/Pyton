# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
age = int(input("Enter your age:"))
if age < 0:
    print("wrong age")
elif age < 18:
     print ("You are not yet of legal age")
else:
    print ("You have become an adult")

    a = 10
    b = 5

    if a % b == 0:
        print("Ділиться")
    print(a // b)
else :
    print("Ділиться з залишком")
    print(a % b)

    salary = int(input("Please enter your salary: "))
    years_worked = int(input("Please enter the number of years you have worked: "))

    if years_worked <= 3:
        salary += salary * 0.1
    elif years_worked >= 3:
        salary += salary * 0.2

    if salary < 4000:
        salary += 1000
    elif salary >= 4000:
        salary += 500

    print("Your new salary is: ", salary)


