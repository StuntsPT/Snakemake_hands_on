#!/usr/bin/env python3
from sys import argv


def parse_modeltest(modeltest_oufile):
    """
    Parses a modeltest outfile and returns the
    RAxML model
    """
    with open(modeltest_oufile, "r") as mtof:
        mt_data = mtof.readlines()
        model = mt_data[-4].split()[-1]

    return model


if __name__ == "__main__":
    my_file = argv[1]
    my_model = parse_modeltest(my_file)
    print(my_model)
