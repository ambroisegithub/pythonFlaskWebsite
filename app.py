# Define a function
# def greet(name):
#     """This function greets the person passed as an argument."""
#     print("Hello, " + name + "!")

# Call the function
# g     # Output: Hello, Bob!

# Function with return statement
# def add_numbers(a, b):
#     """This function adds two numbers and returns the result."""
#     result = a + b
#     return result

# Call the function and store the result in a variable
# sum = add_numbers(3, 5)
# print("Sum:", sum)  # Output: Sum: 8

# Function with default argument
# def greet_with_default(name, greeting="Hello"):
#     """This function greets a person with a custom greeting."""
#     print(greeting + ", " + name + "!")

# Call the function with and without providing a custom greeting
# greet_with_default("Alice")                 # Output: Hello, Alice!
# greet_with_default("Bob", "Hi")             # Output: Hi, Bob!

# def Addnumbers(num1, num2):
#     result = num1 + num2
#     return result
# sum = Addnumbers(10, 40)
# print("the sum of two number is", sum)

# condition statement in python

# age = 10

# if age < 18:
#  print("You are young person")
# else:
#     print("you are adult")
 
 
# gender = "male"
# if gender == "male": 
#     print("you are male")
# else:
#     print("you are women") 

#to display the people which allowed to vote is male who are above 18 years old

# age = 10
# gender = "female"

# if(age >= 21 and gender == "male"):
#     print("you are adult who allowed to vote")
# else:
#     print("you are not allowed to vote becouse you are not adult and male")

# if age >= 18:
#      if gender == "male":
#         print("you are adult means you are allowed to vote")
#      else:
#          print("you are not allowed to vote becouse you are not male and vote")
# else:
#          print("you are not allowed to vote yet")           
# list and tupple in python
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route("/about")
def about():
   return render_template('about.html')
 
if __name__ == '__main__':
    app.run(debug=True)
 