#!/usr/bin/python3
if __name__ == "__main__":
    import sys  # import sys module
    argv = sys.argv[1:]  # get arguments from command line
    argc = len(argv)  # get number of arguments

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))  # print number of arguments

    for i, arg in enumerate(argv, start=1):  # loop through arguments
        print("{}: {}".format(i, arg))  # print number and argument
