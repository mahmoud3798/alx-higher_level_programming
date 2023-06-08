#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    num_args = len(args)

    print("{} {}{}.".format(num_args, "argument" if num_args == 1 else "arguments" if num_args > 1 else "", ":" if num_args > 0 else "."))

    for i, arg in enumerate(args):
	print("{}: {}".format(i + 1, arg))
