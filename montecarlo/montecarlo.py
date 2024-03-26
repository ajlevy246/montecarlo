"""Provide the primary functions."""

from BitString import *

def test():
    testBitString = BitString(5)
    testBitString.set_int_config(1024)
    print("Should be 1024: ", testBitString.int())

if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print("Running as main")
