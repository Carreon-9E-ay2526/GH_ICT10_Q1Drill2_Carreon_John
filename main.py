#Working with Numbers
from pyscript import display, document


#def greet_them(e):
    #usename = document.getElementById('inputone').value
    #display(f'Hello {usename}!', target='result')

def addingnums(e):
    document.getElementById('result').innerHTML = " "
    number1 = float(document.getElementById('num1').value)
    number2 = float(document.getElementById('num2').value)
    sum = number1 + number2

    display(f'The sum of {number1} and {number2} is {sum}', target='result')

def subingnums(e):
    document.getElementById('result').innerHTML = " "
    number1 = float(document.getElementById('num1').value)
    number2 = float(document.getElementById('num2').value)
    difference = number1 - number2

    display(f'The difference of {number1} and {number2} is {difference}', target='result')

def multiplicationnums(e):
    document.getElementById('result').innerHTML = " "
    number1 = float(document.getElementById('num1').value)
    number2 = float(document.getElementById('num2').value)
    multiplication = number1 * number2

    display(f'The difference of {number1} and {number2} is {multiplication}', target='result')

def Exponums(e):
    document.getElementById('result').innerHTML = " "
    number1 = float(document.getElementById('num1').value)
    number2 = float(document.getElementById('num2').value)
    Expo = number1 ** number2

    display(f'The difference of {number1} and {number2} is {Expo}', target='result')

def floatdivnums(e):
    document.getElementById('result').innerHTML = " "
    number1 = float(document.getElementById('num1').value)
    number2 = float(document.getElementById('num2').value)
    Floatdiv = number1 / number2

    display(f'The difference of {number1} and {number2} is {Floatdiv}', target='result')

def floordivnums(e):
    document.getElementById('result').innerHTML = " "
    number1 = float(document.getElementById('num1').value)
    number2 = float(document.getElementById('num2').value)
    Floordiv = number1 // number2

    display(f'The difference of {number1} and {number2} is {Floordiv}', target='result')

def modulonums(e):
    document.getElementById('result').innerHTML = " "
    number1 = float(document.getElementById('num1').value)
    number2 = float(document.getElementById('num2').value)
    Modulo = number1 % number2

    display(f'The difference of {number1} and {number2} is {Modulo}', target='result')