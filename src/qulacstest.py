from qulacs import Observable, QuantumCircuit, QuantumState
from qulacs.gate import Y,CNOT,merge

def qtest(angle):
    state = QuantumState(3)
    state.set_Haar_random_state()
    circuit = QuantumCircuit(3)
    circuit.add_X_gate(0)
    merged_gate = merge(CNOT(0,1),Y(1))
    circuit.add_gate(merged_gate)
    circuit.add_RX_gate(1, angle)
    circuit.update_quantum_state(state)
    observable = Observable(3)
    observable.add_operator(2.0, "X 2 Y 1 Z 0")
    observable.add_operator(-3.0, "Z 2")
    result = observable.get_expectation_value(state)
    
    output = {'energy': result}
    return(output)
