# ======================
# CHEMICAL REACTION DATA
# ======================

CATION_REACTIONS = {
    # Group I (HCl Group)
    "Pb²⁺": {
        "test": "Hot water + K₂CrO₄",
        "reaction": "Pb²⁺ + CrO₄²⁻ → PbCrO₄↓ (yellow)",
        "reason": "Forms insoluble lead chromate (Ksp = 2.8×10⁻¹³)"
    },
    "Ag⁺": {
        "test": "NH₄OH dissolution + HNO₃",
        "reaction": "AgCl + 2NH₃ → [Ag(NH₃)₂]⁺ (soluble complex)",
        "reason": "Forms diamminesilver(I) complex (Kf = 1.1×10⁷)"
    },
    "Hg₂²⁺": {
        "test": "Black residue with NH₄OH",
        "reaction": "Hg₂Cl₂ + 2NH₃ → Hg↓ + HgNH₂Cl↓ + NH₄⁺",
        "reason": "Disproportionation reaction"
    },

    # Group II (H₂S Acidic Group)
    "Cu²⁺": {
        "test": "NH₄OH deep blue solution",
        "reaction": "Cu²⁺ + 4NH₃ → [Cu(NH₃)₄]²⁺",
        "reason": "Forms tetraamminecopper(II) complex (λmax ≈ 600 nm)"
    },
    "Pb²⁺": {
        "test": "K₂CrO₄ yellow precipitate",
        "reaction": "Pb²⁺ + CrO₄²⁻ → PbCrO₄↓",
        "reason": "Confirmatory test after Group I separation"
    },
    "Bi³⁺": {
        "test": "SnCl₂ reduction",
        "reaction": "2Bi³⁺ + 3Sn²⁺ → 2Bi↓ + 3Sn⁴⁺",
        "reason": "Redox reaction (E° = 0.32V for Bi³⁺/Bi)"
    },
    "As³⁺/⁵⁺": {
        "test": "(NH₄)₂Sx dissolution",
        "reaction": "As₂S₃ + 3S²⁻ → 2AsS₃³⁻",
        "reason": "Forms soluble thioarsenite complex"
    },

    # Group III (NH₄OH/NH₄Cl Group)
    "Fe³⁺": {
        "test": "K₄[Fe(CN)₆]",
        "reaction": "4Fe³⁺ + 3[Fe(CN)₆]⁴⁻ → Fe₄[Fe(CN)₆]₃↓ (Prussian blue)",
        "reason": "Mixed-valence iron cyanide complex"
    },
    "Al³⁺": {
        "test": "Aluminon reagent",
        "reaction": "Al³⁺ + aluminon → red lake complex",
        "reason": "Chelation with aurintricarboxylic acid"
    },
    "Cr³⁺": {
        "test": "NaOH/H₂O₂ + Pb(OAc)₂",
        "reaction": "Cr³⁺ → CrO₄²⁻ → PbCrO₄↓ (yellow)",
        "reason": "Oxidation to chromate followed by precipitation"
    },

    # Group IV (H₂S Basic Group)
    "Zn²⁺": {
        "test": "NaOH solubility",
        "reaction": "Zn²⁺ + 2OH⁻ → Zn(OH)₂↓ → [Zn(OH)₄]²⁻",
        "reason": "Amphoteric behavior"
    },
    "Mn²⁺": {
        "test": "NaBiO₃ oxidation",
        "reaction": "2Mn²⁺ + 5NaBiO₃ + 14H⁺ → 2MnO₄⁻ + 5Bi³⁺ + 5Na⁺ + 7H₂O",
        "reason": "Oxidation to purple permanganate"
    },
    "Ni²⁺": {
        "test": "Dimethylglyoxime",
        "reaction": "Ni²⁺ + 2dmgH → [Ni(dmg)₂]↓ (red)",
        "reason": "Square planar chelate complex"
    },
    "Co²⁺": {
        "test": "NH₄SCN complex",
        "reaction": "Co²⁺ + 4SCN⁻ → [Co(SCN)₄]²⁻ (blue)",
        "reason": "Tetrahedral thiocyanate complex"
    },

    # Group V ((NH₄)₂CO₃ Group)
    "Ba²⁺": {
        "test": "Flame test (green)",
        "reaction": "Ba²⁺ → Ba* (excited state)",
        "reason": "Emission at 524 nm (green)"
    },
    "Sr²⁺": {
        "test": "Flame test (crimson)",
        "reaction": "Sr²⁺ → Sr* (excited state)",
        "reason": "Emission at 650-680 nm (red)"
    },
    "Ca²⁺": {
        "test": "Flame test (brick-red)",
        "reaction": "Ca²⁺ → Ca* (excited state)",
        "reason": "Emission at 622 nm (orange-red)"
    },

    # Group VI (Soluble Group)
    "NH₄⁺": {
        "test": "NaOH + heat",
        "reaction": "NH₄⁺ + OH⁻ → NH₃↑ + H₂O",
        "reason": "Ammonia gas detection"
    },
    "Mg²⁺": {
        "test": "Magneson reagent",
        "reaction": "Mg²⁺ + magneson → blue lake complex",
        "reason": "Adsorption indicator reaction"
    },
    "Na⁺": {
        "test": "Flame test (yellow)",
        "reaction": "Na⁺ → Na* (excited state)",
        "reason": "Emission at 589 nm (D-line)"
    },
    "K⁺": {
        "test": "Flame test (violet)",
        "reaction": "K⁺ → K* (excited state)",
        "reason": "Emission at 766/770 nm"
    }
}

