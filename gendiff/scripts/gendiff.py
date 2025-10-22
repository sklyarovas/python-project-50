import argparse

from gendiff.main import core


def parser_configuration():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', 
                        type=str, 
                        help='set format of output', 
                        default='stylish')

    return parser.parse_args()


def main():
    args = parser_configuration()
    core(args.format, args.first_file, args.second_file)


if __name__ == "__main__":
    main()
