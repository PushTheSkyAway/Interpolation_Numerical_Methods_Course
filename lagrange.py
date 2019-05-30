
def lagrange_interpolation(fi_functions, datay):
    """ Makes LaGrange interpolation of data
    Args:
        fi_functions (func[]): list of fi functions for each x
        datay (float[]): list of interpolation y's
 
    Returns:
        function: function that interpolates data
    """
    def interpolation_func(x):
        result = 0
        index = 0
        for y in datay:
            result = result + y*fi_functions[index](x)
            index = index+1

        return result

    return interpolation_func



def make_fi_function(x0, data):
    """Generates fi function for LaGrange
    Args:
        x0 (float): x for which function will be generated
        data (float[]): All x's
    """
    def fi(x):
        result = 1
        for xi in data:
            if xi!=x0:
                result = result*(x-xi)/(x0-xi)
        return result

    return fi
