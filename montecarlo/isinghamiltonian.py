import numpy as np
from bitstring import BitString

class IsingHamiltonian:
    def __init__(self, J: list[list[tuple][int, int]], mus: list[int]):
        self.J = J
        self.mus = mus
    
    def compute_average_values(self, temperature: int):
        #Iterate over all possible bit strings, return the average energy, average magnetization, heat capactity and magnetic susceptibility

        bs = BitString(len(self.J)) #Creates a bew bitstring object of length (length of J).

        beta = 1/(1.38064852 **(10**(-23)) * temperature) #Calculate beta

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

    def energy(self, bs: BitString):
        energy = 0 #Initialize energy
        bitStringArray = [1 if bit else -1 for bit in bs.config] #Convert 0's --> -1's

        for node in self.J: #Node: [(connected node, edge weight), ....]
            for edge in node: #Edge: (connected node, edge weight)
                if node < edge[0]: #Ignores duplicated edges
                    connectionEnergy = bitStringArray[node] * bitStringArray[edge[0]] * edge[1] #spin(node1) * spin(node2) * edge weight
                    energy += connectionEnergy #Adds energy of the given edge to the total
                    
            energy += bitStringArray[node] * self.mus[node] #For each node, adds the mu value of the node to the total energy

        return energy



        
        
