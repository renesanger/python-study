def spam():
    eggs = 'spam local'
    print(eggs)

def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)

def test():
    global eggs 
    eggs= 'ggg'

eggs = 'global local'
bacon()
print(eggs)
test()
print(eggs)


