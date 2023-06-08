#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    res = 0
    args = sys.argv[:]
    num_args = len(args)
    for i in range(1, num_args):
        res += int(sys.argv[i])
    print(res)
