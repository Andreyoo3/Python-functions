# Defining
def functionname(parameters):
    """function_docstring"""
    function_suite
    return [expression]


# Arguments of functions
def print_required_and_keyword(str):
    """This prints a passed string into this function"""
    print (str)
    return


def print_default(name, age=35):
    """This prints a passed info into this function"""
    print ("Name: ", name)
    print ("Age ", age)
    return


def print_variable(arg1, *vartuple):
    """This prints a variable passed arguments"""
    print ("Output is: ")
    print (arg1)
    for var in vartuple:
        print (var)
    return


# Required arguments
print ("\nRequired arguments:")
# print_required_and_keyword()
print_required_and_keyword('foo')


# Keyword arguments
print ("\nKeyword arguments:")
print_required_and_keyword(str="baz")


# Default arguments
print ("\nDefault arguments:")
print_default(age=50, name="miki")
print_default(name="miki")


# Variable-length arguments
print ("\nVariable-length arguments:")
print_variable(10)
print_variable(70, 60, 50)


# Pass by reference vs value
print ("\nPass by reference vs value:")


def appendItem(some_list, item):
    some_list.append(item)  # Modifies the list in a way visible to the caller


def replaceItems(some_list, newcontentlist):
    del some_list[:]  # Modification visible to the caller
    some_list.extend(newcontentlist)  # Modification visible to the caller
    some_list = [5,
                 6]  # No outside effect; lets the local list point to a new list object,
    # losing the reference to the list object passed as an argument


def clearSet(some_set):
    some_set.clear()


def tryToTouchAnInteger(some_int):
    some_int += 1  # No outside effect; lets the local int to point to a new int object,
    # losing the reference to the int object passed as an argument
    print ("int inside:", some_int)  # 4 if int was 3 on function entry


some_list = [1, 2]
appendItem(some_list, 3)
print (some_list)  # [1, 2, 3]

replaceItems(some_list, [3, 4])
print (some_list)  # [3, 4]

some_set = set([1, 2])
clearSet(some_set)
print (some_set)  # set([])

some_int = 3
tryToTouchAnInteger(some_int)
print ("int outside:", some_int)  # 3


# Prevent argument change
print ("\nPrevent argument change:")


def evilGetLength(some_list):
    length = len(some_list)
    del some_list[:]  # Muhaha: clear the list
    return length


some_list = [1, 2]
print (evilGetLength(some_list))  # list gets cleared
print (some_list)
some_list = [1, 2]
print (evilGetLength(some_list[:]))  # Pass a copy of the list
print (some_list)


# Closures
print ("\nClosures:")


def generate_power_func(n):
    print ("id(n): %X" % id(n))

    def nth_power(x):
        return x ** n

    print ("id(nth_power): %X" % id(nth_power))
    return nth_power


raised_to_4 = generate_power_func(4)
del (generate_power_func)
print (raised_to_4(2))
print (repr(raised_to_4))
print (raised_to_4.__closure__)


# Lambda expressions
print ("\nLambda expressions:")
print (sorted([[3, 4], [3, 5], [1, 2], [7, 3]], key=lambda x: x[1]))


def attribution(name):
    return lambda x: x + ' -- ' + name


pp = attribution('John')
print (pp('Dinner is in the fridge'))


# Tips & Tricks
print ("\nTips & Tricks")


def function(item, stuff=[]):
    stuff.append(item)
    print (stuff)


function(1)
function(2)


def function(item, stuff=None):
    if stuff is None:
        stuff = []
    stuff.append(item)
    print (stuff)


function(1)
function(2)