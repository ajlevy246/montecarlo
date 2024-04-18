import numpy as np

from .bitstring import BitString

class IsingHamiltonian:
    """Ising Hamiltonian Class
    For calculating thermodynamic averages
    """
    def __init__(self, J, mus):
        """_summary_

        :param J: J values
        :type J: _type_
        :param mus: Mu values
        :type mus: _type_
        """
        self.J = J
        self.mus = mus
    
    def compute_average_values(self, temperature: int):
        #Iterate over all possible bit strings, return the average energy, average magnetization, heat capactity and magnetic susceptibility

        bs = BitString(len(self.J)) #Creates a new bitstring object of length (length of J).

        beta = 1/(1.38064852 ** (10 ** (-23)) * temperature) #Calculate beta

        factorZ = 0
        averageEnergyEV = 0
        averageMagEV = 0
        averageEnergySqEV = 0
        averageMagSqEV = 0

        for i in range(2**len(bs)): #Loop over all configurations

            bs.set_int_config(i) #Sets the current configuration

            stateEnergy = self.energy(bs) #Calculates energy
            stateMag = bs.sum() - (len(bs) - bs.sum()) #Calculates magnetization

            configProbability = np.e**(-1*beta*stateEnergy) #Calculates the probability without the scaling factor (Z)

            factorZ += configProbability #Increments the scaling factor Z

            #Calculates expectation values, without including scaling factor Z
            currentEnergyEV = stateEnergy * configProbability
            currentEnergySqEV = currentEnergyEV * stateEnergy 
            currentMagEV = stateMag * configProbability 
            currentMagSqEV = currentMagEV * stateMag

            #Adds the calculated expection values to the totals
            averageEnergyEV += currentEnergyEV 
            averageEnergySqEV += currentEnergySqEV

            averageMagEV += currentMagEV
            averageMagSqEV += currentMagSqEV

        #Divide by scaling factor Z
        averageEnergyEV /= factorZ 
        averageMagEV /= factorZ 
        averageEnergySqEV /= factorZ
        averageMagSqEV /= factorZ 

        #Calc final values for HC and MS
        heatCapacity = (averageEnergySqEV - (averageEnergyEV**2)) / temperature
        magneticSusceptibility = (averageMagSqEV - (averageMagEV**2)) / temperature

        return averageEnergyEV, averageMagEV, heatCapacity, magneticSusceptibility



#--------------------------------------------
#Helper functions

    def energy(self, bs):
        energy = 0 #Initialize energy
        bitStringArray = [1 if bit else -1 for bit in bs.config] #Convert 0's --> -1's

        for i in range(len(self.J)): #Node: [(connected node, edge weight), ....]
            node = self.J[i]
            for edge in node: #Edge: (connected node, edge weight)
                if i < edge[0]: #Ignores duplicated edges
                    connectionEnergy = bitStringArray[i] * bitStringArray[edge[0]] * edge[1] #spin(node1) * spin(node2) * edge weight
                    energy += connectionEnergy #Adds energy of the given edge to the total
                    
            energy += bitStringArray[i] * self.mus[i] #For each node, adds the mu value of the node to the total energy. Should not contribute in this example

        return energy



        
        
