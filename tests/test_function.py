import unittest
from equation_solver import solve_linear_equation, linear_equation_func


class SolveLinearEquationTests(unittest.TestCase):

    def test_positive_linear_equation(self):
        # Test a positive equation
        equation = "2x + 3 = 7"
        expected_steps = [
            "Original equation: 2x + 3 = 7 \n",
            "Subtract 3.00 from both sides:\n",
            "2.00x + 3.00 - 3.00 = 7.00 - 3.00\n",
            "Simplify the equation \n",
            "2.00x = 4.00\n",
            "Dividing both sides by 2.0:\n",
            "2.00x / 2.00 = 4.00 / 2.00 \n",
            "The answer is...",
            "x = 2.00"
        ]
        self.assertEqual(solve_linear_equation(equation), 2)

    def test_negative_linear_equation(self):
        # Test an equation with no constant term
        equation = "3x - 2 = 7"
        expected_steps = [
            "Original equation: 3x - 2 = 7 \n",
            "Add 2.00 to both sides:\n",
            "3.00x - 2.00 + 2.00 = 7.00 + 2.00\n",
            "Simplify the equation \n",
            "3.00x = 9.00\n",
            "Dividing both sides by 3.0:\n",
            "3.00x / 3.00 = 9.00 / 3.00 \n",
            "The answer is...",
            "x = 3.00"
        ]
        self.assertEqual(solve_linear_equation(equation), 3)

    def test_decimals_linear_equation(self):
        # Test an equation with decimals
        equation = "2.5x + 3.5 = 7.5"
        expected_steps = [
            "Original equation: 2.5x + 3.5 = 7.5 \n",
            "Subtract 3.50 from both sides:\n",
            "2.50x + 3.50 - 3.50 = 7.50 - 3.50\n",
            "Simplify the equation \n",
            "2.50x = 4.00\n",
            "Dividing both sides by 2.5:\n",
            "2.50x / 2.50 = 4.00 / 2.50 \n",
            "The answer is...",
            "x = 1.60"
        ]
        self.assertEqual(solve_linear_equation(equation), 1.6)

    def test_negative_decimals_linear_equation(self):
        # Test an equation with decimals
        equation = "2.5x - 3.5 = 7.5"
        expected_steps = [
            "Original equation: 2.5x - 3.5 = 7.5 \n",
            "Add 3.50 to both sides:\n",
            "2.50x - 3.50 + 3.50 = 7.50 + 3.50\n",
            "Simplify the equation \n",
            "2.50x = 11.00\n",
            "Dividing both sides by 2.5:\n",
            "2.50x / 2.50 = 11.00 / 2.50 \n",
            "The answer is...",
            "x = 4.40"
        ]
        self.assertEqual(solve_linear_equation(equation), 4.4)

    def test_negative_coefficients_linear_equation(self):
        # Test an equation with negative coefficients
        equation = "-2x - 3 = 7"
        expected_steps = [
            "Original equation: -2x - 3 = 7 \n",
            "Add 3.00 to both sides:\n",
            "-2.00x - 3.00 + 3.00 = 7.00 + 3.00\n",
            "Simplify the equation \n",
            "-2.00x = 10.00\n",
            "Dividing both sides by -2.0:\n",
            "-2.00x / -2.00 = 10.00 / -2.00 \n",
            "The answer is...",
            "x = -5.00"
        ]
        self.assertEqual(solve_linear_equation(equation), -5)

    def test_invalid_input(self):
        # Test an invalid input that should raise an error
        equation = "2x + = 10"
        with self.assertRaises(Exception):
            solve_linear_equation(equation)
    

class LinearEquationFuncTest(unittest.TestCase):
    
    def test_valid_linear_equation_func(self):
        # Test a valid equation
        equation = "2(4x + 3) + 6 = 24 - 4x"
        expected_steps = [
            "First, expand the bracket... ",
            "(4.0x * 2.0) + (3.0 * 2.0) + 6.0 = 24.0 - 4.0x \n",
            "Simplify the equation...",
            "8.0x + 6.0 + 6.0 = 24.0 - 4.0x \n",
            "Further simplify the equation...",
            "8.0x + 12.0 = 24.0 - 4.0x \n",
            "Move like terms to same side...",
            "8.0x + 4.0x = 24.0 - 12.0 \n",
            "Further simplify the equation... ",
            "12.0x = 12.0 \n",
            "Divide both side by 12.0 ",
            "12.0x / 12.0 = 12.0 / 12.0 \n",
            "Finally, the answer is...",
            "x = 1.00"
        ]
        assert linear_equation_func(equation) == "x = 1.0"

    def test_invalid_linear_equation_func_2(self):
        # Test invalid equation
        equation = "2(3x + 5) +  = 8 - 4x"
        assert linear_equation_func(equation) == None

    def test_valid_linear_decimal_equation_func(self):
        # Test decimal equation
        equation = "2(4.5x + 3.5) + 6.5 = 24.5 - 4.5x"
        expected_steps = [
            "First, expand the bracket... ",
            "(4.5x * 2.0) + (3.5 * 2.0) + 6.5 = 24.5 - 4.5x \n",
            "Simplify the equation...",
            "9.0x + 7.0 + 6.5 = 24.5 - 4.5x \n",
            "Further simplify the equation...",
            "9.0x + 13.5 = 24.5 - 4.5x \n",
            "Move like terms to same side...",
            "9.0x + 4.5x = 24.5 - 13.5 \n",
            "Further simplify the equation... ",
            "13.5x = 11.0 \n",
            "Divide both side by 13.5 ",
            "13.5x / 13.5 = 11.0 / 13.5 \n",
            "Finally, the answer is...",
            "x = 0.8148148148148148"
        ]
        assert linear_equation_func(equation) == "x = 0.8148148148148148"

    def test_valid_linear_negative_equation_func(self):
        # Test valid negative equation func
        equation = "2(4x - 3) + 6 = 24 - 4x"
        expected_steps = [
            "First, expand the bracket... ",
            "(4.0x * 2.0) + (-3.0 * 2.0) + 6.0 = 24.0 - 4.0x \n",
            "Simplify the equation...",
            "8.0x - 6.0 + 6.0 = 24.0 - 4.0x \n",
            "Further simplify the equation...",
            "8.0x - 0.0 = 24.0 - 4.0x \n",
            "Move like terms to same side...",
            "8.0x + 4.0x = 24.0 - 0.0 \n",
            "Further simplify the equation... ",
            "12.0x = 24.0 \n",
            "Divide both side by 12.0 ",
            "12.0x / 12.0 = 24.0 / 12.0 \n",
            "Finally, the answer is...",
            "x = 2.00"
        ]
        assert linear_equation_func(equation) == "x = 2.0"
