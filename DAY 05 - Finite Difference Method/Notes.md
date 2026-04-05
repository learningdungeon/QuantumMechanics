
# 📝 Quantum Research Log: Day 05
### Date: April 6, 2026 | Focus: 2D Confinement & Sub-bands

## 1. Core Concept: The "Z-XY" Split
Today I learned that a **Quantum Well** isn't just a 1D line; it's a 3D environment with different rules for different directions:
* **Z-Direction (Vertical):** The particle is "trapped" by material barriers (AlGaAs). This creates discrete energy levels ($E_1, E_2$).
* **XY-Plane (Horizontal):** The particle is "free" to move side-to-side. This creates a continuous range of energy starting from each $E_n$.

## 2. Numerical Discovery: The "Leakage" Threshold
By coding the **Finite Difference Method** in Python, I found a critical architectural limit:
* **Simulation Result:** For a **2nm GaAs well**, the first excited state ($E_2$) is **0.3535 eV**.
* **The Problem:** Standard AlGaAs barriers are often $\approx$ **0.3 eV**. 
* **The Lesson:** In a **30km relay**, using $E_2$ for data would fail because the energy is higher than the walls of the "well." The signal would literally "leak" out.

## 3. The "Architect's" Strategy
* **Material Engineering:** To fix leakage, we must either widen the well (to lower the energy levels) or increase the Aluminum fraction (to raise the barrier walls).
* **Quantum for All:** I practiced translating these "Sub-band" paraboloids into simple daily terms: "The electron is in a room where it can't jump through the ceiling (Z), but it can run around the floor as much as it wants (XY)."

## 4. Tools & Integration
* **NetSquid:** Best for modeling the **Time & Distance** of the 30km fiber.
* **Qiskit:** Best for the **Secure Logic** of the Zero-Day protection protocol.
* **FDM Python:** The "Engine" used to verify the physical stability before scaling.

**"We don't just build circuits; we engineer the reality that holds the qubits."**
