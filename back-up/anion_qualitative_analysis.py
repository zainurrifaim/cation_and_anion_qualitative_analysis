# ======================
# CHEMICAL REACTION DATA
# ======================

ANION_REACTIONS = {
    # Group I (Dilute H₂SO₄ Group)
    "CO₃²⁻": {
        "test": "Effervescence + lime water",
        "reaction": "CO₃²⁻ + 2H⁺ → CO₂↑ + H₂O\nCO₂ + Ca(OH)₂ → CaCO₃↓ (milky)",
        "reason": "Carbonates release CO₂ gas that forms insoluble calcium carbonate (Ksp = 4.5×10⁻⁹)"
    },
    "S²⁻": {
        "test": "Lead acetate paper",
        "reaction": "S²⁻ + Pb²⁺ → PbS↓ (black, Ksp = 9.0×10⁻²⁹)",
        "reason": "Extremely low solubility allows detection at ppm levels"
    },
    "NO₂⁻": {
        "test": "Brown fumes with acid",
        "reaction": "2NO₂⁻ + 2H⁺ → NO₂↑ (brown) + NO↑ + H₂O",
        "reason": "Nitrous acid decomposition produces characteristic brown gas"
    },
    "CH₃COO⁻": {
        "test": "Vinegar smell",
        "reaction": "CH₃COO⁻ + H⁺ → CH₃COOH↑ (pKa = 4.76)",
        "reason": "Volatile acetic acid detected by odor"
    },

    # Group II (Conc. H₂SO₄ Group)
    "Cl⁻": {
        "test": "AgNO₃ precipitation",
        "reaction": "Ag⁺ + Cl⁻ → AgCl↓ (white, Ksp = 1.8×10⁻¹⁰)\nAgCl + 2NH₃ → [Ag(NH₃)₂]⁺ (soluble)",
        "reason": "Distinctive solubility behavior in ammonia"
    },
    "Br⁻": {
        "test": "AgNO₃ precipitation",
        "reaction": "Ag⁺ + Br⁻ → AgBr↓ (pale yellow, Ksp = 5.0×10⁻¹³)",
        "reason": "Intermediate solubility product distinguishes from other halides"
    },
    "I⁻": {
        "test": "AgNO₃ precipitation",
        "reaction": "Ag⁺ + I⁻ → AgI↓ (yellow, Ksp = 8.5×10⁻¹⁷)",
        "reason": "Most insoluble silver halide"
    },
    "NO₃⁻": {
        "test": "Brown ring test",
        "reaction": "NO₃⁻ + 3Fe²⁺ + 4H⁺ → NO↑ + 3Fe³⁺ + 2H₂O\nFe²⁺ + NO → [Fe(NO)]²⁺ (brown ring)",
        "reason": "Nitric oxide complexation with Fe²⁺ (E° = +0.96V)"
    },

    # Group III (Special Tests)
    "SO₄²⁻": {
        "test": "BaCl₂ in acid",
        "reaction": "Ba²⁺ + SO₄²⁻ → BaSO₄↓ (white, Ksp = 1.1×10⁻¹⁰)",
        "reason": "Kinetically inert precipitate resistant to acid dissolution"
    },
    "PO₄³⁻": {
        "test": "Ammonium molybdate",
        "reaction": "PO₄³⁻ + 12MoO₄²⁻ + 3NH₄⁺ + 24H⁺ → (NH₄)₃PO₄·12MoO₃↓ (yellow)",
        "reason": "Heteropoly acid formation under acidic conditions"
    },
    "BO₃³⁻": {
        "test": "Flame test",
        "reaction": "BO₃³⁻ + H₂SO₄ + CH₃CH₂OH → B(OCH₂CH₃)₃ (green flame)",
        "reason": "Volatile boron ester produces characteristic green color"
    }
}

# ======================
# CORE FUNCTIONS
# ======================

def print_reaction_explanation(ion):
    """Display detailed chemical explanation for detected ion"""
    if ion in ANION_REACTIONS:
        print(f"\nReaction Details for {ion}:")
        print(f"Test Method: {ANION_REACTIONS[ion]['test']}")
        print(f"Chemical Equation:\n{ANION_REACTIONS[ion]['reaction']}")
        print(f"Scientific Principle: {ANION_REACTIONS[ion]['reason']}")
    else:
        print(f"\nNote: No reaction details available for {ion}")

def get_user_input(prompt, options=None):
    """Get validated user input"""
    while True:
        response = input(prompt).lower().strip()
        if not options or response in options:
            return response
        print(f"Please enter one of: {', '.join(options)}")

# ======================
# GROUP TEST FUNCTIONS
# ======================