# ======================
# CORE FUNCTIONS
# ======================

def print_reaction_explanation(ion):
    """Display detailed chemical explanation for detected ion"""
    if ion in CATION_REACTIONS:
        print(f"\nReaction Details for {ion}:")
        print(f"Test Method: {CATION_REACTIONS[ion]['test']}")
        print(f"Chemical Equation: {CATION_REACTIONS[ion]['reaction']}")
        print(f"Scientific Principle: {CATION_REACTIONS[ion]['reason']}")
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
    """Test for Group I cations (Pb²⁺, Ag⁺, Hg₂²⁺)"""
    detected = []
    print("\n=== GROUP I: Dilute HCl Test ===")
    
    if get_user_input("Did a precipitate form with dilute HCl? (y/n): ", ['y', 'n']) == 'y':
        print("\nPerforming confirmatory tests...")
        
        # Test for Lead
        if get_user_input("Does precipitate dissolve in hot water? (y/n): ", ['y', 'n']) == 'y':
            detected.append("Pb²⁺")
            print("-> Pb²⁺ confirmed: Yellow precipitate with K₂CrO₄")
            print_reaction_explanation("Pb²⁺")
            
            # Test remaining precipitate
            if get_user_input("To residue, add NH₄OH. Dissolves? (y/n): ", ['y', 'n']) == 'y':
                detected.append("Ag⁺")
                print("-> Ag⁺ confirmed: White precipitate with HNO₃")
                print_reaction_explanation("Ag⁺")
            else:
                detected.append("Hg₂²⁺")
                print("-> Hg₂²⁺ confirmed: Black residue")
                print_reaction_explanation("Hg₂²⁺")
        
        else:  # No lead present
            if get_user_input("Add NH₄OH to precipitate. Dissolves? (y/n): ", ['y', 'n']) == 'y':
                detected.append("Ag⁺")
                print("-> Ag⁺ confirmed: White precipitate with HNO₃")
                print_reaction_explanation("Ag⁺")
            else:
                detected.append("Hg₂²⁺")
                print("-> Hg₂²⁺ confirmed: Black residue")
                print_reaction_explanation("Hg₂²⁺")
    
    return detected

