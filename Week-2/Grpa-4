# Take operation name from input
operation = input()

if operation == "odd_num_check":
    # Odd number checker
    number = int(input())
    if number % 2 == 0:
        print("no")
    else:
        print("yes")

elif operation == "perfect_square_check":
    # Perfect square checker
    number = int(input())
    if int(number**0.5)**2 == number:
        print("yes")
    else:
        print("no")

elif operation == "vowel_check":
    # Vowel checker
    string = input().lower()
    if ("a" in string or "e" in string or "i" in string or "o" in string or "u" in string) :
        print("yes")
    else:
        print("no")

elif operation == "divisibility_check":
    # Divisibility checker
    number = int(input())
    if number % 2 == 0:
        if number % 3 == 0:
            print("divisible by 2 and 3")
        else:
          print("divisible by 2")
    elif number % 3 == 0:
        print("divisible by 3")
    else:
        print("not divisible by 2 and 3")

elif operation == "palindrominator":
    # Palindrominator
    string = input()
    palindrome = string + string[-2::-1]
    print(palindrome)

elif operation == "simple_interest":
    # Simple interest calculator
    principal_amount = float(input())
    n_years = int(input())
    if n_years < 10:
        interest_rate = 0.05
    else:
        interest_rate = 0.08
    simple_interest = principal_amount * interest_rate * n_years
    print(int(simple_interest))

else:
    print("Invalid Operation")
