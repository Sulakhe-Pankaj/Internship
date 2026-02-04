# 50 Basic Python Questions - Solutions
# Each question solved as a separate function

# Question 1: Print your name using print() function
def q1_print_name():
    print("Question 1: Print Name")
    print("Rahul")
    print()

# Question 2: Take two numbers as input and print their sum
def q2_sum_two_numbers():
    print("Question 2: Sum of Two Numbers")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Sum: {num1 + num2}")
    print()

# Question 3: Take user's age and print (no conditions)
def q3_age_input():
    print("Question 3: Age Input")
    age = int(input("Enter your age: "))
    print(f"Your age is: {age}")
    print()

# Question 4: Single-line and multi-line comments
def q4_comments_demo():
    print("Question 4: Comments Demo")
    # This is a single-line comment
    """
    This is a multi-line comment
    It can span multiple lines
    Useful for documentation
    """
    print("Comments demonstrated in code!")
    print()

# Question 5: Create 5 different variables and print their types
def q5_different_variable_types():
    print("Question 5: Different Variable Types")
    string_var = "Hello"
    integer_var = 42
    float_var = 3.14
    boolean_var = True
    complex_var = 3 + 4j
    
    print(f"String: {string_var} -> Type: {type(string_var)}")
    print(f"Integer: {integer_var} -> Type: {type(integer_var)}")
    print(f"Float: {float_var} -> Type: {type(float_var)}")
    print(f"Boolean: {boolean_var} -> Type: {type(boolean_var)}")
    print(f"Complex: {complex_var} -> Type: {type(complex_var)}")
    print()

# Question 6: Store full name and print greeting
def q6_greeting_with_name():
    print("Question 6: Name Greeting")
    name = "Rahul Kumar"
    print(f"Hello, {name}!")
    print()

# Question 7: Assign and reassign variable
def q7_variable_reassignment():
    print("Question 7: Variable Reassignment")
    x = 10
    print(f"Initial value: {x}")
    x = 20
    print(f"After reassignment: {x}")
    print()

# Question 8: Arithmetic operations
def q8_arithmetic_operations():
    print("Question 8: Arithmetic Operations")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    print(f"Addition: {num1} + {num2} = {num1 + num2}")
    print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
    print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
    print(f"Division: {num1} / {num2} = {num1 / num2}")
    print(f"Modulus: {num1} % {num2} = {num1 % num2}")
    print(f"Exponent: {num1} ** {num2} = {num1 ** num2}")
    print(f"Floor Division: {num1} // {num2} = {num1 // num2}")
    print()

# Question 9: Correct variable naming
def q9_variable_naming():
    print("Question 9: Variable Naming")
    # Wrong: 2name = "Value"  # Can't start with number
    # Correct:
    name2 = "Value"  # Variable names must start with letter or underscore
    print(f"Correct variable: {name2}")
    print()

# Question 10: Swap two numbers using third variable
def q10_swap_numbers():
    print("Question 10: Swap Two Numbers")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    print(f"Before swap: a = {a}, b = {b}")
    temp = a
    a = b
    b = temp
    print(f"After swap: a = {a}, b = {b}")
    print()

# Question 11: Multiline message using \n
def q11_multiline_message():
    print("Question 11: Multiline Message")
    message = "Welcome to Python\nThis is line 2\nThis is line 3"
    print(message)
    print()

# Question 12: Input three different data types
def q12_multiple_data_types():
    print("Question 12: Multiple Data Types Input")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    height = float(input("Enter height: "))
    print("Data stored successfully!")
    print()

# Question 13: Calculate simple interest
def q13_simple_interest():
    print("Question 13: Simple Interest")
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest: "))
    time = float(input("Enter time in years: "))
    
    si = (principal * rate * time) / 100
    print(f"Simple Interest: {si}")
    print()

# Question 14: Print type of data entered
def q14_check_data_type():
    print("Question 14: Check Data Type")
    data = input("Enter any data: ")
    print(f"Type of {data}: {type(data)}")
    print()

