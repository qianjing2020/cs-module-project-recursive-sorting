def double_print(n):
    print(n)
    if n == 0:
        return    
    double_print(n-1)
    
    double_print(n-1)

double_print(3)