from os import getcwd
from sys import argv

from crlf.crlf import main


def start():
    main(getcwd(), argv[1:])


if __name__ == '__main__':
    start()
