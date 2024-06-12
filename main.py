import random
import sys

def generate(args: list[str]) -> None:
    print(random.randint(1, args[0]))

if __name__ == '__main__':
    generate(sys.argv[1:])
