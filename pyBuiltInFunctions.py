# abs() function Returns the absolute value of a number
x = -33.5
print(abs(x))

# all() function Returns True for the given list, dictionary, set or tuple
x = [1, 33, 'aa', 'ahmad']
print(all(x))
y = (0, False, 1)
print(all(y))
z = []
print(all(z))

# bin() function Returns the binary for the given value
print(bin(14))      # The output has (0b) prefix means binary value

# bool() function Converts the given value to boolean format
t1 = []
print(bool(t1))
t2 = 0.0
print(bool(t2))
t3 = None
print(bool(t3))
t4 = True
print(bool(t4))

# callable() function Returns True when the given value is callable
print("--------------------------------")
x = 7
print(callable(x))
x = lambda : print("I'm lambda function")
print(callable(x))
x() # calling the lambda function

# compile() function Compiles the given string format code
code = "x=5\ny=15\nprint(x+y)"
com_code = compile(code, '', 'exec')
print(type(com_code))
exec(com_code)

# exec() function Executes the given large or small peice of code
print("--------------------------------")
exec('print(22==22)')
exec('print(2+8)')

# sum() function Adds all given values
li = [33,45,333,25,234,3443,4,54,4,45,4,45,45]
print(sum(li))

# any() function Returns True if any of the given value is True
print(any(['a', False, 0]))

# eval() function Runs the given expresion within our code
x = 8
print(eval('x*5/x'))

# float() function Returns the float value of the given value (if it has)
print('--------------------------------')
y = 23
print(float(y))

# format() function Returns a formatted representation of a given value
print('--------------------------------')
print(format(112, 'd')) # prints 112 on the place of 'd' d means integer digit
print(format(23.334432, 'f')) # 'f' means float
print(format(18, 'b')) # 'b' means binary

# iter() function Returns the given list or dict as iterable
print('--------------------------------')
li = [1,2,3,4,5]
listIter = iter(li)
print(next(listIter)) # prints 1
print(next(listIter)) # prints 2
print(next(listIter)) # prints 3
print(next(listIter)) # prints 4
print(next(listIter)) # prints 5

# len()
print('--------------------------------')
print(len(li))

# list()
string = 'aeiou'
print(list(string))

# object() Is the base for all classes
python = object()
print(type(python))
print(dir(python))

# id() Returns the identity of the object
s = 23
print("s id(): ", id(s))

# open() Opens the file in the given path
file = open('C:/README.txt')
content = file.read()
file.close()
print("File contents:\n", content)

