import numpy
import matplotlib.pyplot as plt
import pandas as pd
from lagrange import *
from cubic_spline import *


def main():
    NUMBER_OF_POINTS = 10
    # Reading Data

    #Distance(m), Elevation(m)

    #profile_data = pd.read_csv("Kushma_Balewa.csv", names=["distance","elevation"])
    #profile_data = pd.read_csv("Gran_Zebru.csv", names=["distance","elevation"])
    profile_data = pd.read_csv("Lebork.csv", names=["distance", "elevation"])
    #profile_data = pd.read_csv("Gdansk.csv", names=["distance","elevation"])

    # profile_samples = len(profile_data["distance"])

    step = len(profile_data["distance"])//(NUMBER_OF_POINTS)

    ##LAGRANGE##

    interpolation_data = profile_data[::step]

    fi_functions = []

    for x in interpolation_data["distance"]:
        fi_functions.append(make_fi_function(
            x, interpolation_data["distance"]))

    itrpl_func = lagrange_interpolation(
        fi_functions, interpolation_data["elevation"])

    interpolation_y = []

    for x in profile_data["distance"]:
        interpolation_y.append(itrpl_func(x))

    plt.plot(profile_data["distance"], profile_data["elevation"])
    plt.plot(profile_data["distance"], interpolation_y, 'r')
    #plt.plot(interpolation_data["distance"], interpolation_data["elevation"],'go')
    plt.legend(["Exact function", "Interpolated function",
                "Interpolation points"])
    plt.title("Gathered data")
    plt.xlabel("Distance [m]")
    plt.ylabel("Elevation [m]")
    plt.show()

    ##SPLINES##

    CubicSplineInterpolation.set_spline_step(2)
    


if __name__ == "__main__":
    main()
