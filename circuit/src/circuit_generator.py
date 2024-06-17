# Built-in modules
import math

# Imports from Qiskit
from qiskit import QuantumCircuit
from qiskit.circuit.library import *
from qiskit.visualization import plot_distribution

# Imports from Qiskit Runtime
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime import SamplerV2 as Sampler

from time import sleep

""" 
Circuit Generator that will generate specific circuits for the user to run on IBM Quantum hardware.
"""

class CircuitGenerator():
    def __init__(self) -> None:
        pass
    
    def __str__(self) -> str:
        print(self)
    
    def knapsack(self, weights, values, max_weight):
        n = len(weights)
        dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for w in range(1, max_weight + 1):
                if weights[i - 1] <= w:
                    dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
                else:
                    dp[i][w] = dp[i - 1][w]
        
        return dp[n][max_weight]
        
        

    
def main():
    Circuit = CircuitGenerator()
    oracle = Circuit.quantum_knapsack(self=Circuit, weights=[1, 2, 3], values=[60, 100, 120], max_weight=5)
    oracle.draw(output="mpl", style="iqp").show()
    sleep(20)
    
main()