def test_group_ii():
    """Test for Group II cations (Cu²⁺, Pb²⁺, Bi³⁺, As³⁺/⁵⁺)"""
    detected = []
    print("\n=== GROUP II: H₂S in Acidic Medium ===")
    
    if get_user_input("Did a precipitate form after passing H₂S in acidic solution? (y/n): ", ['y', 'n']) == 'y':
        print("\nPerforming confirmatory tests...")
        
        # Test for Arsenic
        if get_user_input("Treat with (NH₄)₂Sx. Dissolves? (y/n): ", ['y', 'n']) == 'y':
            detected.append("As³⁺/⁵⁺")
            print("-> As confirmed: Yellow precipitate with HNO₃")
            print_reaction_explanation("As³⁺/⁵⁺")
        
        # Test for Copper
        if get_user_input("Add NH₄OH. Deep blue solution? (y/n): ", ['y', 'n']) == 'y':
            detected.append("Cu²⁺")
            print("-> Cu²⁺ confirmed: Deep blue solution")
            print_reaction_explanation("Cu²⁺")
        
        # Test for Bismuth
        if get_user_input("Add SnCl₂. Black precipitate? (y/n): ", ['y', 'n']) == 'y':
            detected.append("Bi³⁺")
            print("-> Bi³⁺ confirmed: Black precipitate")
            print_reaction_explanation("Bi³⁺")
        
        # Test for Lead (if not already detected in Group I)
        if "Pb²⁺" not in detected and get_user_input("Dissolve in HNO₃ + K₂CrO₄. Yellow precipitate? (y/n): ", ['y', 'n']) == 'y':
            detected.append("Pb²⁺")
            print("-> Pb²⁺ confirmed: Yellow precipitate")
            print_reaction_explanation("Pb²⁺")
    
    return detected

def test_group_iii():
    """Test for Group III cations (Fe³⁺, Al³⁺, Cr³⁺)"""
    detected = []
    print("\n=== GROUP III: NH₄OH/NH₄Cl ===")
    
    if get_user_input("Did a precipitate form after adding NH₄OH/NH₄Cl? (y/n): ", ['y', 'n']) == 'y':
        print("\nPerforming confirmatory tests...")
        
        # Test for Iron
        if get_user_input("Add K₄[Fe(CN)₆]. Blue precipitate? (y/n): ", ['y', 'n']) == 'y':
            detected.append("Fe³⁺")
            print("-> Fe³⁺ confirmed: Prussian blue precipitate")
            print_reaction_explanation("Fe³⁺")
        
        # Test for Aluminum
        if get_user_input("Add aluminon + NH₄OH. Red precipitate? (y/n): ", ['y', 'n']) == 'y':
            detected.append("Al³⁺")
            print("-> Al³⁺ confirmed: Red lake precipitate")
            print_reaction_explanation("Al³⁺")
        
        # Test for Chromium
        if get_user_input("Boil with NaOH/H₂O₂, add CH₃COOH + Pb(OAc)₂. Yellow? (y/n): ", ['y', 'n']) == 'y':
            detected.append("Cr³⁺")
            print("-> Cr³⁺ confirmed: Yellow PbCrO₄ precipitate")
            print_reaction_explanation("Cr³⁺")
    
    return detected

def test_group_iv():
    """Test for Group IV cations (Zn²⁺, Mn²⁺, Ni²⁺, Co²⁺)"""
    detected = []
    print("\n=== GROUP IV: H₂S in Basic Medium ===")
    
    if get_user_input("Did a precipitate form after passing H₂S in basic solution? (y/n): ", ['y', 'n']) == 'y':
        print("\nPerforming confirmatory tests...")
        
        # Test for Zinc
        if get_user_input("Add NaOH. White precipitate soluble in excess? (y/n): ", ['y', 'n']) == 'y':
            detected.append("Zn²⁺")
            print("-> Zn²⁺ confirmed: Amphoteric behavior")
            print_reaction_explanation("Zn²⁺")
        
        # Test for Manganese
        if get_user_input("Add HNO₃ + NaBiO₃. Purple solution? (y/n): ", ['y', 'n']) == 'y':
            detected.append("Mn²⁺")
            print("-> Mn²⁺ confirmed: MnO₄⁻ formation")
            print_reaction_explanation("Mn²⁺")
        
        # Test for Nickel
        if get_user_input("Add dimethylglyoxime. Red precipitate? (y/n): ", ['y', 'n']) == 'y':
            detected.append("Ni²⁺")
            print("-> Ni²⁺ confirmed: Nickel-dimethylglyoxime complex")
            print_reaction_explanation("Ni²⁺")
        
        # Test for Cobalt
        if get_user_input("Add NH₄SCN. Blue complex? (y/n): ", ['y', 'n']) == 'y':
            detected.append("Co²⁺")
            print("-> Co²⁺ confirmed: [Co(SCN)₄]²⁻ complex")
            print_reaction_explanation("Co²⁺")
    
    return detected

