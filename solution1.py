# Write code for algorithm 1 below

def count_down(num):
    # base case
    if num == 0:
        return num
    # recursive case
    else:
        print(num)
        count_down(num-1)

whatever = 1
count_down(whatever)