import argparse

from gendiff import generate_diff


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
    generate_diff(args.first_file, args.second_file, args.format)


if __name__ == "__main__":
    main()
