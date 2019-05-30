import numpy as np


class CubicSplineInterpolation():
    
    __H = 1

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

        for i in range(0, n):
           #TODO wszystko
           pass
        
        

    @staticmethod
    def interpolate(knots_x, knots_y):
        CubicSplineInterpolation.__gen_system_of_equations(knots_x,knots_y)



CubicSplineInterpolation.interpolate([1,3,5],[6,-2,4])