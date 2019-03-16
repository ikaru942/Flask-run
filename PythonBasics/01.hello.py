print("Hello World")

myname = input("What is your name: ")
print("Hello " + str(myname))

#Alternative way to format a string
print("Hello %s" % myname)

print(f"Hello{myname"}!")



i = 120
print(f"Variable i has the value {i}")

f = 1.6180339
print(f"Variable f has the value {f} and its type is {type(f)}")

b = true
print(f"Variable b has the value {b}")

n = None
print(f"Variable n has the value pf {n}")


#Change variable type
i = 140
print(f"Vaariable i has the value {i} and is the type {type(i)}")
i = 3.0
print(f"Variable f has the value {f} and its type is {type(i)})

x = 10
if (x > 0):
    print("The number x is positive")
elif (x < 0):
    print("The number x is negative")
else:
    print("The number x is zero")

x = 10
if (x > 0):
    pass
elif (x < 0):
    print("The number x is negative")
else:
    print("The number x is zero")


if (x == 0):
    pass

name "Chris"
print(f"\nVariable name is of type {type(name)} and has the value {name}")

c = ("John", 10, 20, 10)
print(f"\nc[0] has the value {c} and is of type {type(c)}")


#Python List
l = ["Anna", "Tom", "John", 10, 10.0]
print(f"\nThe ballue of l is {l} and its type is {type(l)}")
