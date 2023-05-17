#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = list(set(my_list))  # Create a list of unique elements
    total = sum(unique_list)  # Compute the sum of unique elements
    return total
