# Comman exceptions:
# 1. ZeroDevisionError: no is devided by zero.
# 2. NameError: name not found.
# 3. IdentationError: increment identation is given.
# 4. IOError: input/output operation fails.
# 5. EOFError: end of file reached, and yet operations are being performed.

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = a/b
    print("a/b = %d"%c)
except:     # We can ignore the Exception in 'except' block.
    print("Can't devide by zero!")
else:       # Executed when their isn't any error.
    print("Hi I'm else block")

print("-----------------------------")

try:
    fileptr = open('README.txt')
except:
    print("File not found!")
else:
    print('Done, successfully')
    fileptr.close()

# Multiple errors:
try:
    a = 10/0
except (ArithmeticError, IOError):
    print("Arithmetic Exception")
else:
    print("Successfully Done!")
    
# finally statement: executed before the try statement throws an exception.
try:
    fileptr = open("file.txt", "a") 
    try:
        fileptr.write("\nHi I'm Samak Wardak!")
    finally:
        fileptr.close()
        print("File closed!")
        print("Type of fileptr: ",type(fileptr))
except:
    print("Can't open the file!")
    # File I/O modes: 
    # w (write)
    # r (read)
    # a (append)
    
# raise statement:
try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ValueError
    else:
        print("The age is valid!")
except:
    print("The age is not valid!")

# Custom Exceptions
class ErrorInCode(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)
try:
    raise ErrorInCode(2000)
except ErrorInCode as ae:
    print("Received error", ae.data)
    
