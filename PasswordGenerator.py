import string
import random

def pass_generator(size=16, chars=string.ascii_letters + string.digits):
    random.seed();
    return ''.join(random.choice(chars) for _ in range(size))

if __name__ == "__main__":
    print(pass_generator())