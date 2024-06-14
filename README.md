# Quantic Optimization of Post-processing result in problem mapping for quantum circuit

This repository contains the code that will be used to generate the results for future publication. The code is written in Python and C++ and uses the Qiskit library to interact with the IBM quantum computer.

The goal of this project is to optimize the post-processing of the results of a quantum circuit. The optimization is done by using a quantum computer to find the best mapping of the problem to the quantum circuit.

This implies having an optimized mapping of the problem for NP-complete applications.

## Quantic computer used for the different experiments

The different experiments are done using IBM Quantum computer, selected for the lowest EPLG (Error Per Layered Gate for a 100-qbits chain) and the highest number of qubits with the highest CLOPS_h (Circuit Layer Operation Per Second) and regarding the financial cost of the experiment.

Here is the list of the different quantum computers used for the experiments table : 

| Name | EPLG | CLOPS_h | Qubits | Cost |
|------|------|---------|--------| ---- |
| ibm_torino|0.9%|3.8K|133| High|
| ibm_sherbrooke|1.7%|5K|127| Medium |
| ibm_kyiv | 1.9% | 5K | 127 |  High |
| ibm_quebec | 2% | 5K | 127 | High |

For the different experiments, the quantum computer used is the ibm_sherbrooke and the ibm_torino.

