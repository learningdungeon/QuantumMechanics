
# 🌀 Quantum Systems Architecture: 2D Heterostructure
### Day 05: Numerical Analysis of GaAs/AlGaAs Quantum Wells

## 🏗️ The Architectural Design
Modeling the physical layer of a **30km Quantum Relay** using the **RAQT** framework.

* **Well:** GaAs (2nm)
* **Barrier:** AlGaAs (V0 ≈ 0.3 eV)
* **Method:** Finite Difference Method (FDM) in Python.

## 💻 Simulation Results
| State | Energy (eV) | Status |
| :--- | :--- | :--- |
| **E1 (Ground)** | **0.2044 eV** | **Confined** |
| **E2 (Excited)** | **0.3535 eV** | **Leaking** |

## 🔍 Architect's Analysis
* **Leakage Issue:** E2 exceeds the barrier height (0.3 eV). 
* **Impact:** High risk of signal loss in a 30km fiber relay.
* **Fix:** Next iteration will test a **5nm** width to pull E2 below the barrier.

**Author:** Noor-Ul-Ain | Qiskit Advocate
EOF
