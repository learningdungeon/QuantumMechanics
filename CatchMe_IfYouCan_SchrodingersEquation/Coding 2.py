from qiskit.quantum_info import Statevector
# Remove the measurement for a moment to see the 'pure' address
circuit_no_meas = circuit.remove_final_measurements(inplace=False)
state = Statevector.from_instruction(circuit_no_meas)
print(state)
