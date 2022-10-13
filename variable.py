#create variable

#first you have to create variable and assign to it

a = "a"

# do not need to be declared with any particular type.
# it can even change type after they have been set.

#if you want to specify the data type of a variable , this can be done with  casting.

#casting----
x = str(3)
y = int(3)
z = float(3)



#you can get the data type of a variable with the type() function

print(type(x))
print(type(y))
print(type(z))
print("---------------------------------------\n")



#assign multiiple value to many variable

ab, ac, ae = "bangladesh", "pakistan", "nepal"
print("ab value is " + ab)
print("ac value is " + ac)
print("ae value is " + ae)
print("---------------------------------------\n")

# one value to multiple variable

x = y = z = "banladesh"
print("x value is " + x)
print("y value is " + y)
print("z value is " + z)
print("---------------------------------------\n")

# If you have a collection of values in a list, tuple etc.
# Python allows you to extract the values into variables.
# This is called unpacking.

countryName = ["bangldesh", "china", "united states", "united kingdom"]
a, b, c, d = countryName
print("a value is " + a)
print("b value is " + b)
print("c value is " + c)
print("d value is " + d)
print("---------------------------------------\n")
#in the print() function , you output multiple variable separated by comma.
#comma will be treat as space

print(a, b, c, d)
# the best way to output in different data type one print() funtion by using comma
print("---------------------------------------\n")


# variable are two type --
# 1. local variable (funtion variable)
# 2. global variable. (outside a funtion)

#global varible--
x = "hello world"
print(x)
print("---------------------------------------\n")

#local variable

def func():
    x = "python code is short"
    print(x)
func()
print("------------------------------------------\n")

#global keyword
name = "jakaria mahmud"
def func1():
    global name
    name = "sakil ahmed"

func1()
print(name)
print("---------------------------------------\n")

