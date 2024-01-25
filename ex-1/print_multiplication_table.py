def multiplication_table(n):
    if n == 0 or  not (isinstance(n, (int,float))):
        print(ValueError("Input 'n' should be a integer."))
        return
        
    for i in range(1, 11 ):
        print(f"{i} x {n} = {i * n}\t")
multiplication_table('a')