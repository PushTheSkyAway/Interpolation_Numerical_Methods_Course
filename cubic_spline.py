import numpy as np


class CubicSplineInterpolation():

    __H = 2
    __coeffs = np.array([])
    __x = []
    __y = []

    @staticmethod
    def set_spline_step(step):
        __H = step

    @staticmethod
    def __gen_system_of_equations(x, y):
        n = len(x)-1
        size = 4*n
        h = CubicSplineInterpolation.__H

        system = np.zeros((size, size))
        b = np.zeros((size, 1))

        eq_nr = 0

        #a0 = f(x0)
        system[eq_nr][0] = 1
        b[eq_nr][0] = y[0]
        eq_nr = eq_nr+1

        # a0 + b0h + c0h^2 + d0h^3 = f(x1)
        system[eq_nr][0] = 1
        system[eq_nr][1] = h
        system[eq_nr][2] = h**2
        system[eq_nr][3] = h**3
        b[eq_nr][0] = y[1]
        eq_nr = eq_nr+1

        for i in range(0, n-1):
           
            #a1 = f(x1)
            system[eq_nr][4*i+4] = 1
            b[eq_nr][0] = y[i+1]
            eq_nr = eq_nr+1

            # a1 + b1h + c1h^2 + d1h^3 = f(x2)
            system[eq_nr][4*i+4] = 1
            system[eq_nr][4*i+5] = h
            system[eq_nr][4*i+6] = h**2
            system[eq_nr][4*i+7] = h**3
            b[eq_nr][0] = y[i+2]
            eq_nr = eq_nr+1

            # b0 + 2c0h + 3d0h^2 - b1 = 0
            system[eq_nr][4*i+1] = 1
            system[eq_nr][4*i+2] = 2*h**1
            system[eq_nr][4*i+3] = 3*h**2
            system[eq_nr][4*i+5] = -1
            eq_nr = eq_nr+1

            # 2c0 + 6d0h - 2c1 = 0
            system[eq_nr][4*i+2] = 2
            system[eq_nr][4*i+3] = 6*h
            system[eq_nr][4*i+6] = -2
            eq_nr = eq_nr+1

        # Derivatives at edges
        #c0 = 0
        system[eq_nr][2] = 1
        eq_nr = eq_nr + 1

        # 2cn + 6dnh = 0
        system[eq_nr][-1] = 6*h
        system[eq_nr][-2] = 2
        eq_nr = eq_nr + 1

        return system, b

    @staticmethod
    def calc_coeffs(knots_x, knots_y):
        #Mx = b
        M, b = CubicSplineInterpolation.__gen_system_of_equations(
            knots_x, knots_y)

        CubicSplineInterpolation.__coeffs = np.linalg.solve(M, b)

        CubicSplineInterpolation.__x = knots_x
        CubicSplineInterpolation.__y = knots_y
        
        

    @staticmethod
    def interpolate(x):
        _x = CubicSplineInterpolation.__x
        _y = CubicSplineInterpolation.__y
        _coeffs = CubicSplineInterpolation.__coeffs
        
        for i in range(0, len(_x)-1):
            if _x[i] <= x <= _x[i+1]:
                result = _y[i]
                for j in range(0, 4):
                    result = result + _coeffs[4*i+j]*(x-_x[i])**j
                    
                
                return result

