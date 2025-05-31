def compare_to_five(y):
    if y > 5:
        return "Greater"
    elif y < 0:
        return "Negative"
    elif y < 5:
        return "Less"
    else:
        return "Equal"
print(compare_to_five(10))
print(compare_to_five(3))
print(compare_to_five(5))
print(compare_to_five(-2))
print(compare_to_five(0))
def compare_to_five(y):
    if y > 5:
        return "Greater"
    elif y < 5:
        return "Less"
    elif y < 0:
        return "Negative"
    else:
        return "Equal"
print(compare_to_five(-2))
# Create the following piece of code: If x > 200, print out "Big"; If x > 100 and x <= 200, print out "Average"; and If x <= 100, print out "Small". Use the if, elif, and else keywords in your code.
def compare_to_x(x):
    if x > 200:
        return "Big"
    elif x > 100 and x <= 200:
        return "Average"
    else:
        return "Small"
print(compare_to_x(250))
print(compare_to_x(150))
print(compare_to_x(50))