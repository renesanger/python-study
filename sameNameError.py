def spam():
    print(eggs)  # ERROR!
    eggs = 'spam local'
   
    eggs = 'global'
spam()

# This error is to show that python does not accept a fallback value if it the variable is instantiated after
