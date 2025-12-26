"""Write a function which receives 4 digits and returns the latest time of day that can be built with those digits.

The time should be in HH:MM format.

Examples:

1, 9, 8, 3 => "19:38"

9, 1, 2, 5 => "21:59" ("19:25" is also a valid time, but 21:59 is later)`

Notes

Result should be a valid 24-hour time, between 00:00 and 23:59.
Only inputs which have valid answers are tested."""

# Abstraction
# Algorithm
# Inputs must be positive ints between 0 and 9
# The length of list of numbers must be 4

# Calculating the time
# First digit must be either 0,1 or 2 before the colon
# Preference of 2 over 1 and 1 over 0, unless it's 00
# The second two digits after the colon must be in range(1,60)
# The larger the number the more preferred
# a for loop for the first half of the time
# A for loop for the second half of the time3

# How to sort first half of the time
# variable a
# variable b
# Loop through the list, .pop() if 0, if no 0, then 2 if no 2 then 1 - assign to variable A
# Then find the max in the remaining list and assign it to variable b
# Only two numbers are left. Convert them into integers.
# Assign max to var d and remaining to variable e
# make it d+e. If outside of range(1,60) then swap it around to be e+d.

import datetime


def latest_time_compiler(numbers: list[str]) -> str:
    a, b, c, d, = "", "", "", ""
    for i in range(len(numbers)+1):
        for num in numbers:
            print(num, i)


latest_time_compiler(["0", "0", "0", "0"])
# lst = ["0", "2", "5", "7"]
# # test1 = lst.pop(2)
# # test2 = lst.remove("0")
# # print(lst)
# # print(test1)
# # print(test2)
# for n in lst:
#     print(n)
#     print(lst.index(n))