# Question 15: Use pass keyword in empty function
def q15_pass_keyword():
    print("Question 15: Pass Keyword")
    def empty_function():
        pass
    
    print("Function with pass keyword executed!")
    empty_function()
    print()

# Question 16: Multiply two integers
def q16_multiply_integers():
    print("Question 16: Multiply Two Integers")
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))
    print(f"Multiplication: {num1 * num2}")
    print()

# Question 17: Average of two floating-point numbers
def q17_average_floats():
    print("Question 17: Average of Two Floats")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    average = (num1 + num2) / 2
    print(f"Average: {average}")
    print()

# Question 18: Complex number real and imaginary parts
def q18_complex_number():
    print("Question 18: Complex Number")
    complex_num = 3 + 4j
    print(f"Complex number: {complex_num}")
    print(f"Real part: {complex_num.real}")
    print(f"Imaginary part: {complex_num.imag}")
    print()

# Question 19: Convert int to float and vice versa
def q19_type_conversion():
    print("Question 19: Type Conversion")
    integer = 42
    float_num = 3.14
    
    print(f"Integer to Float: {int_to_float := float(integer)}")
    print(f"Float to Integer: {float_to_int := int(float_num)}")
    print()

# Question 20: Convert string number to integer
def q20_string_to_int():
    print("Question 20: String to Integer")
    num_str = input("Enter a number as string: ")
    num_int = int(num_str)
    print(f"Converted integer: {num_int}")
    print()

# Question 21: Check if variable is True or False
def q21_boolean_check():
    print("Question 21: Boolean Check")
    value = True
    if value:
        print(f"Value is True: {value}")
    else:
        print(f"Value is False: {value}")
    print()

# Question 22: Input name and print length
def q22_string_length():
    print("Question 22: String Length")
    name = input("Enter your name: ")
    print(f"Length of {name}: {len(name)}")
    print()

# Question 23: Join two strings with space
def q23_join_strings():
    print("Question 23: Join Strings")
    str1 = "Hello"
    str2 = "World"
    result = str1 + " " + str2
    print(f"Joined: {result}")
    print()

# Question 24: Convert string number to float
def q24_string_to_float():
    print("Question 24: String to Float")
    num_str = "123.45"
    num_float = float(num_str)
    print(f"Converted: {num_float}, Type: {type(num_float)}")
    print()

# Question 25: Check if number is int or float
def q25_check_number_type():
    print("Question 25: Check Number Type")
    num = input("Enter a number: ")
    if "." in num:
        print(f"{num} is a float")
    else:
        print(f"{num} is an integer")
    print()

# Question 26: Check if two variables have same type
def q26_same_type_check():
    print("Question 26: Same Type Check")
    var1 = 10
    var2 = 20
    var3 = "hello"
    
    print(f"var1 and var2 same type: {type(var1) == type(var2)}")
    print(f"var1 and var3 same type: {type(var1) == type(var3)}")
    print()

# Question 27: Add two string numbers after converting
def q27_add_string_numbers():
    print("Question 27: Add String Numbers")
    str_num1 = input("Enter first number: ")
    str_num2 = input("Enter second number: ")
    result = int(str_num1) + int(str_num2)
    print(f"Sum: {result}")
    print()

# Question 28: Validate mobile number length
def q28_mobile_validation():
    print("Question 28: Mobile Number Validation")
    mobile = input("Enter mobile number: ")
    if len(mobile) == 10:
        print("Valid mobile number!")
    else:
        print("Invalid mobile number!")
    print()

# Question 29: List with different data types
def q29_mixed_list():
    print("Question 29: Mixed Data Types List")
    mixed_list = [42, "Hello", 3.14, True, 3+4j]
    for item in mixed_list:
        print(f"Value: {item}, Type: {type(item)}")
    print()

# Question 30: Convert int to bool and vice versa
def q30_int_bool_conversion():
    print("Question 30: Int-Bool Conversion")
    num = 1
    boolean = bool(num)
    print(f"Integer to Boolean: {num} -> {boolean}")
    
    bool_val = True
    integer = int(bool_val)
    print(f"Boolean to Integer: {bool_val} -> {integer}")
    print()

