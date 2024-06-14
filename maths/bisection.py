import math

def bisection_method(decimal_places):
    # Printing the formula
    print("Bisection Method")

    # Asking user for the function expression
    expression = input("Enter the function expression: ")

    # Asking user for the function values
    x_value = float(input("Enter the value of x: "))
    fa = eval(expression, {"x": x_value, "e": math.e})
    fb = eval(expression, {"x": x_value, "e": math.e})

    # Checking if f(a) and f(b) have opposite signs
    while fa * fb > 0:
        print("The function values at a and b do not have opposite signs. Please enter new values.")
        x_value = float(input("Enter the value of x: "))
        fa = eval(expression, {"x": x_value, "e": math.e})
        fb = eval(expression, {"x": x_value, "e": math.e})

    # Asking user for the initial interval
    a = float(input("Enter the lower bound of the interval: "))
    b = float(input("Enter the upper bound of the interval: "))

    # Printing the initial values
    print("Initial interval: [", a, ",", b, "]")

    # Asking user for confirmation
    confirmed = input("Is the initial interval valid? (y/n): ")
    while confirmed.lower() != 'y':
        # Asking user for new values
        a = float(input("Enter the new lower bound of the interval: "))
        b = float(input("Enter the new upper bound of the interval: "))
        confirmed = input("Is the new interval valid? (y/n): ")

    # Converting decimal_places to precision
    precision = 10 ** -decimal_places

    # Initialize previous root
    prev_root = None

    # Iterating until convergence or desired precision
    while abs(b - a) > precision:
        c = (a + b) / 2  # Calculate the midpoint

        # Printing the values in each iteration
        print("a =", round(a, decimal_places))
        print("b =", round(b, decimal_places))
        print("c =", round(c, decimal_places))

        # Evaluating the function at the midpoint
        fc = eval(expression, {"x": c, "e": math.e})

        if fc == 0:
            break  # c is the root, exit the loop
        elif fa * fc < 0:
            b = c  # Update the interval [a, c]
        else:
            a = c  # Update the interval [c, b]

        # Check if two consecutive roots are equal up to desired decimal places
        if prev_root is not None and round(c, decimal_places) == round(prev_root, decimal_places):
            break  # Convergence reached, exit the loop

        prev_root = c

        # Asking user for confirmation
        confirmed = input("Is the value calculated correct? (y/n): ")
        while confirmed.lower() != 'y':
            # Asking user for new value
            c = float(input("Enter the new value for c: "))
            confirmed = input("Is the new value correct? (y/n): ")

    return round(c, decimal_places)


# Example usage:
decimal_places = int(input("Enter the number of decimal places: "))
root = bisection_method(decimal_places)
print("Root:", root)
