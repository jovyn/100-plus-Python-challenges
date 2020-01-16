# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class MyClass:
  def get_String(self):
    mystr = input("Enter a string here: ")
    return mystr

  def print_String(self,some_str):
    print(f"String to print is : {some_str}")

x1 = MyClass()
x_str = str(x1.get_String())
x1.print_String(x_str.upper())