# Question 31: All arithmetic operators
def q31_all_arithmetic():
    print("Question 31: All Arithmetic Operators")
    a = 20
    b = 3
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Modulus: {a} % {b} = {a % b}")
    print(f"Exponent: {a} ** {b} = {a ** b}")
    print(f"Floor Division: {a} // {b} = {a // b}")
    print()

# Question 32: Assignment operator +=
def q32_assignment_operator():
    print("Question 32: Assignment Operator")
    num = int(input("Enter a number: "))
    print(f"Original: {num}")
    num += 10
    print(f"After += 10: {num}")
    print()

# Question 33: Comparison operators
def q33_comparison_operators():
    print("Question 33: Comparison Operators")
    a = 15
    b = 10
    print(f"{a} == {b}: {a == b}")
    print(f"{a} != {b}: {a != b}")
    print(f"{a} > {b}: {a > b}")
    print(f"{a} < {b}: {a < b}")
    print(f"{a} >= {b}: {a >= b}")
    print(f"{a} <= {b}: {a <= b}")
    print()

# Question 34: Logical operators (and, or)
def q34_logical_operators():
    print("Question 34: Logical Operators")
    num = int(input("Enter a number: "))
    if 10 <= num <= 20:
        print(f"{num} is between 10 and 20")
    else:
        print(f"{num} is NOT between 10 and 20")
    print()

# Question 35: Bitwise AND, OR, XOR
def q35_bitwise_operators():
    print("Question 35: Bitwise Operators")
    a = 5  # 0101
    b = 3  # 0011
    print(f"{a} & {b} (AND): {a & b}")
    print(f"{a} | {b} (OR): {a | b}")
    print(f"{a} ^ {b} (XOR): {a ^ b}")
    print()

# Question 36: Membership - check character in string
def q36_membership_string():
    print("Question 36: Membership in String")
    char = "a"
    string = "apple"
    if char in string:
        print(f"'{char}' exists in '{string}'")
    else:
        print(f"'{char}' does NOT exist in '{string}'")
    print()

# Question 37: Membership in list
def q37_membership_list():
    print("Question 37: Membership in List")
    num = int(input("Enter a number: "))
    list_nums = [10, 20, 30, 40]
    if num in list_nums:
        print(f"{num} exists in list")
    else:
        print(f"{num} does NOT exist in list")
    print()

# Question 38: Identity operators (is, is not)
def q38_identity_operators():
    print("Question 38: Identity Operators")
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    
    print(f"a is b: {a is b}")
    print(f"a is not b: {a is not b}")
    print(f"a is c: {a is c}")
    print()

# Question 39: Bitwise shifts
def q39_bitwise_shifts():
    print("Question 39: Bitwise Shifts")
    a = 5  # 0101
    b = 2
    print(f"{a} << {b} (Left Shift): {a << b}")
    print(f"{a} >> {b} (Right Shift): {a >> b}")
    print()

# Question 40: Complex expression with mixed operators
def q40_complex_expression():
    print("Question 40: Complex Expression")
    a = 10
    b = 5
    c = 3
    result = (a + b) * c > 30 and a < 15 or c == 3
    print(f"Expression result: {result}")
    print()

# Question 41: Check if number is positive
def q41_positive_check():
    print("Question 41: Check Positive")
    num = int(input("Enter a number: "))
    if num > 0:
        print(f"{num} is positive")
    print()

# Question 42: Even or odd
def q42_even_odd():
    print("Question 42: Even or Odd")
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
    print()

# Question 43: Age category (Child/Teen/Adult/Senior)
def q43_age_category():
    print("Question 43: Age Category")
    age = int(input("Enter age: "))
    if age < 13:
        print("Child")
    elif age < 18:
        print("Teen")
    elif age < 60:
        print("Adult")
    else:
        print("Senior")
    print()

# Question 44: Pass or Fail
def q44_pass_fail():
    print("Question 44: Pass or Fail")
    marks = int(input("Enter marks: "))
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")
    print()

