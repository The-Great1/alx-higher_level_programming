#!/usr/bin/python3
for double in range(0, 100):
    if double == 99:
        print("{0:d}".format(double))
        continue
    print("{0:02}".format(double), end=", ")
