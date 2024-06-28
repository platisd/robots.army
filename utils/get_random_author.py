"""
This script reads the provided authors.yml file and prints a random key (not value)
corresponding to one of the authors in the file.
"""

import sys
import argparse
import random

import yaml


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("authors_file", help="Path to authors.yml file")
    args = parser.parse_args()

    with open(args.authors_file, "r") as f:
        authors = yaml.safe_load(f)

    author = random.choice(list(authors.keys()))
    print(author)

    return 0


if __name__ == "__main__":
    sys.exit(main())
