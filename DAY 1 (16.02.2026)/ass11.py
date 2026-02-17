def analyze_function(func): 
    print("Type:", type(func))
      
    print("\nFirst 10 attributes from dir():")
    print(dir(func)[:10]) 
    print("\nHelp output:")
    help(func) 


def my_function(x): 
    return x * x


analyze_function(my_function)
analyze_function(str.upper)
