"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk
# Create a window object
window = Tk() 
# Hide the window, hint: use the withdraw method
window.withdraw() 
# Ask the user for the first number   
first_num = float(simpledialog.askfloat("Your first number", "What is your first addend?"))
# Ask the user for the second number
second_num = float(simpledialog.askfloat("Your second number", "What is your second addend?"))
# Display the sum of the two numbers 
equals_sum = first_num+second_num
print(equals_sum)

