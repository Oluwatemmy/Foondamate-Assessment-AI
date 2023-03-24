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
    
    if not match1 and not match2:
        print("Invalid equation format. Please enter the equation in the format 'ax + b = c', where a, b, and c are integers or decimals.")
        return
    
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
    


def linear_equ_func():
    equ_format = "a(bx + c) + d = e - fx"
    equ = input(f"Enter your linear equation in this format: {equ_format}: \n")

    # equ = '2(4x + 3) + 6 = 24 - 4x'
    print(f"The equation is: {equ}\n")

    # Splitting the equation into different components.
    equ_parts = equ.split(" ")

    # Extracting the coefficients and constants from the equation
    a, b, c, d, e, f = map(float, [equ_parts[0].split("(")[0], equ_parts[0].split("(")[1].split("x")[0], equ_parts[2].split(")")[0], equ_parts[4], equ_parts[6], equ_parts[8].split("x")[0]])
    c_sign, d_sign, f_sign = equ_parts[1], equ_parts[3], equ_parts[7]

    print("First, expand the bracket...")
    equ1 = f"({b}x * {a}) {c_sign} ({c} * {a}) {d_sign} {d} = {e} {f_sign} {f}x\n"
    print(equ1)

    eval1 = b * a
    eval2 = eval(f"{a}*{c_sign}{c}")

    if eval2 >= 0:
        
        print("Solve and remove the bracket...")
        equ2 = f"{eval1}x + {eval2} {d_sign} {d} = {e} {f_sign} {f}x\n"
        print(equ2)
        
        eval3 = eval(f"{eval2} {d_sign} {d}")
        if eval3 >= 0:
            
            print("Simplify the equation...")
            equ3 = f"{eval1}x + {eval3} = {e} {f_sign} {f}x\n"
            print(equ3)
            
            if f_sign == "+":

                print("Move like terms to same side...")
                equ4 = f"{eval1}x - {f}x = {e} - {eval3}\n"
                print(equ4)

                eval4 = eval(f"{eval1} - {f}")
                eval5 = eval(f"{e} - {eval3}") 

                print("Further simplify the equation...")
                equ5 = f"{eval4}x = {eval5}\n"
                print(equ5)

                print(f"Divide both side by {eval4}")
                equ6 = f"{eval4}x / {eval4} = {eval5} / {eval4}\n"
                print(equ6)

                print("Finally, the answer is...")
                equ7 = f"x = " + str(eval5/eval4)
                print(equ7)
                
            else:
                print("Move like terms to same side...")
                equ4 = f"{eval1}x + {f}x = {e} - {eval3}\n"
                print(equ4)

                eval4 = eval(f"{eval1} + {f}")
                eval5 = eval(f"{e} - {eval3}") 

                print("Further simplify the equation...")
                equ5 = f"{eval4}x = {eval5}\n"
                print(equ5)

                print(f"Divide both side by {eval4}")
                equ6 = f"{eval4}x / {eval4} = {eval5} / {eval4}\n"
                print(equ6)

                print("Finally the answer is...")
                equ7 = f"x = " + str(eval5/eval4)
                print(equ7)
                
        else:
            eval3 = eval3 * -1

            print("Simplify the equation...")
            equ3 = f"{eval1}x - {eval3} = {e} {f_sign} {f}x\n"
            print(equ3)
            
            if f_sign == "+":
                print("Move like terms to same side...")
                equ4 = f"{eval1}x - {f}x = {e} + {eval3}\n"
                print(equ4)

                eval4 = eval(f"{eval1} - {f}")
                eval5 = eval(f"{e} + {eval3}") 

                print("Further simplify the equation...")
                equ5 = f"{eval4}x = {eval5}\n"
                print(equ5)

                print(f"Divide both side by {eval4}")
                equ6 = f"{eval4}x / {eval4} = {eval5} / {eval4}\n"
                print(equ6)

                print("Finally, the answer is...")
                equ7 = f"x = " + str(eval5/eval4)
                print(equ7)

            else:
                print("Move like terms to same side...")
                equ4 = f"{eval1}x + {f}x = {e} + {eval3}\n"
                print(equ4)

                eval4 = eval(f"{eval1} + {f}")
                eval5 = eval(f"{e} + {eval3}") 

                print("Further simplify the equation...")
                equ5 = f"{eval4}x = {eval5}\n"
                print(equ5)

                print(f"Divide both side by {eval4}")
                equ6 = f"{eval4}x / {eval4} = {eval5} / {eval4}\n"
                print(equ6)

                print("Finally, the answer is...")
                equ7 = f"x = " + str(eval5/eval4)
                print(equ7)

    else:
        eval2 = eval2 * -1

        print("Solve and remove the bracket...")
        equ2 = f"{a*b}x - {eval2} {d_sign} {d} = {e} {f_sign} {f}x\n"
        print(equ2)

        eval3 = eval(f"-{eval2} {d_sign} {d}")
        if eval3 >= 0:
            
            print("Simplify the equation...")
            equ3 = f"{eval1}x + {eval3} = {e} {f_sign} {f}x\n"
            print(equ3)
            
            if f_sign == "+":
                print("Move like terms to same side...")
                equ4 = f"{eval1}x - {f}x = {e} - {eval3}\n"
                print(equ4)

                eval4 = eval(f"{eval1} - {f}")
                eval5 = eval(f"{e} - {eval3}")

                print("Further simplify the equation...")
                equ5 = f"{eval4}x = {eval5}\n"
                print(equ5)

                print(f"Divide both side by {eval4}")
                equ6 = f"{eval4}x / {eval4} = {eval5} / {eval4}\n"
                print(equ6)

                print("Finally, the answer is...")
                equ7 = f"x = " + str(eval5/eval4)
                print(equ7)
                
            else:
                print("Move like terms to same side...")
                equ4 = f"{eval1}x + {f}x = {e} - {eval3}\n"
                print(equ4)

                eval4 = eval(f"{eval1} + {f}")
                eval5 = eval(f"{e} - {eval3}") 

                print("Further simplify the equation...")
                equ5 = f"{eval4}x = {eval5}\n"
                print(equ5)

                print(f"Divide both side by {eval4}")
                equ6 = f"{eval4}x / {eval4} = {eval5} / {eval4}\n"
                print(equ6)

                print("Finally, the answer is...")
                equ7 = f"x = " + str(eval5/eval4)
                print(equ7)
                
        else:
            eval3 = eval3 * -1

            print("Simplify the equation...")
            equ3 = f"{eval1}x - {eval3} = {e} {f_sign} {f}x\n"
            print(equ3)
            
            if f_sign == "+":

                print("Move like terms to same side...")
                equ4 = f"{eval1}x - {f}x = {e} + {eval3}\n"
                print(equ4)

                eval4 = eval(f"{eval1} - {f}")
                eval5 = eval(f"{e} + {eval3}")

                print("Further simplify the equation...")
                equ5 = f"{eval4}x = {eval5}\n"
                print(equ5)

                print(f"Divide both side by {eval4}")
                equ6 = f"{eval4}x / {eval4} = {eval5} / {eval4}\n"
                print(equ6)

                print("Finally, the answer is...")
                equ7 = f"x = " + str(eval5/eval4)
                print(equ7)

            else:
                print("Move like terms to same side...")
                equ4 = f"{eval1}x + {f}x = {e} + {eval3}\n"
                print(equ4)

                eval4 = eval(f"{eval1} + {f}")
                eval5 = eval(f"{e} + {eval3}") 

                print("Further simplify the equation...")
                equ5 = f"{eval4}x = {eval5}\n"
                print(equ5)

                print(f"Divide both side by {eval4}")
                equ6 = f"{eval4}x / {eval4} = {eval5} / {eval4}\n"
                print(equ6)

                print("Finally, the answer is...")
                equ7 = f"x = " + str(eval5/eval4)
                print(equ7)
    return eval5/eval4

linear_equ_func()