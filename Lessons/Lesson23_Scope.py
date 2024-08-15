# scope = the region that a variable is recognized
#         A variable is only available from inside the region its created.
#         A global and locally scoped versions of a variable can be created

# L E G B = Local Enclosing Global Built-in

name = 'htet' # global scope (available inside & outside function)

def displayName():
    name = 'moe' # local scope (available only inside the function)
    print(name)

displayName()
print(name)

