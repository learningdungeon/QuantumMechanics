# --- RAQT Hardware Architecture Logic (Day 4) ---
# This version is a pure Logic Class to bypass NetSquid abstract errors.

class RAQT_Logic:
    def __init__(self, L_nm, m_e, m_h):
        self.width = L_nm
        self.m_e = m_e
        self.m_h = m_h
        
    def calculate_recombination_prob(self):
        # Logic: Smaller L (Width) = Higher Overlap
        # Logic: High mass mismatch = lower efficiency
        mismatch = abs(self.m_h - self.m_e)
        efficiency = (1.0 / self.width) * (1.0 - mismatch)
        return max(0.0, min(1.0, efficiency))

# --- Execution ---
try:
    # GaAs Parameters
    gaas = RAQT_Logic(L_nm=2, m_e=0.067, m_h=0.45)
    prob = gaas.calculate_recombination_prob()

    print("\n" + "="*45)
    print("🚀 RAQT HARDWARE LOGIC: SUCCESS")
    print("="*45)
    print(f"Material: GaAs (Gallium Arsenide)")
    print(f"Well Width (L): {gaas.width} nm")
    print(f"Mass Mismatch: {abs(gaas.m_h - gaas.m_e):.3f}")
    print(f"Recombination Probability: {prob:.2%}")
    print("="*45 + "\n")

except Exception as e:
    print(f"❌ Error: {e}")
