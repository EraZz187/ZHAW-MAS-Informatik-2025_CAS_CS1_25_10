a, b = 'one', 'two'
print("outer a,b =", a, b)


def function():
    # a, b = 1, 2
    a = 1
    print("inner a,b=", a, b)


function()
print("outer a,b=", a, b)