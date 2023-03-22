# Welcome to Foondamate AI 
# This will help you to solve your mathematical equations and return all the steps needed to solve the equation
import re

def solve_linear_equation():
    """
    Solves a linear equation in one variable and returns the steps taken to solve the equation.
    The equation should be entered in the format "ax + b = c", where a, b, and c are integers or decimals.
    """
    # Get the equation from the user
    equation = input("Enter a linear equation in one variable (e.g. 'ax - b = c'): ")
    
    # Parse the equation using regular expressions
    match1 = re.match(
        r'^\s*(?P<a>[-+]?(\d+(\.\d*)?|\.\d+))\s*x\s*[-+]\s*'
        r'(?P<b>[-+]?(\d+(\.\d*)?|\.\d+))\s*=\s*'
        r'(?P<c>[-+]?(\d+(\.\d*)?|\.\d+))\s*$',
        equation
    )
    
    if not match1:
        print("Invalid equation format. Please enter the equation in the format 'ax + b = c', where a, b, and c are integers or decimals.")
        return
    
    # Extract the coefficients and constants from the equation
    a = float(match1.group('a'))
    b = float(match1.group('b'))
    c = float(match1.group('c'))
    
    # Solve the equation
    steps = []

    # check if the equation contains a plus sign or a minus sign
    if '+' in equation:
        # Subtract b from both sides of the equation
        steps.append(f"Original equation: {equation} \n")
        steps.append(f"Subtract {b:.2f} from both sides:\n")
        steps.append(f"{a:.2f}x + {b:.2f} - {b:.2f} = {c:.2f} - {b:.2f}\n")
        steps.append("Simplify the equation \n")        
        steps.append(f"{a:.2f}x = {c-b:.2f}\n")

        # Divide both sides by a to isolate x
        steps.append("Dividing both sides by {}:".format(a) + "\n")
        x = (c-b)/a
        steps.append("x = {:.2f}".format(x))
    elif '-' in equation:
        # Add b to both sides of the equation
        steps.append(f"Original equation: {equation} \n")
        steps.append(f"Add {b:.2f} to both sides:\n")
        steps.append(f"{a:.2f}x - {b:.2f} + {b:.2f} = {c:.2f} + {b:.2f}\n")
        steps.append("Simplify the equation \n")
        steps.append(f"{a:.2f}x = {c+b:.2f}\n")

        # Divide both sides by a to isolate x
        steps.append("Dividing both sides by {}:".format(a) + "\n")
        x = (c+b)/a
        steps.append("x = {:.2f}".format(x))
        
    
    # Print the steps
    for step in steps:
        print(step)
    
    return x
    
    
    
