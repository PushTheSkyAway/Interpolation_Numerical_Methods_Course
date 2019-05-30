import numpy as np


class CubicSplineInterpolation():
    
    __H = 2

    @staticmethod
    def set_spline_step(step):
        __H = step

    @staticmethod
    def __gen_system_of_equations(x, y):
        n = len(x)-1
        size = n*4
        h = CubicSplineInterpolation.__H

        system = np.zeros((size,size))
        b = np.zeros((size,1))

        eq_nr = 0


        for i in range(0, n-1):
            #a0 = f(x0)
            system[eq_nr][4*i] = 1
            b[eq_nr][0] = y[i]
            eq_nr = eq_nr+1

            #a0 + b0h + c0h^2 + d0h^3 = f(x1)
            system[eq_nr][4*i] = 1
            system[eq_nr][4*i+1] = h
            system[eq_nr][4*i+2] = h**2
            system[eq_nr][4*i+3] = h**3
            b[eq_nr][0] = y[i+1]
            eq_nr = eq_nr+1

            #a1 = f(x1)
            system[eq_nr][4*i+4] = 1
            b[eq_nr][0] = y[i+1]
            eq_nr = eq_nr+1

            #a1 + b1h + c1h^2 + d1h^3 = f(x2)
            system[eq_nr][4*i+4] = 1
            system[eq_nr][4*i+5] = h
            system[eq_nr][4*i+6] = h**2
            system[eq_nr][4*i+7] = h**3
            b[eq_nr][0] = y[i+2]
            eq_nr = eq_nr+1

            #b0 + 2c0h + 3d0h^2 - b1 = 0
            system[eq_nr][4*i+1] = 1
            system[eq_nr][4*i+2] = 2*h**1
            system[eq_nr][4*i+3] = 3*h**2
            system[eq_nr][4*i+5] = -1
            eq_nr = eq_nr+1

            #2c0 + 6d0h - 2c1 = 0
            system[eq_nr][4*i+2] = 2
            system[eq_nr][4*i+3] = 6*h
            system[eq_nr][4*i+6] = -2
            eq_nr = eq_nr+1


        #Derivatives at edges 
        #c0 = 0
        system[eq_nr][2] = 1
        eq_nr = eq_nr + 1

        #2cn + 6dnh = 0
        system[eq_nr][-1] = 6*h
        system[eq_nr][-2] = 2
        eq_nr = eq_nr + 1


        return system, b
        
        

    @staticmethod
    def interpolate(knots_x, knots_y):
        #Mx = b
        M, b = CubicSplineInterpolation.__gen_system_of_equations(knots_x,knots_y)
        coeffs = np.linalg.solve(M,b)
        print(coeffs)



CubicSplineInterpolation.interpolate([1,3,5],[6,-2,4])