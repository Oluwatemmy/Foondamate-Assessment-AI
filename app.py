# Welcome to Foondamate AI 
# This will help you to solve your mathematical equations and return all the steps needed to solve the equation

print('Welcome')


def solve_linear_equation(equation):
    try:
        # An equation with the format ax + b = c
        # Split the equation into left and right hand sides
        left, right = equation.split('=')

        # Split the left side into its two coefficients
        a, b = left.split('x')
        if a == 'x':
            a = float(1)
        a = float(a.strip())
        b = float(b.replace(' ', '').strip())

        # Convert the right side to a float
        c = float(right.strip())

        # check if the equation contains a plus sign
        if '+' in left:
            # Subtract b from both sides of the equation
            print(f"Subtract {b} from both sides \n")

            print(f"{a:.2f}x + {b:.2f} = {c:.2f} \n")

            print(f"{a:.2f}x + {b:.2f} - {b:.2f} = {c:.2f} - {b:.2f} \n")

            # Simplify
            print("Simplify \n")
            sub_ans = f"{a:.2f}x = {c-b:.2f}\n"
            print(sub_ans)

            # Divide both sides by a to isolate x
            # print("Divide both side by common factor")
            if a == 0:
                raise ValueError('Invalid equation: coefficient of x cannot be zero.')
            
            print(f"Divide both sides by {a:.2f} \n")

            print(f"{a}x = {c-b:.2f} \n")
            x = (c - b) / a
            print(f"x = {x:.2f} \n")

        # check if the equation contains a minus sign
        elif '-' in left:
            # Add b to both sides of the equation
            print(f"Add {b} to both sides \n")

            print(f"{a:.2f}x - {b:.2f} = {c:.2f} \n")

            print(f"{a:.2f}x - {b:.2f} + {b:.2f} = {c:.2f} + {b:.2f} \n")

            # Simplify
            print("Simplify \n")
            add_ans = f"{a:.2f}x = {c+b:.2f}\n"
            print(add_ans)

            # Divide both sides by a to isolate x

            if a == 0:
                raise ValueError('Invalid equation: coefficient of x cannot be zero.')
            
            print(f"Divide both sides by {a:.2f} \n")

            print(f"{a}x = {c+b:.2f} \n")
            x = (c + b) / a
            print(f"x = {x:.2f} \n")

        # Return the solution 
        return f"x = {x:.2f}"
    except (ValueError, TypeError) as e:
        # Handle errors by printing an error message
        print(f"Error: {e}")
        return None, None
    
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
