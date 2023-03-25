import re
from app import solve_linear_equation, linear_equation_func


if __name__ == '__main__':
    # Check the equation format of the user input and return either of the two functions above or an error
    while True:
        try:
            equation_one_format = 'ax - b = c'
            equation_two_format = 'a(bx + c) + d = e - fx'
            equation = input(f"Enter your linear equation in the format : '{equation_one_format}' or '{equation_two_format}' where a, b, c, d, e and f are integers or decimals.\n")
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

            equation_parts = equation.split(" ")

            if match1 or match2:
                solve_linear_equation(equation)
                break
            
            elif equation_parts:
                linear_equation_func(equation)
                break
            else:
                raise Exception
        except Exception as e:
            print("Invalid equation format. Please enter either 'ax - b = c' or 'a(bx + c) + d = e - fx'. \n")
            break


