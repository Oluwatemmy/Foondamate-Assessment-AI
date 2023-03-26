<a name="readme-top"></a>

<!-- Project Shields -->
<div align="center">

  [![Contributors][contributors-shield]][contributors-url]
  [![Forks][forks-shield]][forks-url]
  [![Stargazers][stars-shield]][stars-url]
  [![Issues][issues-shield]][issues-url]
  [![MIT License][license-shield]][license-url]
  [![Twitter][twitter-shield]][twitter-url]
</div>

<!-- Project Name -->
<div align="center">
  <h1>Foondamate Coding Challenge</h1>
</div>

<div>
  <p align="center">
    <a href="https://github.com/Oluwatemmy/Foondamate-Coding-Challenge#readme"><strong>Explore the Documentation »</strong></a>
    <br />
    <a href="https://github.com/Oluwatemmy/Foondamate-Coding-Challenge/issues">Report Bug</a>
    ·
    <a href="https://github.com/Oluwatemmy/Foondamate-Coding-Challenge/issues">Request Feature</a>
  </p>
</div>


<!-- About the Project -->
## Foondamate Coding Challenge

This is a Command Line (CLI) application that solves equations in a given format. Example:

* 7x - 2 = 21
* 2(4x + 3) + 6 = 24 - 4x

Users can use this application to solve mathematical equations. And more functionality will be added to help solve more math's problems.

The CLI application solves the equation in the given format above and return all the solutions required in solving the equation.

Enjoy! 😊😊✌️✌️

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Installation -->
## Usage

To explore and run the code locally, follow these steps:

1. Clone this Foondamate Coding Challenge repository

2. Then you have full access to the repository which include the tests' folder, equation_solver.py and the run_app.py files alongside the README file, License and the .gitattributes file.

3.  Head over to the run_app.py file to check the code and that is the file that runs the application

4. Open up your terminal and run this command:
  ``` console
python run_app.py
```

5. Then you should see a result asking you to input the equation just like this:
  ```console
Enter your linear equation in the format : 'ax - b = c' or 'a(bx + c) + d = e - fx' where a, b, c, d, e and f are integers or decimals. 
```

6. Input the equation you would like the application to run. Let's try `7x - 2 = 21`

7. Then you will get the following result:
```console
Enter your linear equation in the format : 'ax - b = c' or 'a(bx + c) + d = e - fx' where a, b, c, d, e and f are integers or decimals.
7x - 2 = 21
Original equation: 7x - 2 = 21 

Add 2.00 to both sides:

7.00x - 2.00 + 2.00 = 21.00 + 2.00

Simplify the equation

7.00x = 23.00

Dividing both sides by 7.0:

7.00x / 7.00 = 23.00 / 7.00

The answer is...
x = 3.29 
```

8. Let's try it with the other equation format `2(4x + 3) + 6 = 24 - 4x`

9. The result will be:
  ```console
Enter your linear equation in the format : 'ax - b = c' or 'a(bx + c) + d = e - fx' where a, b, c, d, e and f are integers or decimals.
2(4x + 3) + 6 = 24 - 4x
First, expand the bracket...
(4.0x * 2.0) + (3.0 * 2.0) + 6.0 = 24.0 - 4.0x

Simplify the equation...
8.0x + 6.0 + 6.0 = 24.0 - 4.0x

Further simplify the equation...
8.0x + 12.0 = 24.0 - 4.0x

Move like terms to same side...
8.0x + 4.0x = 24.0 - 12.0

Further simplify the equation...
12.0x = 12.0

Divide both side by 12.0
12.0x / 12.0 = 12.0 / 12.0

Finally, the answer is...
x = 1.0 
```

10. All set. You can check out the functions that solves those equations in the `equation_solver.py` file.

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Tests -->
## Tests

You can check out the `tests`folder to check how to test the functions extensively 

To test them, follow this steps:

1. In your terminal, you need to install the `pytest` module and to do so, DO this:
  ```console
pip install pytest 
```

2. After a successful installation, check the `test_function.py` file to see all the codes and the equations used in these tests

3. run this command in your terminal 
  ```console
pytest 
```

4. The test should begin, and you should get a message that returns the test summary info telling you all the tests were passed.

5. You can edit the equations to use for the test and if it is an invalid equation, some of the tests will fail.

Enjoy!!!!

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Contact -->
## Contact

You can contact me with my social media handles:

[LinkedIn](https://www.linkedin.com/in/oluwatemmy15) | [Twitter](https://twitter.com/Oluwatemmy15) | [Github](https://github.com/Oluwatemmy) | Email: oluwaseyitemitope456@gmail.com


<p align="right"><a href="#readme-top">back to top</a></p>







<!-- Markdown Links & Images -->
[contributors-shield]: https://img.shields.io/github/contributors/Oluwatemmy/Foondamate-Coding-Challenge.svg?style=for-the-badge
[contributors-url]: https://github.com/Oluwatemmy/Foondamate-Coding-Challenge/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Oluwatemmy/Foondamate-Coding-Challenge.svg?style=for-the-badge
[forks-url]: https://github.com/Oluwatemmy/Foondamate-Coding-Challenge/network/members
[stars-shield]: https://img.shields.io/github/stars/Oluwatemmy/Foondamate-Coding-Challenge.svg?style=for-the-badge
[stars-url]: https://github.com/Oluwatemmy/Foondamate-Coding-Challenge/stargazers
[issues-shield]: https://img.shields.io/github/issues/Oluwatemmy/Foondamate-Coding-Challenge.svg?style=for-the-badge
[issues-url]: https://github.com/Oluwatemmy/Foondamate-Coding-Challenge/issues
[license-shield]: https://img.shields.io/github/license/Oluwatemmy/Foondamate-Coding-Challenge.svg?style=for-the-badge
[license-url]: https://github.com/Oluwatemmy/Foondamate-Coding-Challenge/blob/main/LICENSE
[twitter-shield]: https://img.shields.io/badge/-@Oluwatemmy15-1ca0f1?style=for-the-badge&logo=twitter&logoColor=white&link=https://twitter.com/Oluwatemmy15
[twitter-url]: https://twitter.com/Oluwatemmy15
[python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