def test_group_v():
    """Test for Group V cations (Ba²⁺, Sr²⁺, Ca²⁺)"""
    detected = []
    print("\n=== GROUP V: (NH₄)₂CO₃ ===")
    
    if get_user_input("Did a precipitate form after adding (NH₄)₂CO₃? (y/n): ", ['y', 'n']) == 'y':
        print("\nPerforming flame tests...")
        flame = get_user_input("Flame test color (green/crimson/brick-red/none): ", 
                             ['green', 'crimson', 'brick-red', 'none'])
        
        if flame == "green":
            detected.append("Ba²⁺")
            print("-> Ba²⁺ confirmed: Green flame")
            print_reaction_explanation("Ba²⁺")
        elif flame == "crimson":
            detected.append("Sr²⁺")
            print("-> Sr²⁺ confirmed: Crimson flame")
            print_reaction_explanation("Sr²⁺")
        elif flame == "brick-red":
            detected.append("Ca²⁺")
            print("-> Ca²⁺ confirmed: Brick-red flame")
            print_reaction_explanation("Ca²⁺")
    
    return detected

def test_group_vi():
    """Test for Group VI cations (NH₄⁺, Mg²⁺, Na⁺, K⁺)"""
    detected = []
    print("\n=== GROUP VI: Soluble Group ===")
    
    # Ammonium test
    if get_user_input("Add NaOH + heat. Ammonia smell? (y/n): ", ['y', 'n']) == 'y':
        detected.append("NH₄⁺")
        print("-> NH₄⁺ confirmed: Ammonia gas detected")
        print_reaction_explanation("NH₄⁺")
    
    # Magnesium test
    if get_user_input("Add magneson reagent. Blue precipitate? (y/n): ", ['y', 'n']) == 'y':
        detected.append("Mg²⁺")
        print("-> Mg²⁺ confirmed: Blue lake complex")
        print_reaction_explanation("Mg²⁺")
    
    # Flame tests
    flame = get_user_input("Flame test through cobalt glass (yellow/violet/none): ", 
                         ['yellow', 'violet', 'none'])
    if flame == "yellow":
        detected.append("Na⁺")
        print("-> Na⁺ confirmed: Yellow flame")
        print_reaction_explanation("Na⁺")
    elif flame == "violet":
        detected.append("K⁺")
        print("-> K⁺ confirmed: Violet flame")
        print_reaction_explanation("K⁺")
    
    return detected

# ======================
# MAIN PROGRAM
# ======================

def main():
    print("\n===== QUALITATIVE CATION ANALYSIS =====")
    print("Systematic analysis of cations from Group I to Group VI\n")
    
    detected_cations = []
    
    # Perform all group tests in order
    detected_cations.extend(test_group_i())
    detected_cations.extend(test_group_ii())
    detected_cations.extend(test_group_iii())
    detected_cations.extend(test_group_iv())
    detected_cations.extend(test_group_v())
    detected_cations.extend(test_group_vi())
    
    # Display final results
    print("\n=== FINAL RESULTS ===")
    if detected_cations:
        unique_cations = sorted(set(detected_cations))
        print("Detected cations:", ", ".join(unique_cations))
        
        # Print summary of all detected cations
        print("\n=== SUMMARY OF DETECTED CATIONS ===")
        for cation in unique_cations:
            print(f"\n{cation}:")
            print(f"Test Method: {CATION_REACTIONS[cation]['test']}")
            print(f"Reaction: {CATION_REACTIONS[cation]['reaction']}")
    else:
        print("No cations detected.")

if __name__ == "__main__":
    main()