import montecarlo

test = montecarlo.BitString(10) #Test bitstring with 10 bits.

def test_to_str():
    assert (str(test) == "0000000000")

def test_equals():
    assert (test == montecarlo.BitString(10))
    assert (test == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    assert (test != [1, 1, 1])
    assert (test != [0, 1, 0, 0, 0, 0, 0, 0, 0, 0])

def test_length():
    assert (len(test) == 10)
    assert(len(montecarlo.BitString(5)) == 5)

def test_on():
    assert (test.on() == 0)
    assert (test.off() == 10)

def test_flip_site():
    test.flip_site(0)
    assert(str(test) == "1000000000")

    test.flip_site(0)
    test.flip_site(1)
    assert(str(test) == "0100000000")

def test_int():
    test.set_int_config(0)
    assert (test.int() == 0)

    test.set_int_config(1)
    assert(test.int() == 1)

    test.set_int_config(3)
    assert(test.int() == 3)

def test_set_config():
    test.set_config([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    assert(test == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

def test_set_int_config():
    test.set_int_config(5, 4)
    assert(test == [0,1,0,1])

def test_sum():
    test.set_int_config(0)
    assert(test.sum() == 0)
    test.set_int_config(5, 4)

    assert(test.sum() == test.on())
