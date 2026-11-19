def spam(divide_by):
    try:
        # Any code in this bloxk that causes ZeroDivisionError won't crash the progra,
        return 42 / divide_by
    except:
        # If ZeroDivisionError happened, the code in this block runs:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
