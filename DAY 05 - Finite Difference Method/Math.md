
# 🧮 Mathematical Framework: Finite Difference Method (FDM)
### Physical Layer Analysis for 2nm GaAs Quantum Wells

## 1. The Schrödinger Equation
To model the energy levels ($E_n$), we solve the 1D Time-Independent Schrödinger Equation:
$$-\frac{\hbar^2}{2m^*} \frac{d^2\psi(z)}{dz^2} + V(z)\psi(z) = E\psi(z)$$

Where:
* **$\hbar$**: Reduced Planck's Constant.
* **$m^*$**: Effective mass of the electron in GaAs ($0.067 \cdot m_0$).
* **$V(z)$**: Potential energy (0 in the well, $V_0$ in the barriers).

## 2. Discretization (FDM)
We approximate the second derivative using the central difference formula:
$$\frac{d^2\psi}{dz^2} \approx \frac{\psi_{i+1} - 2\psi_i + \psi_{i-1}}{\Delta z^2}$$

Substituting this into the Schrödinger equation gives us the Hamiltonian matrix $H$:
$$H_{i,i} = \frac{\hbar^2}{m^* \Delta z^2} + V_i$$
$$H_{i,i\pm1} = -\frac{\hbar^2}{2m^* \Delta z^2}$$

## 3. The "Architect's" Numerical Proof
Using $L_z = 2$nm and $V_0 = 0.3$eV:
* **$E_1 \approx 0.204$ eV**: Validates the ground state is safely trapped.
* **$E_2 \approx 0.353$ eV**: Proves the excited state exceeds $V_0$, causing the "leakage" observed in Day 05 simulations.

**This math serves as the foundation for the RAQT Physical Layer stability checks.**
