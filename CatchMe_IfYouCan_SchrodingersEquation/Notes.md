# 🛠️ Quantum Circuit: Defining the Digital Address (Ψ)

In this stage of the **Electronoogle Map**, we move from theory to implementation. This Qiskit script defines the precise rotation of an electron within its probability cloud using a universal gate sequence.

### 📜 The Code (Qiskit Python)
This snippet creates a 1-qubit state within a 156-qubit system (representing a large-scale IBM Quantum processor).

```python
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

# Define the Register (Allocating space on a large-scale processor)
qreg_q = QuantumRegister(156, 'q')
creg_c = ClassicalRegister(1, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

# Stop 5: Setting the Address (Universal Rotation)
circuit.rz(-pi / 2, qreg_q[0])   # Phase adjustment
circuit.rx(pi / 4, qreg_q[0])    # The 'Agility' shift (Superposition)
circuit.rz(pi / 2, qreg_q[0])    # Final coordinate lock

# The Hunter's Measurement
circuit.measure(qreg_q[0], creg_c[0])
