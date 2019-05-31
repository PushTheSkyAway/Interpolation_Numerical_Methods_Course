import getopt
import sys

import matplotlib.pyplot as plt
import numpy
import pandas as pd

from cubic_spline import *
from lagrange import *


def main(argv):
    NUMBER_OF_POINTS = 15
    # Reading Data

    filename = ""

    try:
        opts, args = getopt.getopt(argv, "f:n:")
    except getopt.GetoptError:
        print("main.py -f <input_file> -n <number_of_nodes>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-f':
            filename = arg
        elif opt == '-n':
            NUMBER_OF_POINTS = int(arg)

    if filename == "":
        print("You have to specify filename!\nUsage: main.py -f <input_file> -n <number_of_nodes>")
        sys.exit(2)
    elif NUMBER_OF_POINTS < 3:
        print("You can't use less than 3 nodes.\nUsage: main.py -f <input_file> -n <number_of_nodes>")
        sys.exit(2)

    #Distance(m), Elevation(m)
    try:
        profile_data = pd.read_csv(filename, names=[
            "distance", "elevation"])
    except FileNotFoundError:
        print("File \"" + filename + "\" not found.")
        sys.exit(2)

    step = len(profile_data["distance"])//(NUMBER_OF_POINTS)

    interpolation_data = profile_data[::step]

    ##LAGRANGE###########################################################################

    fi_functions = []

    for x in interpolation_data["distance"]:
        fi_functions.append(make_fi_function(
            x, interpolation_data["distance"]))

    itrpl_func = lagrange_interpolation(
        fi_functions, interpolation_data["elevation"])

    interpolation_y = []

    for x in profile_data["distance"]:
        interpolation_y.append(itrpl_func(x))

    # plotting
    f = plt.figure(1)
    plt.plot(profile_data["distance"], profile_data["elevation"])
    plt.plot(profile_data["distance"], interpolation_y, 'r')
    plt.legend(["Exact function", "Interpolated function",
                "Interpolation points"])
    plt.title("Lagrange interpolation, Nodes = " +
              str(NUMBER_OF_POINTS) + ", Location = " + str(filename[:-4]))
    plt.xlabel("Distance [m]")
    plt.ylabel("Elevation [m]")
    f.show()

    #####################################################################################

    ##SPLINES############################################################################

    CubicSplineInterpolation.calc_coeffs(np.array(
        interpolation_data["distance"]), np.array(interpolation_data["elevation"]))

    spline_interpolation_y = []

    for x in profile_data["distance"]:
        spline_interpolation_y.append(CubicSplineInterpolation.interpolate(x))

    # plotting
    g = plt.figure(2)
    plt.plot(profile_data["distance"], profile_data["elevation"])
    plt.plot(profile_data["distance"], spline_interpolation_y, 'r')
    plt.legend(["Exact function", "Interpolated function",
                "Interpolation points"])
    plt.title("Cubic spline interpolation, Nodes = " +
              str(NUMBER_OF_POINTS)+", Location = " + str(filename[:-4]))
    plt.xlabel("Distance [m]")
    plt.ylabel("Elevation [m]")
    g.show()

    ######################################################################################

    input()


if __name__ == "__main__":
    main(sys.argv[1:])
