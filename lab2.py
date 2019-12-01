myint = 7
print (myint)

myfloat = 7.0
print (myfloat)

mystring = "Hello"
print (mystring)

mystring = "sergo"
myfloat = 12.32
myint = 10

if mystring == "sergo":
    print("String: %s" % mystring)

if isinstance(myfloat, float) and myfloat == 12.32:
    print("Float: %f" % myfloat)

if isinstance(myint, int) and myint == 10:
    print("Integer: %d" % myint)

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

x = object()
y = object()

x_list = [x]
y_list = [y]
big_list = []

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

data = ("John", "Doe", 53.44)
format_string = "Hello"

print(format_string % data)


s = "Strings are awesome!"
print("Length of s = %d" % len(s))

print("The first occurrence of the letter a = %d" % s.index("a"))

print("a occurs %d times" % s.count("a"))

print("The first five characters are '%s'" % s[:5])
print("The next five characters are '%s'" % s[5:10])
print("The thirteenth character is '%s'" % s[12])
print("The characters with odd index are '%s'" %s[1::2])
print("The last five characters are '%s'" % s[-5:])

print("String in uppercase: %s" % s.upper())

print("String in lowercase: %s" % s.lower())

if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

print("Split the words of the string: %s" % s.split(" "))


phonebook = {  "John" : 938477566, "Jack" : 938377264, "Jill" : 947662781 }

phonebook["Jake"] = 938273443
del phonebook["Jill"]

if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")