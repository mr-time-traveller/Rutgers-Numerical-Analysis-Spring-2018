def get_coeff(f, x):
    """
    Solves for the coefficients in a Netwon polynomial using divided
    differences
    Input:
    f - the value of the function evaluated in x
    x - the corresponding x values                                                                    
    Output:
    a - a list of the coefficients ordered like this [a0,a1...aN]
    """
    # Find the looping index
    n = len(x) - 1
    # Initially copy all the f values to a
    a = f.copy()

    for i in range( 1, n + 1 ):
        for j in range( n, i - 1 , -1 ):
            # Notice that a[j] uses a[j]. This is no problem as
            # initially a[j] is equal to f
            a[j] = (a[j] - a[j-1]) / (x[j] - x[j-i])

    return a