# [Day 4] Semiconductor Physics & System Architecture
## Topic: Effective Mass Mismatch and 2D Confinement

---

### 📋 Overview
Today's research focused on the physical layer of quantum networking, specifically how the inherent properties of semiconductors (like **GaAs**) impact signal emission and stability in a 30km fiber relay.

---

### 🔬 Key Concepts

#### 1. The Effective Mass Mismatch
In crystalline structures, electrons and holes move differently due to their **Effective Mass** ($m^*$).

* **Electrons (m_e* approx 0.0):** Fast, agile, and high mobility.
* **Holes (m_h* approx 0.4):** Relatively heavy and slow.
* **Architectural Impact:** This mismatch makes recombination (the meeting of e^- and h^+to emit a photon) a statistical challenge. If they don't meet, no signal is generated.

#### 2. 2D Quantum Well Engineering
To solve the mismatch, we utilize **Spatial Confinement**:

* By narrowing the walls (L) of the quantum well, we force the wavefunctions of the electron and hole to overlap.
* This **"Bumping"** or forced collision increases **Recombination Efficiency**.
* **Result:** A sharper, more reliable photon signal for the **RAQT** framework.

#### 3. Trade-offs in Barrier Height
Engineering the "well" requires balancing energy retention vs. power:

* **Raising Barriers:** Prevents "Energy Leaks" (Quantum Tunneling) by creating a higher potential wall.
* **Cost:** Requires higher operating voltage (Power consumption), which is a critical constraint for remote or resource-constrained deployments.

---

### 💡 Architect's Reflection
> *"If the station (Hole) is heavy and the train (Electron) is too fast, the passenger (Information) can't board. We narrow the platform (2D Well) to ensure the connection happens."*

---
*Log generated with technical support from Gemini.*
