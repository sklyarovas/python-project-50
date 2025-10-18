import argparse


parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', type=str, help='set format of output', default='plain')

args = parser.parse_args()


def main():
    print(f'{args.first_file} and {args.second_file}')


if __name__ == "__main__":
    main()
