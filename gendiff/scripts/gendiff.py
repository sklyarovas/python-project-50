import argparse


parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

parser.add_argument('first_file', type=str, help='')
parser.add_argument('second_file', type=str, help='')

args = parser.parse_args()


def main():
    print(f'{args.first_file} and {args.second_file}')


if __name__ == "__main__":
    main()
