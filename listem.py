import argparse
import os


def list_dirs(dirs, flags):
    if dirs is None:
        return 'No files in the current directory.'

    dirs.sort()
    splice_index = 0

    if 'a' not in flags:
        for i, d in enumerate(dirs):
            if d[0] != '.':
                splice_index = i
                break

    for d in dirs[splice_index:]:
        print(d)


def get_dirs(args):
    dirs = os.listdir(args.path)
    return dirs


def get_flags(args):
    flags = []

    if args.all:
        flags.append('a')

    return flags


def main(args=None):
    parser = argparse.ArgumentParser(description='Lists directory contents.')
    parser.add_argument(
        'path', nargs='?', default=os.getcwd(), help='File path')
    parser.add_argument('-a', dest='all',
                        action='store_true', help='List all files.')

    args = parser.parse_args()

    dirs = get_dirs(args)
    flags = get_flags(args)

    list_dirs(dirs, flags)


if __name__ == '__main__':
    main()
