#this is a function in replit that clears the entries
from replit import clear
#import the ascii calculator logo from the art module 
from art import logo

#create an addition function
def add(n1, n2):
    """This returns the sum of two numbers"""
    return (n1 + n2)

#create a substraction function

def sub(n1, n2):
    """This returns the result from the subtraction of two numbers"""
    return (n1 - n2)

#create a multiplication function

def multiply(n1, n2):
    """This returns the result from the multiplication of two numbers"""
    return (n1 * n2)

#create a division function

def divide(n1, n2):
    """This returns the result from the division of two numbers"""
    return (n1 / n2)

#craete a dictionary of the operators sign and the function name which will be used to show users the symbols and carry out the calculation operation.
operation = {"+": add, "-": sub, "*": multiply, "/": divide}


#create a function which will be used in recursion and calling back
def calculator():
    """
        This function takes input of numbers and operation sign from users and
        display the result depending on the operator selected.
    """
  print(logo)
  num1 = float(input('what is the first number'))
  for signs in operation:
      print(signs)
  #this variable is used for running the while loop 
  end_of_calc = False
  
  
  #the loop stops when this condition is not met   
  while end_of_calc != True:
    operation_sign = input('pick an operation from the line above')

    num2 = float(input('what is the second number'))
    #the if statement checks to make sure the operator selected is correct
    if operation_sign not in operation:
        print('invalid input')
    else:
        #if correct operator is selected
        #this variable calculate stores the value in the operation dictionary with key operation sign depending on the user input
        calculate = operation[operation_sign]
        
        #the calculate depending on input can either be add, sub, multipy and divide which can now be used to return the solution to answer
        #this can be done in so many ways but through this way, we can use fewer lines of code.
        answer = calculate(num1, num2)
        print(f"The answer for {num1} {operation_sign} {num2} is {answer}")
        #to determine if the calculation should continue or not
        next_input =input(
                f'Type "y" to continue calculating with {answer} or type "n" to end calculation.'
            )
        #conditional statement to determine if the loop ends or contiues depending on the next_input input
        if next_input == 'y':
            end_of_calc = False
            num1=answer
        elif next_input == 'n':
            end_of_calc = True
            #this clears the page

            clear()
            #this recalls  the function again
            calculator()
          
calculator()