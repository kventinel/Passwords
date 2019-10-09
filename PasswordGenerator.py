#!/usr/bin/env python3
import argparse
import random
import string

def _parse_args():
    parser = argparse.ArgumentParser(description='Script for generate random password')
    parser.add_argument('--only-digits', action='store_true',
                        help='use, if want generate password only from digits')
    parser.add_argument('--size', type=int, default=16, help='size of password')
    return parser.parse_args()

def pass_generator(size, symbols):
    """
    Generate password of given size from given symbols.
    """
    random.seed();
    return ''.join(random.choice(symbols) for _ in range(size))

def _main(args):
    symbols = string.digits
    if not args.only_digits:
        symbols += string.ascii_letters
    print(pass_generator(args.size, symbols))

if __name__ == "__main__":
    _main(_parse_args())
