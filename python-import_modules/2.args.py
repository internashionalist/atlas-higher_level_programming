#!/usr/bin/python3
if __name__ == "__main__":
    import sys  # import sys module
    argv = sys.argv[1:]  # get arguments from command line
    argc = len(argv)  # get number of arguments

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
