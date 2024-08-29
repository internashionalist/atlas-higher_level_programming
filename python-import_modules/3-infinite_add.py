#!/usr/bin/python3

if __name__ == "__main__":
    import sys  # import sys module

    total = 0  # initialize total to 0
    for arg in sys.argv[1:]:  # skip script name
        total += int(arg)  # add argument to total

    print(total)  # print total
