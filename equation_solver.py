# Welcome to Foondamate AI 
# This will help you to solve your mathematical equations and return all the steps needed to solve the equation
import re

def solve_linear_equation(equation):
    """
    Solves a linear equation in one variable and returns the steps taken to solve the equation.
    The equation should be entered in the format "ax + b = c", where a, b, and c are integers or decimals.
    """

    # Get the equation from the user
    while True:
        # Parse the equation using regular expressions
        match1 = re.match(
            r'^\s*(?P<a>[-+]?\s*\d*(\.\d+)?)?\s*x\s*[-+]\s*'
            r'(?P<b>[-+]?\s*\d*(\.\d+)?)\s*=\s*'
            r'(?P<c>[-+]?\s*\d*(\.\d+)?)\s*$',
            equation
        )

        match2 = re.match(
            r'^\s*x\s*[-+]\s*(?P<b>[-+]?\s*\d*(\.\d+)?)\s*=\s*'
            r'(?P<c>[-+]?\s*\d*(\.\d+)?)\s*$',
            equation
        )
        
        # Extract the coefficients and constants from the equation
        a = float(match1.group('a')) if match1 and match1.group('a') else 1
        b = float(match1.group('b')) if match1 else float(match2.group('b'))
        c = float(match1.group('c')) if match1 else float(match2.group('c'))
        
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
            steps.append(f"{a:.2f}x / {a:.2f} = {c-b:.2f} / {a:.2f} \n")

            # Print the answer out
            steps.append("The answer is...")
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
            steps.append(f"{a:.2f}x / {a:.2f} = {c+b:.2f} / {a:.2f} \n")

            # Print the answer out
            steps.append("The answer is...")
            x = (c+b)/a
            steps.append("x = {:.2f}".format(x))
            
        
        # Print the steps
        for step in steps:
            print(step)
        
        return x
    

def linear_equation_func(equation):
    """
        Solves a linear equation in one variable and returns the steps taken to solve the equation.
        The equation should be entered in the format "a(bx + c) + d = e - fx", where a, b, c, d, e and f are integers or decimals.
    """
    # Get linear equation from user
    while True:
        try:
            # Parse equation into components
            equation_parts = equation.split(" ")

            a = float(equation_parts[0].split("(")[0])
            b = float(equation_parts[0].split("(")[1].split("x")[0])
            c = float(equation_parts[2].split(")")[0])
            d = float(equation_parts[4])
            e = float(equation_parts[6])
            f = float(equation_parts[8].split("x")[0])

            c_sign, d_sign, f_sign = equation_parts[1], equation_parts[3], equation_parts[7]

            # Expand the bracket
            equation1 = f"({b}x * {a}) {c_sign} ({c} * {a}) {d_sign} {d} = {e} {f_sign} {f}x\n"
            print("First, expand the bracket...")
            print(equation1)

            c_a = c*a
            equation_2 = f"{b*a}x {c_sign} {c_a} {d_sign} {d} = {e} {f_sign} {f}x\n"
            equation_2i = f"{b*a}x {c_sign} {c_a+d} = {e} {f_sign} {f}x" if d_sign == "+" else f"{b*a}x {c_sign} {c_a-d} = {e} {f_sign} {f}x"
            print("Simplify the equation...")
            print(equation_2)

            print("Further simplify the equation...")
            print(equation_2i + "\n")

            # Solve and remove the bracket
            eval1 = b * a
            eval2 = eval(f"{a}*{c_sign}{c}")
            eval3 = eval(f"{eval2} {d_sign} {d}")

            eval4 = eval(f"{eval1} - {f}") if f_sign == "+" else eval(f"{eval1} + {f}")
            eval5 = eval(f"{e} - {eval3}") if f_sign == "+" else eval(f"{e} - {eval3}")

            print("Move like terms to same side...")
            equation_4 = f"{eval1}x {'-' if f_sign == '+' else '+'} {f}x = {e} {'+' if f_sign == '+' else '-'} {eval3}\n"
            print(equation_4)

            print("Further simplify the equation...")
            equation_5 = f"{eval4}x = {eval5}\n"
            print(equation_5)

            print(f"Divide both side by {eval4}")
            equation_6 = f"{eval4}x / {eval4} = {eval5} / {eval4}\n"
            print(equation_6)

            print("Finally, the answer is...")
            equation_7 = f"x = " + str(eval5/eval4)
            print(equation_7)
            break
        except Exception as e:
            print("Invalid equation format. Please enter the equation in the format 'a(bx + c) + d = e - fx', where a, b, c, d, e, and f are integers or decimals. \n")
