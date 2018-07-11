import sys
import os


def main():
    if len(sys.argv) < 2:
        print('No directory path given in input')
        sys.exit(1)

    print('parsing directory ' + sys.argv[1])

    dirname = sys.argv[1]
    for filename in os.listdir(dirname):
        print(filename + '\n')

if __name__ == "__main__":
    main()
