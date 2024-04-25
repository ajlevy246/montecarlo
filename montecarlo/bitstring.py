import numpy as np

#;laskdjfl;aksdjf
class BitString:
    """Simple class to generate a bitstring configuration
    """
    def __init__(self, N):
        """Intializes a new bitstring object

        :param N: Number of bits
        :type N: int
        """
        self.N = N
        self.config = np.zeros(N, dtype=int) 

    def __repr__(self):
        """Returns a string representation of the object

        :return: string rep
        :rtype: string
        """
        stringRep = ""
        for bit in self.config:
            stringRep += str(bit)
        return stringRep

    def __eq__(self, other): 
        """checks whether two bitstrings are equal

        :param other: another object to check against
        :type other: any
        :return: True if equal, false otherwise.
        :rtype: boolean
        """
        try:       
            return True if (self.config==other.config).all() else False #Works if other is a BitString object.
        except: 
            thisArray = list(self.config)
            if (len(thisArray) == len(other)):
                for i in range(len(thisArray)):
                    if (thisArray[i] != other[i]):
                        print("Found difference")
                        return False
                return True
            return False #Works if other is a list
     
    def __len__(self):
        """Returns the length of the underlying array.

        :return: length of the array
        :rtype: int
        """
        return len(self.config)

    def on(self):
        """Returns the number of bits that are flipped on.

        :return: Number of on bits
        :rtype: int
        """
        countOn = 0
        for bit in self.config:
            if bit == 1:
                countOn += 1
        return countOn
    
    def off(self):
        """Returns the number of bits that are flipped off.

        :return: Number of off bits
        :rtype: int
        """
        countOff = 0
        for bit in self.config:
            if bit == 0:
                countOff += 1
        return countOff
    
    def flip_site(self,i):
        """Flips the bit at the given index

        :param i: index to flip
        :type i: int
        """
        self.config[i] = 0 if self.config[i] else 1
    
    def int(self):
        """Returns an integer representation of the object.

        :return: base 10 integer representation.
        :rtype: int
        """
        return int(str(self), 2)
 
    def set_config(self, s):
        """sets the configuration of the bit string.

        :param s: A new configuration to set.
        :type s: list[int]
        """
        self.config = np.array(s)
        

    def set_int_config(self, dec, digits=0):
        """Sets the configuration of the bit string, based on a decimal integer.

        :param dec: decimal integer
        :type dec: int
        :param digits: number of digits to configure to, defaults to 0
        :type digits: int, optional
        """
        digits = len(self.config) if not digits else digits
        binFromInt = "{0:b}".format(dec) #Convertes decimal to binary
        tmpArray = [0 for i in range(digits - len(binFromInt))] if digits else [] #Initializes array as empty if digits is not passsed, else length digits-bin length
        
        for binDigit in binFromInt:
            tmpArray.append(int(binDigit))

        self.config = np.array(tmpArray)

    def sum(self):
        """Sums the number of on bits.

        :return: Sum of on bits
        :rtype: int
        """
        numList = [int(bit) for bit in str(self)] #Convert numpy.bitstring into list of ints, because I can't figure out how to sum over it
        return sum(numList) 