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
        """_summary_

        :return: _description_
        :rtype: _type_
        """
        stringRep = ""
        for bit in self.config:
            stringRep += str(bit)
        return stringRep

    def __eq__(self, other): 
        """_summary_

        :param other: _description_
        :type other: _type_
        :return: _description_
        :rtype: _type_
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
        """_summary_

        :return: _description_
        :rtype: _type_
        """
        return len(self.config)

    def on(self):
        """_summary_

        :return: _description_
        :rtype: _type_
        """
        countOn = 0
        for bit in self.config:
            if bit == 1:
                countOn += 1
        return countOn
    
    def off(self):
        """_summary_

        :return: _description_
        :rtype: _type_
        """
        countOff = 0
        for bit in self.config:
            if bit == 0:
                countOff += 1
        return countOff
    
    def flip_site(self,i):
        """_summary_

        :param i: _description_
        :type i: _type_
        """
        self.config[i] = 0 if self.config[i] else 1
    
    def int(self):
        """_summary_

        :return: _description_
        :rtype: _type_
        """
        return int(str(self), 2)
 
    def set_config(self, s):
        """_summary_

        :param s: _description_
        :type s: list[int]
        """
        self.config = np.array(s)
        

    def set_int_config(self, dec, digits=0):
        """_summary_

        :param dec: _description_
        :type dec: int
        :param digits: _description_, defaults to 0
        :type digits: int, optional
        """
        digits = len(self.config) if not digits else digits
        binFromInt = "{0:b}".format(dec) #Convertes decimal to binary
        tmpArray = [0 for i in range(digits - len(binFromInt))] if digits else [] #Initializes array as empty if digits is not passsed, else length digits-bin length
        
        for binDigit in binFromInt:
            tmpArray.append(int(binDigit))

        self.config = np.array(tmpArray)

    def sum(self):
        """_summary_

        :return: _description_
        :rtype: _type_
        """
        numList = [int(bit) for bit in str(self)] #Convert numpy.bitstring into list of ints, because I can't figure out how to sum over it
        return sum(numList) #Super inefficient but whatever.