def test_group_i():
    """Test for Group I anions (CO₃²⁻, S²⁻, NO₂⁻, CH₃COO⁻)"""
    detected = []
    print("\n=== GROUP I: Dilute H₂SO₄ Tests ===")
    
    if get_user_input("Add dilute H₂SO₄. Gas evolved? (y/n): ", ['y', 'n']) == 'y':
        gas_type = get_user_input("Describe the gas (effervescence/rotten egg/brown/vinegar): ",
                                ['effervescence', 'rotten egg', 'brown', 'vinegar'])
        
        if gas_type == "effervescence":
            if get_user_input("Pass gas through lime water. White precipitate? (y/n): ", ['y', 'n']) == 'y':
                detected.append("CO₃²⁻")
                print("-> CO₃²⁻ confirmed: Effervescence and white precipitate")
                print_reaction_explanation("CO₃²⁻")
        
        elif gas_type == "rotten egg":
            if get_user_input("Expose lead acetate paper. Turns black? (y/n): ", ['y', 'n']) == 'y':
                detected.append("S²⁻")
                print("-> S²⁻ confirmed: Rotten egg smell and black precipitate")
                print_reaction_explanation("S²⁻")
        
        elif gas_type == "brown":
            detected.append("NO₂⁻")
            print("-> NO₂⁻ confirmed: Brown fumes")
            print_reaction_explanation("NO₂⁻")
        
        elif gas_type == "vinegar":
            detected.append("CH₃COO⁻")
            print("-> CH₃COO⁻ confirmed: Vinegar smell")
            print_reaction_explanation("CH₃COO⁻")
    
    return detected

def test_group_ii():
    """Test for Group II anions (Cl⁻, Br⁻, I⁻, NO₃⁻)"""
    detected = []
    print("\n=== GROUP II: Conc. H₂SO₄ Tests ===")
    
    if get_user_input("Add conc. H₂SO₄. Colored fumes observed? (y/n): ", ['y', 'n']) == 'y':
        fume_color = get_user_input("Fume color (white/yellow/violet/brown): ",
                                  ['white', 'yellow', 'violet', 'brown'])
        
        if fume_color == "white":
            if get_user_input("Add AgNO₃. White precipitate soluble in NH₄OH? (y/n): ", ['y', 'n']) == 'y':
                detected.append("Cl⁻")
                print("-> Cl⁻ confirmed: White fumes and soluble precipitate")
                print_reaction_explanation("Cl⁻")
        
        elif fume_color == "yellow":
            if get_user_input("Add AgNO₃. Pale yellow precipitate? (y/n): ", ['y', 'n']) == 'y':
                detected.append("Br⁻")
                print("-> Br⁻ confirmed: Yellow fumes and precipitate")
                print_reaction_explanation("Br⁻")
        
        elif fume_color == "violet":
            if get_user_input("Add AgNO₃. Yellow precipitate insoluble in NH₄OH? (y/n): ", ['y', 'n']) == 'y':
                detected.append("I⁻")
                print("-> I⁻ confirmed: Violet fumes and insoluble precipitate")
                print_reaction_explanation("I⁻")
        
        elif fume_color == "brown":
            if get_user_input("Perform brown ring test (FeSO₄ + H₂SO₄). Ring formed? (y/n): ", ['y', 'n']) == 'y':
                detected.append("NO₃⁻")
                print("-> NO₃⁻ confirmed: Brown ring test positive")
                print_reaction_explanation("NO₃⁻")
    
    return detected

def test_group_iii():
    """Test for Group III anions (SO₄²⁻, PO₄³⁻, BO₃³⁻)"""
    detected = []
    print("\n=== GROUP III: Specific Tests ===")
    
    # Sulfate test
    if get_user_input("Add BaCl₂ to solution. White precipitate? (y/n): ", ['y', 'n']) == 'y':
        if get_user_input("Add dilute HCl. Precipitate insoluble? (y/n): ", ['y', 'n']) == 'y':
            detected.append("SO₄²⁻")
            print("-> SO₄²⁻ confirmed: Acid-insoluble white precipitate")
            print_reaction_explanation("SO₄²⁻")
    
    # Phosphate test
    if get_user_input("Add ammonium molybdate + HNO₃. Yellow precipitate? (y/n): ", ['y', 'n']) == 'y':
        detected.append("PO₄³⁻")
        print("-> PO₄³⁻ confirmed: Yellow ammonium phosphomolybdate")
        print_reaction_explanation("PO₄³⁻")
    
    # Borate test
    if get_user_input("Perform flame test (ethanol + H₂SO₄). Green flame? (y/n): ", ['y', 'n']) == 'y':
        detected.append("BO₃³⁻")
        print("-> BO₃³⁻ confirmed: Green flame test")
        print_reaction_explanation("BO₃³⁻")
    
    return detected

# ======================
# MAIN PROGRAM
# ======================

def main():
    print("\n===== QUALITATIVE ANION ANALYSIS =====")
    print("Systematic analysis of anions from Group I to Group III\n")
    
    detected_anions = []
    
    # Perform all group tests in order
    detected_anions.extend(test_group_i())
    detected_anions.extend(test_group_ii())
    detected_anions.extend(test_group_iii())
    
    # Display final results
    print("\n=== FINAL RESULTS ===")
    if detected_anions:
        unique_anions = sorted(set(detected_anions))
        print("Detected anions:", ", ".join(unique_anions))
        
        # Print summary of all detected anions
        print("\n=== SUMMARY OF DETECTED ANIONS ===")
        for anion in unique_anions:
            print(f"\n{anion}:")
            print(f"Test Method: {ANION_REACTIONS[anion]['test']}")
            print(f"Reaction: {ANION_REACTIONS[anion]['reaction']}")
    else:
        print("No anions detected.")

if __name__ == "__main__":
    main()