# Question 45: Nested if for voting eligibility
def q45_voting_eligibility():
    print("Question 45: Voting Eligibility")
    age = int(input("Enter age: "))
    if age >= 18:
        has_id = input("Do you have an ID? (yes/no): ").lower()
        if has_id == "yes":
            print("Eligible for voting")
        else:
            print("Need ID to vote")
    else:
        print("Not eligible for voting")
    print()

# Question 46: Temperature check
def q46_temperature_check():
    print("Question 46: Temperature Check")
    temp = int(input("Enter temperature: "))
    if temp < 20:
        print("Cold")
    elif 20 <= temp <= 30:
        print("Normal")
    else:
        print("Hot")
    print()

# Question 47: Find largest of three numbers
def q47_largest_of_three():
    print("Question 47: Largest of Three Numbers")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    
    if a >= b:
        if a >= c:
            print(f"Largest: {a}")
        else:
            print(f"Largest: {c}")
    else:
        if b >= c:
            print(f"Largest: {b}")
        else:
            print(f"Largest: {c}")
    print()

# Question 48: Leap year check
def q48_leap_year():
    print("Question 48: Leap Year")
    year = int(input("Enter year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is NOT a leap year")
    print()

# Question 49: Username and password check
def q49_login_check():
    print("Question 49: Login Check")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == "admin" and password == "1234":
        print("Login successful!")
    else:
        print("Invalid credentials!")
    print()

# Question 50: Discount calculation
def q50_discount_calculation():
    print("Question 50: Discount Calculation")
    amount = float(input("Enter purchase amount: "))
    
    if amount > 1000:
        discount = amount * 0.10
        print(f"Discount: 10% = {discount}")
    elif amount > 500:
        discount = amount * 0.05
        print(f"Discount: 5% = {discount}")
    else:
        discount = 0
        print(f"No discount")
    
    final_amount = amount - discount
    print(f"Final amount: {final_amount}")
    print()

# Main function to run all questions
def run_all_solutions():
    print("=" * 60)
    print("50 BASIC PYTHON QUESTIONS - ALL SOLUTIONS")
    print("=" * 60)
    print()
    
    functions = [
        q1_print_name, q2_sum_two_numbers, q3_age_input, q4_comments_demo,
        q5_different_variable_types, q6_greeting_with_name, q7_variable_reassignment,
        q8_arithmetic_operations, q9_variable_naming, q10_swap_numbers,
        q11_multiline_message, q12_multiple_data_types, q13_simple_interest,
        q14_check_data_type, q15_pass_keyword, q16_multiply_integers,
        q17_average_floats, q18_complex_number, q19_type_conversion,
        q20_string_to_int, q21_boolean_check, q22_string_length,
        q23_join_strings, q24_string_to_float, q25_check_number_type,
        q26_same_type_check, q27_add_string_numbers, q28_mobile_validation,
        q29_mixed_list, q30_int_bool_conversion, q31_all_arithmetic,
        q32_assignment_operator, q33_comparison_operators, q34_logical_operators,
        q35_bitwise_operators, q36_membership_string, q37_membership_list,
        q38_identity_operators, q39_bitwise_shifts, q40_complex_expression,
        q41_positive_check, q42_even_odd, q43_age_category,
        q44_pass_fail, q45_voting_eligibility, q46_temperature_check,
        q47_largest_of_three, q48_leap_year, q49_login_check,
        q50_discount_calculation
    ]
    
    while True:
        print("Choose an option:")
        print("1. Run specific question (enter Q number)")
        print("2. Run a range of questions")
        print("3. Exit")
        
        choice = input("Enter choice: ").lower()
        
        if choice == "1":
            try:
                q_num = int(input("Enter question number (1-50): "))
                if 1 <= q_num <= 50:
                    functions[q_num - 1]()
                else:
                    print("Invalid question number!")
            except ValueError:
                print("Invalid input!")
        
        elif choice == "2":
            try:
                start = int(input("Enter start question (1-50): "))
                end = int(input("Enter end question (1-50): "))
                if 1 <= start <= end <= 50:
                    for i in range(start - 1, end):
                        functions[i]()
                else:
                    print("Invalid range!")
            except ValueError:
                print("Invalid input!")
        
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    run_all_solutions()
