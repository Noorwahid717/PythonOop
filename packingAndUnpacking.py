# A Python program to demonstrate both packing and unpacking

# A sample python function that takes three arguments
# and orints them
def fun1 (a, b, c):
    print(a, b, c)

# Another sample function
# This is an example of packing, All arguments passed
# to fun2 are packed into tuple *args.
def fun2 (*args):

    # convert args tuple to a list so we can modify it
    args = list(args)

    # Modifying args
    args[0] = "Geeksforgeeks"
    args[1] = "awesome"

    # unpacking args and calling fun1()
    fun1(*args)

# Driver code
fun2('hello', 'beuatiful', 'wotld')
