from app import solve_linear_equation


if __name__ == '__main__':
    # Prompt the user for the equation
    equation = input("Enter an equation in the form ax + b = c: ")

    # Solve the equation
    x = solve_linear_equation(equation)

    # Print the solution
    if x is not None:
        print("Solved")
    else:
        print("Not solved")