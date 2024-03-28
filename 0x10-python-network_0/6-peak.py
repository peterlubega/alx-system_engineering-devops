#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""

    # Check if the list is empty
    if list_of_integers == []:
        return None

    # If the list has only one or two elements, return the maximum value
    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    # Find the middle index
    mid = int(size / 2)
    # Get the value of the middle element
    peak = list_of_integers[mid]

    # Check if the middle element is a peak
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    # If middle element is less than left adjacent element, search left half
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    # If middle element is less than right adjacent element, search right half
    else:
        return find_peak(list_of_integers[mid + 1:])
