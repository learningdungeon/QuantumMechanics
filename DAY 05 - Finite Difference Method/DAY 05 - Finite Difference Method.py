import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh

# --- 1. Physical Constants (SI Units) ---
hbar = 1.054e-34
m_e = 9.11e-31
q_e = 1.602e-19
m_eff = 0.067 * m_e  # Effective mass for GaAs

# --- 2. Geometry & Potential ---
L = 20e-9           # Total simulation width (20 nm)
well_width = 2e-9    # The "Architect's" 2nm Well
N = 1000             # Number of grid points
z = np.linspace(-L/2, L/2, N)
dz = z[1] - z[0]

# Define V(z): 0 in the well, 0.3 eV in the barriers
V_barrier = 0.3 * q_e 
V = np.where(np.abs(z) < well_width/2, 0, V_barrier)

# --- 3. Build the Hamiltonian Matrix ---
# Kinetic energy part (Finite Difference)
main_diag = (hbar**2 / (m_eff * dz**2)) * np.ones(N) + V
off_diag  = -0.5 * (hbar**2 / (m_eff * dz**2)) * np.ones(N-1)

# Solve for Eigenvalues (E_n) and Eigenvectors (psi)
energies, wavefunctions = eigh(np.diag(main_diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1))

# --- 4. Result in eV ---
print(f"E1: {energies[0]/q_e:.4f} eV")
print(f"E2: {energies[1]/q_e:.4f} eV")

# --- 5. Visualization ---
plt.plot(z*1e9, V/q_e, 'k', label="Potential V(z)")
for i in range(2):
    plt.plot(z*1e9, (wavefunctions[:, i]*1e9) + energies[i]/q_e, label=f"n={i+1}")
plt.xlabel("Position (nm)")
plt.ylabel("Energy (eV)")
plt.title("2nm Quantum Well Confinement")
plt.legend()
# --- Save the graph as an image file ---
# --- Add this line to save the image as a file ---
plt.savefig('quantum_well_plot.png')
plt.show()