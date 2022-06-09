#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = a_dictionary.copy()

    for i in sorted(new_dict):
        print(f"{i}: {new_dict[i]}")
