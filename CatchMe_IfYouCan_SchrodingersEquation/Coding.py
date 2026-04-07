from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(156, 'q')
creg_c = ClassicalRegister(1, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.rz(-pi / 2, qreg_q[0])
circuit.rx(pi / 4, qreg_q[0])
circuit.rz(pi / 2, qreg_q[0])
circuit.measure(qreg_q[0], creg_c[0])
