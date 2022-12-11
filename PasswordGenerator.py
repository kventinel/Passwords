#!/usr/bin/env python3
import argparse
import random
import string

def _parse_args():
    parser = argparse.ArgumentParser(description='Script for generate random password')
    symbols_group = parser.add_mutually_exclusive_group()
    symbols_group.add_argument(
        '--digits', action='store_true',
        help='use, if want generate password only from digits'
    )
    symbols_group.add_argument(
        '--digits-and-letters', action='store_true',
        help='use, if want generate password only from digits and letters'
    )
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
    if not args.digits:
        symbols += string.ascii_letters
        if not args.digits_and_letters:
            symbols += '!@#$%^&*()_-=+,<.>/?'
    print(pass_generator(args.size, symbols))

if __name__ == "__main__":
    _main(_parse_args())
