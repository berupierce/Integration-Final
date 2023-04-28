"""
Calculator
"""
__author__ = "Beru Pierce"


def introduction():
    """writes an introduction
    :return: introduction to user
    """
    print("Hi there!")
    name_user = input("What is your name? ")
    return "Hello, " + name_user + "!" + "\n"


# https://www.youtube.com/watch?v=63nw00JqHo0
def calculate_sum(a, b):
    """adds 2 numbers
    :param a: first user input number
    :param b: second user input number
    :return: sum of a and b
    """
    result = a + b
    return result


def calculate_diff(c, d):
    """subtracts 2 numbers
    :param c: first user input number
    :param d: second user input number
    :return: difference of c and d
    """
    result = c - d
    return result


def calculate_product(e, f):
    """multiplies two numbers
    :param e: first user input number
    :param f: second user input number
    :return: product of e and f
    """
    result = e * f
    return result


def lower_num(g, h):
    """lower of two numbers
    :param g: user input number
    :param h: user input number
    :return: lower number
    """
    if g < h:
        return g
    elif h < g:
        return h
    elif g == h:
        return g, h


def exponents(a, b):
    """base to a power
    :param a: user input base number
    :param b: user input power
    :return: base raised to power
    """
    result = a ** b
    return result


def division(a, b):
    """division
    :param a: user input dividend
    :param b: user input divisor
    :return: quotient
    """
    result = a / b
    return result


def floor_division(a, b):
    """how many times divisor goes into dividend
    :param a: user input dividend
    :param b: user input divisor
    :return: quotient
    """
    result = a // b
    return result


def modulus(a, b):
    """remainder
    :param a: user input dividend
    :param b: user input divisor
    :return: remainder
    """
    result = a % b
    return result


def upper_num(g, h):
    """find the greater number
    :param g: user input number
    :param h: user input number
    :return: greater number
    """
    if g > h:
        return g
    elif h > g:
        return h
    elif g == h:
        return g, h


def menu():
    """while loop menu of calculator options.
    """
    print(introduction())
    print("Welcome to the Menu!")
    while True:
        print("[1] Addition")
        print("[2] Subtraction")
        print("[3] Multiplication")
        print("[4] Exponents")
        print("[5] Division")
        print("[6] Smallest and Largest Number")
        print("[7] Loop to find sum of numbers")
        print("[8] Boolean to see if number is even or odd")
        print("[0] Exit program", "\n")
        option = input("Which option would you like to do? ")
        if option == "1":
            print("Addition selected.")
            try:
                num1 = int(input("Enter a number: "))
                num2 = int(input("Enter a second number: "))
                sum_numbers = calculate_sum(num1, num2)
                print("The sum is", sum_numbers, "\n")
            except ValueError:
                print("Invalid entry.", "\n")
        elif option == "2":
            print("Subtraction selected.")
            try:
                num3 = int(input("Enter a number: "))
                num4 = int(input("Enter a second number: "))
                difference = calculate_diff(num3, num4)
                print("The difference is", +difference, "\n")
            except ValueError:
                print("Invalid entry.", "\n")
        elif option == "3":
            print("Multiplication selected.")
            try:
                num5 = int(input("Enter a number: "))
                num6 = int(input("Enter a second number: "))
                product = calculate_product(num5, num6)
                print("The product is", +product, "\n")
            except ValueError:
                print("Invalid entry.", "\n")
        elif option == "4":
            print("Exponents selected.")
            try:
                num_7 = int(input("Enter the base number: "))
                num_8 = int(input("Enter the power: "))
                product = exponents(num_7, num_8)
                print(num_7, "raised to the power", num_8, "is", product, "\n")
            except ValueError:
                print("Invalid entry.", "\n")
        elif option == "5":
            print("Division selected.")
            try:
                num_9 = int(input("Enter the dividend: "))
                num_10 = int(input("Enter the divisor: "))
                quotient = division(num_9, num_10)
                floor_div = floor_division(num_9, num_10)
                remainder = modulus(num_9, num_10)
                print(num_9, "divided by", num_10, "is,", quotient)
                print(num_10, "goes into the number", num_9, floor_div, " times")
                print(num_10, "divided by", num_9, "has a remainder of", remainder, "\n")
            except ValueError:
                print("Invalid entry.", "\n")
        elif option == "6":
            print("Smaller and larger number selected.")
            try:
                num_a = int(input("Now enter a number: "))
                num_b = int(input("Now enter another number: "))
                lower = lower_num(num_a, num_b)
                upper = upper_num(num_a, num_b)
                print("The smaller number is: ", + lower)
                print("The larger number is: ", + upper, "\n")
            except ValueError:
                print("Invalid entry.", "\n")
        elif option == "7":
            print("Sum of numbers selected.")
            try:
                print("Here is a list of numbers between 1 and 50:")
                for x in range(1, 51):
                    print(x, end=", ")
                    x += 1
                print("We can use loops to find the sum of numbers. Enter 0 to end.")
                total = 0
                number_entered = int(input("Enter any number: "))
                while number_entered != 0 and number_entered <= 50:
                    total += number_entered
                    number_entered = int(input("Enter any number: "))
                print("Total= ", total, "\n")
            except ValueError:
                print("Invalid entry.", "\n")
        elif option == "8":
            print("Odd or even number selected.")
            try:
                odd_even = int(input("Enter a number: "))
                if not odd_even % 2 == 0:
                    print("Number is odd.", "\n")
                else:
                    print("Number is even.", "\n")
            except ValueError:
                print("Invalid entry.", "\n")
        elif option == "0":
            print("Exiting.")
            exit()
        else:
            print("Invalid option.", "\n")


menu()

# stackoverflow.com
# help from the think python book
