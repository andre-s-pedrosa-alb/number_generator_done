#!/usr/bin/python3

import random
import sys

def generate(arg: str) -> None:
    print(random.randint(1, arg))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} MAX_RANGE", file=sys.stderr)
        sys.exit(1)

    generate(sys.argv[1])
