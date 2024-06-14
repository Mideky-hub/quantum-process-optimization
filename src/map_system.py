from qiskit import QuantumCircuit
from qiskit.circuit.library import PauliTwoDesign
from qiskit.quantum_info import SparsePauliOp

import numpy as np

n_qbits = 30

qc = PauliTwoDesign( # PauliTwoDesign is a circuit library which generates a circuit with a specific structure
                     # The structure is a series of random Pauli gates followed by a series of random 2-qubit gates
                     # The number of qubits is determined by the `num_qubits` parameter
                     # The number of Pauli gates and 2-qubit gates is determined by the `reps` parameter
                     # The `seed` parameter is used to generate the random gates
                     # The `insert_barriers` parameter determines whether barriers are inserted between the layers
    num_qubits=n_qbits,
    reps=4,
    seed=5,
    insert_barriers=True
)

parameters = qc.parameters

obs = SparsePauliOp.from_sparse_list(
    [("Z", [n_qbits-2], 1)],
    num_qubits=n_qbits
)

np.random.seed(0)
phi_max = 0.5 * np.pi
parameter_values = np.random.uniform(-1 * phi_max, phi_max, len(parameters))