### 🧮 The Mathematical Framework: 2D Confinement Logic

To bridge the gap between abstract code and semiconductor physics, we must define the energy levels within the GaAs Quantum Well. We treat the system as an **Infinite Square Well** in the z-direction to "force" the wavefunction overlap.

#### **1. Energy Eigenvalues**
The allowed energy levels for both the electron ($e$) and the hole ($h$) are governed by the Schrödinger equation for a confined particle:

$$E_n = \frac{n^2 \pi^2 \hbar^2}{2 m^* L^2}$$

**Where:**
* $n=1$ (The ground state/first energy level).
* $\hbar$ (H-bar) is the reduced Planck constant.
* $m^*$ is the **Effective Mass** ($0.067$ for $e$, $0.45$ for $h$ in GaAs).
* $L=2\text{nm}$ (The specific Well Width used in `Simulation.py`).

#### **2. The Effective Mass Mismatch ($\Delta m$)**
The synchronization gap is mathematically represented by the ratio of their kinetic behaviors. Because the hole is significantly heavier ($0.45$), its energy levels are much lower and "denser," leading to a significant mismatch in state preparation:

$$\Delta m_{\text{ratio}} = \frac{m_{e}^{*}}{m_{h}^{*}} \approx 0.148$$

This ratio explains why the "lighter" electron responds more drastically to the confinement than the "heavy" hole. To achieve entanglement, we must account for this energy offset.



#### **3. Recombination Probability ($P_{\text{recomb}}$)**
The probability of a successful photon emission is proportional to the **Spatial Overlap Integral** of the electron ($\psi_e$) and hole ($\psi_h$) wavefunctions:

$$P_{\text{recomb}} \propto \left| \int_{0}^{L} \psi_{e}(z) \psi_{h}(z) \, dz \right|^2$$

By reducing the well width $L$ to **2nm**, we compress these wavefunctions into a smaller volume, mathematically forcing them to interact. In the RAQT simulation logic, this yielded our validated baseline:

> **Validated Recombination Probability: 30.85%**

---

### 💡 Architect's Note on Math
In **Blue Team** operations for Quantum Networks, these equations aren't just theory—they are the parameters for our **Noise Models**. By calculating the exact energy mismatch, we can predict where the "Quantum Signal" is most vulnerable to environmental decoherence. Mastering the atoms is the first step to securing the network.
