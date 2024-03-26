from bitstring import BitString

def test():
    testBitString = BitString(5)
    testBitString.set_int_config(1024)
    assert 1024 == testBitString.int()

def testPackage():
    test()
    print("Passed Tests")