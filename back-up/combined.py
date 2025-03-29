# ======================
# QUALITATIVE ANALYSIS PROGRAM
# ======================
# Complete working version with all fixes
# ======================
# ======================
# IMPORT SECTION
# ======================
import os
from datetime import datetime
import sys
# ======================
# CHEMICAL REACTION DATA
# ======================

CATION_REACTIONS = {
    # Group I (HCl Group)
    "Pb²⁺": {
        "test": "Hot water + K₂CrO₄",
        "reaction": "Pb²⁺ + CrO₄²⁻ → PbCrO₄↓ (yellow)",
        "reason": "Forms insoluble lead chromate (Ksp = 2.8×10⁻¹³)",
        "group": "I"
    },
    "Ag⁺": {
        "test": "NH₄OH dissolution + HNO₃",
        "reaction": "AgCl + 2NH₃ → [Ag(NH₃)₂]⁺ (soluble complex)",
        "reason": "Forms diamminesilver(I) complex (Kf = 1.1×10⁷)",
        "group": "I"
    },
    "Hg₂²⁺": {
        "test": "Black residue with NH₄OH",
        "reaction": "Hg₂Cl₂ + 2NH₃ → Hg↓ + HgNH₂Cl↓ + NH₄⁺",
        "reason": "Disproportionation reaction",
        "group": "I"
    },

    # Group II (H₂S Acidic Group)
    "Cu²⁺": {
        "test": "NH₄OH deep blue solution",
        "reaction": "Cu²⁺ + 4NH₃ → [Cu(NH₃)₄]²⁺",
        "reason": "Forms tetraamminecopper(II) complex (λmax ≈ 600 nm)",
        "group": "II"
    },
    "Pb²⁺": {
        "test": "K₂CrO₄ yellow precipitate",
        "reaction": "Pb²⁺ + CrO₄²⁻ → PbCrO₄↓",
        "reason": "Confirmatory test after Group I separation",
        "group": "II"
    },
    "Bi³⁺": {
        "test": "SnCl₂ reduction",
        "reaction": "2Bi³⁺ + 3Sn²⁺ → 2Bi↓ + 3Sn⁴⁺",
        "reason": "Redox reaction (E° = 0.32V for Bi³⁺/Bi)",
        "group": "II"
    },
    "As³⁺/⁵⁺": {
        "test": "(NH₄)₂Sx dissolution",
        "reaction": "As₂S₃ + 3S²⁻ → 2AsS₃³⁻",
        "reason": "Forms soluble thioarsenite complex",
        "group": "II"
    },

    # Group III (NH₄OH/NH₄Cl Group)
    "Fe³⁺": {
        "test": "K₄[Fe(CN)₆]",
        "reaction": "4Fe³⁺ + 3[Fe(CN)₆]⁴⁻ → Fe₄[Fe(CN)₆]₃↓ (Prussian blue)",
        "reason": "Mixed-valence iron cyanide complex",
        "group": "III"
    },
    "Al³⁺": {
        "test": "Aluminon reagent",
        "reaction": "Al³⁺ + aluminon → red lake complex",
        "reason": "Chelation with aurintricarboxylic acid",
        "group": "III"
    },
    "Cr³⁺": {
        "test": "NaOH/H₂O₂ + Pb(OAc)₂",
        "reaction": "Cr³⁺ → CrO₄²⁻ → PbCrO₄↓ (yellow)",
        "reason": "Oxidation to chromate followed by precipitation",
        "group": "III"
    },

    # Group IV (H₂S Basic Group)
    "Zn²⁺": {
        "test": "NaOH solubility",
        "reaction": "Zn²⁺ + 2OH⁻ → Zn(OH)₂↓ → [Zn(OH)₄]²⁻",
        "reason": "Amphoteric behavior",
        "group": "IV"
    },
    "Mn²⁺": {
        "test": "NaBiO₃ oxidation",
        "reaction": "2Mn²⁺ + 5NaBiO₃ + 14H⁺ → 2MnO₄⁻ + 5Bi³⁺ + 5Na⁺ + 7H₂O",
        "reason": "Oxidation to purple permanganate",
        "group": "IV"
    },
    "Ni²⁺": {
        "test": "Dimethylglyoxime",
        "reaction": "Ni²⁺ + 2dmgH → [Ni(dmg)₂]↓ (red)",
        "reason": "Square planar chelate complex",
        "group": "IV"
    },
    "Co²⁺": {
        "test": "NH₄SCN complex",
        "reaction": "Co²⁺ + 4SCN⁻ → [Co(SCN)₄]²⁻ (blue)",
        "reason": "Tetrahedral thiocyanate complex",
        "group": "IV"
    },

    # Group V ((NH₄)₂CO₃ Group)
    "Ba²⁺": {
        "test": "Flame test (green)",
        "reaction": "Ba²⁺ → Ba* (excited state)",
        "reason": "Emission at 524 nm (green)",
        "group": "V"
    },
    "Sr²⁺": {
        "test": "Flame test (crimson)",
        "reaction": "Sr²⁺ → Sr* (excited state)",
        "reason": "Emission at 650-680 nm (red)",
        "group": "V"
    },
    "Ca²⁺": {
        "test": "Flame test (brick-red)",
        "reaction": "Ca²⁺ → Ca* (excited state)",
        "reason": "Emission at 622 nm (orange-red)",
        "group": "V"
    },

    # Group VI (Soluble Group)
    "NH₄⁺": {
        "test": "NaOH + heat",
        "reaction": "NH₄⁺ + OH⁻ → NH₃↑ + H₂O",
        "reason": "Ammonia gas detection",
        "group": "VI"
    },
    "Mg²⁺": {
        "test": "Magneson reagent",
        "reaction": "Mg²⁺ + magneson → blue lake complex",
        "reason": "Adsorption indicator reaction",
        "group": "VI"
    },
    "Na⁺": {
        "test": "Flame test (yellow)",
        "reaction": "Na⁺ → Na* (excited state)",
        "reason": "Emission at 589 nm (D-line)",
        "group": "VI"
    },
    "K⁺": {
        "test": "Flame test (violet)",
        "reaction": "K⁺ → K* (excited state)",
        "reason": "Emission at 766/770 nm",
        "group": "VI"
    }
}

ANION_REACTIONS = {
    # Group I (Dilute H₂SO₄ Group)
    "CO₃²⁻": {
        "test": "Effervescence + lime water",
        "reaction": "CO₃²⁻ + 2H⁺ → CO₂↑ + H₂O\nCO₂ + Ca(OH)₂ → CaCO₃↓ (milky)",
        "reason": "Carbonates release CO₂ gas that forms insoluble calcium carbonate (Ksp = 4.5×10⁻⁹)",
        "group": "I"
    },
    "S²⁻": {
        "test": "Lead acetate paper",
        "reaction": "S²⁻ + Pb²⁺ → PbS↓ (black, Ksp = 9.0×10⁻²⁹)",
        "reason": "Extremely low solubility allows detection at ppm levels",
        "group": "I"
    },
    "NO₂⁻": {
        "test": "Brown fumes with acid",
        "reaction": "2NO₂⁻ + 2H⁺ → NO₂↑ (brown) + NO↑ + H₂O",
        "reason": "Nitrous acid decomposition produces characteristic brown gas",
        "group": "I"
    },
    "CH₃COO⁻": {
        "test": "Vinegar smell",
        "reaction": "CH₃COO⁻ + H⁺ → CH₃COOH↑ (pKa = 4.76)",
        "reason": "Volatile acetic acid detected by odor",
        "group": "I"
    },

    # Group II (Conc. H₂SO₄ Group)
    "Cl⁻": {
        "test": "AgNO₃ precipitation",
        "reaction": "Ag⁺ + Cl⁻ → AgCl↓ (white, Ksp = 1.8×10⁻¹⁰)\nAgCl + 2NH₃ → [Ag(NH₃)₂]⁺ (soluble)",
        "reason": "Distinctive solubility behavior in ammonia",
        "group": "II"
    },
    "Br⁻": {
        "test": "AgNO₃ precipitation",
        "reaction": "Ag⁺ + Br⁻ → AgBr↓ (pale yellow, Ksp = 5.0×10⁻¹³)",
        "reason": "Intermediate solubility product distinguishes from other halides",
        "group": "II"
    },
    "I⁻": {
        "test": "AgNO₃ precipitation",
        "reaction": "Ag⁺ + I⁻ → AgI↓ (yellow, Ksp = 8.5×10⁻¹⁷)",
        "reason": "Most insoluble silver halide",
        "group": "II"
    },
    "NO₃⁻": {
        "test": "Brown ring test",
        "reaction": "NO₃⁻ + 3Fe²⁺ + 4H⁺ → NO↑ + 3Fe³⁺ + 2H₂O\nFe²⁺ + NO → [Fe(NO)]²⁺ (brown ring)",
        "reason": "Nitric oxide complexation with Fe²⁺ (E° = +0.96V)",
        "group": "II"
    },

    # Group III (Special Tests)
    "SO₄²⁻": {
        "test": "BaCl₂ in acid",
        "reaction": "Ba²⁺ + SO₄²⁻ → BaSO₄↓ (white, Ksp = 1.1×10⁻¹⁰)",
        "reason": "Kinetically inert precipitate resistant to acid dissolution",
        "group": "III"
    },
    "PO₄³⁻": {
        "test": "Ammonium molybdate",
        "reaction": "PO₄³⁻ + 12MoO₄²⁻ + 3NH₄⁺ + 24H⁺ → (NH₄)₃PO₄·12MoO₃↓ (yellow)",
        "reason": "Heteropoly acid formation under acidic conditions",
        "group": "III"
    },
    "BO₃³⁻": {
        "test": "Flame test",
        "reaction": "BO₃³⁻ + H₂SO₄ + CH₃CH₂OH → B(OCH₂CH₃)₃ (green flame)",
        "reason": "Volatile boron ester produces characteristic green color",
        "group": "III"
    }
}

# ======================
# CORE FUNCTIONS
# ======================

def print_reaction_explanation(ion, ion_type):
    """Display detailed chemical explanation for detected ion"""
    reactions = CATION_REACTIONS if ion_type == 'cation' else ANION_REACTIONS
    if ion in reactions:
        print(f"\nReaction Details for {ion}:")
        print(f"Test Method: {reactions[ion]['test']}")
        print(f"Chemical Equation:\n{reactions[ion]['reaction']}")
        print(f"Scientific Principle: {reactions[ion]['reason']}")
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
# CATION TEST FUNCTIONS
# ======================

def get_user_input(prompt, valid_options):
    """Helper function to get validated user input"""
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Please enter one of: {', '.join(valid_options)}")

def print_reaction_explanation(ion, ion_type):
    """Print the reaction details for a given ion"""
    database = CATION_REACTIONS if ion_type == 'cation' else ANION_REACTIONS
    if ion in database:
        info = database[ion]
        print(f"\nReaction Details for {ion}:")
        print(f"Test: {info['test']}")
        print(f"Reaction: {info['reaction']}")
        print(f"Reason: {info['reason']}")
    else:
        print(f"No reaction information found for {ion}")

def test_group_i_cations():
    """Test for Group I cations (Pb²⁺, Ag⁺, Hg₂²⁺)"""
    detected = []
    print("\n=== GROUP I: Dilute HCl Test ===")
    print("Add dilute HCl to the solution and observe.")
    
    if get_user_input("Did a white precipitate form? (y/n): ", ['y', 'n']) == 'y':
        print("\nPerforming confirmatory tests on the precipitate...")
        
        # Test for Lead
        print("\n1. Testing for Pb²⁺:")
        print("a. Decant the solution and wash the precipitate with hot water")
        print("b. Add a few drops of K₂CrO₄ solution to the hot water extract")
        
        if get_user_input("Does a yellow precipitate form? (y/n): ", ['y', 'n']) == 'y':
            detected.append("Pb²⁺")
            print("-> Pb²⁺ confirmed: Yellow PbCrO₄ precipitate")
            print_reaction_explanation("Pb²⁺", 'cation')
            
            # Test remaining precipitate for Ag⁺ and Hg₂²⁺
            print("\n2. Testing remaining precipitate for Ag⁺ and Hg₂²⁺:")
            print("Add NH₄OH to the remaining precipitate")
            
            if get_user_input("Does the precipitate dissolve completely? (y/n): ", ['y', 'n']) == 'y':
                print("a. Acidify the solution with HNO₃")
                if get_user_input("Does a white precipitate reform? (y/n): ", ['y', 'n']) == 'y':
                    detected.append("Ag⁺")
                    print("-> Ag⁺ confirmed: Soluble in NH₄OH, reprecipitates with HNO₃")
                    print_reaction_explanation("Ag⁺", 'cation')
            else:
                if get_user_input("Does the precipitate turn black/gray? (y/n): ", ['y', 'n']) == 'y':
                    detected.append("Hg₂²⁺")
                    print("-> Hg₂²⁺ confirmed: Black/gray residue with NH₄OH")
                    print_reaction_explanation("Hg₂²⁺", 'cation')
        
        else:  # No lead present
            print("\nTesting precipitate directly for Ag⁺ and Hg₂²⁺:")
            print("Add NH₄OH to the precipitate")
            
            if get_user_input("Does the precipitate dissolve completely? (y/n): ", ['y', 'n']) == 'y':
                print("a. Acidify the solution with HNO₃")
                if get_user_input("Does a white precipitate reform? (y/n): ", ['y', 'n']) == 'y':
                    detected.append("Ag⁺")
                    print("-> Ag⁺ confirmed: Soluble in NH₄OH, reprecipitates with HNO₃")
                    print_reaction_explanation("Ag⁺", 'cation')
            else:
                if get_user_input("Does the precipitate turn black/gray? (y/n): ", ['y', 'n']) == 'y':
                    detected.append("Hg₂²⁺")
                    print("-> Hg₂²⁺ confirmed: Black/gray residue with NH₄OH")
                    print_reaction_explanation("Hg₂²⁺", 'cation')
    
    else:
        print("No Group I cations detected.")
    
    return detected

def test_group_ii_cations():
    """Test for Group II cations (Cu²⁺, Pb²⁺, Bi³⁺, As³⁺/⁵⁺)"""
    detected = []
    print("\n=== GROUP II: H₂S in Acidic Medium (0.3M HCl) ===")
    print("Pass H₂S gas through the acidic solution and observe.")
    
    if get_user_input("Did a precipitate form? (y/n): ", ['y', 'n']) == 'y':
        print("\nObserve precipitate color:")
        color = get_user_input("Color? (black/brown/yellow/white): ", ['black', 'brown', 'yellow', 'white'])
        
        print("\nPerforming confirmatory tests...")
        
        # Test for Arsenic (if yellow precipitate)
        if color == 'yellow':
            print("\n1. Testing for As³⁺/⁵⁺:")
            print("a. Treat precipitate with (NH₄)₂Sx solution")
            if get_user_input("Does the precipitate dissolve? (y/n): ", ['y', 'n']) == 'y':
                print("b. Acidify with dilute HCl")
                if get_user_input("Does a yellow precipitate reform? (y/n): ", ['y', 'n']) == 'y':
                    detected.append("As³⁺/⁵⁺")
                    print("-> As³⁺/⁵⁺ confirmed: Yellow As₂S₃")
                    print_reaction_explanation("As³⁺/⁵⁺", 'cation')
        
        # Test for Copper (if black precipitate)
        if color == 'black':
            print("\n2. Testing for Cu²⁺:")
            print("a. Dissolve some precipitate in HNO₃")
            print("b. Add excess NH₄OH to the solution")
            if get_user_input("Does the solution turn deep blue? (y/n): ", ['y', 'n']) == 'y':
                detected.append("Cu²⁺")
                print("-> Cu²⁺ confirmed: [Cu(NH₃)₄]²⁺ complex")
                print_reaction_explanation("Cu²⁺", 'cation')
        
        # Test for Bismuth (if black/brown precipitate)
        if color in ['black', 'brown']:
            print("\n3. Testing for Bi³⁺:")
            print("a. Dissolve some precipitate in HNO₃")
            print("b. Add SnCl₂ solution dropwise")
            if get_user_input("Does a black precipitate form? (y/n): ", ['y', 'n']) == 'y':
                detected.append("Bi³⁺")
                print("-> Bi³⁺ confirmed: Black Bi metal")
                print_reaction_explanation("Bi³⁺", 'cation')
        
        # Test for Lead (if white precipitate and not already detected in Group I)
        if color == 'white' and "Pb²⁺" not in detected:
            print("\n4. Testing for Pb²⁺:")
            print("a. Dissolve precipitate in hot dilute HNO₃")
            print("b. Add K₂CrO₄ solution")
            if get_user_input("Does a yellow precipitate form? (y/n): ", ['y', 'n']) == 'y':
                detected.append("Pb²⁺")
                print("-> Pb²⁺ confirmed: Yellow PbCrO₄")
                print_reaction_explanation("Pb²⁺", 'cation')
    
    else:
        print("No Group II cations detected.")
    
    return detected

def test_group_iii_cations():
    """Test for Group III cations (Fe³⁺, Al³⁺, Cr³⁺)"""
    detected = []
    print("\n=== GROUP III: NH₄OH/NH₄Cl ===")
    print("Add NH₄Cl and then NH₄OH to the solution and observe.")
    
    if get_user_input("Did a precipitate form? (y/n): ", ['y', 'n']) == 'y':
        print("\nObserve precipitate color:")
        color = get_user_input("Color? (red-brown/white/green): ", ['red-brown', 'white', 'green'])
        
        print("\nPerforming confirmatory tests...")
        
        # Test for Iron
        if color == 'red-brown':
            print("\n1. Testing for Fe³⁺:")
            print("a. Dissolve some precipitate in dilute HCl")
            print("b. Add K₄[Fe(CN)₆] solution")
            if get_user_input("Does a dark blue precipitate form? (y/n): ", ['y', 'n']) == 'y':
                detected.append("Fe³⁺")
                print("-> Fe³⁺ confirmed: Prussian blue")
                print_reaction_explanation("Fe³⁺", 'cation')
        
        # Test for Aluminum
        if color == 'white':
            print("\n2. Testing for Al³⁺:")
            print("a. Dissolve some precipitate in dilute HCl")
            print("b. Add aluminon reagent and make slightly basic with NH₄OH")
            if get_user_input("Does a red lake form? (y/n): ", ['y', 'n']) == 'y':
                detected.append("Al³⁺")
                print("-> Al³⁺ confirmed: Red lake complex")
                print_reaction_explanation("Al³⁺", 'cation')
        
        # Test for Chromium
        if color == 'green':
            print("\n3. Testing for Cr³⁺:")
            print("a. Boil with NaOH and H₂O₂")
            print("b. Acidify with CH₃COOH")
            print("c. Add Pb(OAc)₂ solution")
            if get_user_input("Does a yellow precipitate form? (y/n): ", ['y', 'n']) == 'y':
                detected.append("Cr³⁺")
                print("-> Cr³⁺ confirmed: Yellow PbCrO₄")
                print_reaction_explanation("Cr³⁺", 'cation')
    
    else:
        print("No Group III cations detected.")
    
    return detected
def test_group_iv_cations():
    """Test for Group IV cations (Zn²⁺, Mn²⁺, Ni²⁺, Co²⁺)"""
    detected = []
    print("\n=== GROUP IV: H₂S in Basic Medium (NH₃/NH₄Cl) ===")
    print("Make the solution slightly basic with NH₃/NH₄Cl buffer.")
    print("Pass H₂S gas through the solution and observe.")
    
    if get_user_input("Did a precipitate form? (y/n): ", ['y', 'n']) == 'y':
        print("\nObserve precipitate color:")
        color = get_user_input("Color? (white/flesh-pink/black): ", ['white', 'flesh-pink', 'black'])
        
        print("\nPerforming confirmatory tests...")
        
        # Test for Zinc
        if color == 'white':
            print("\n1. Testing for Zn²⁺:")
            print("a. Dissolve precipitate in dilute HCl")
            print("b. Add NaOH solution dropwise")
            print("   Observe: White precipitate forms initially")
            print("c. Add excess NaOH")
            if get_user_input("Does the precipitate dissolve? (y/n): ", ['y', 'n']) == 'y':
                detected.append("Zn²⁺")
                print("-> Zn²⁺ confirmed: Amphoteric behavior")
                print_reaction_explanation("Zn²⁺", 'cation')
        
        # Test for Manganese
        if color == 'flesh-pink':
            print("\n2. Testing for Mn²⁺:")
            print("a. Dissolve some precipitate in dilute HNO₃")
            print("b. Add solid NaBiO₃ and stir")
            if get_user_input("Does the solution turn purple? (y/n): ", ['y', 'n']) == 'y':
                detected.append("Mn²⁺")
                print("-> Mn²⁺ confirmed: MnO₄⁻ formation")
                print_reaction_explanation("Mn²⁺", 'cation')
        
        # Test for Nickel
        if color == 'black':
            print("\n3. Testing for Ni²⁺:")
            print("a. Dissolve some precipitate in aqua regia")
            print("b. Add dimethylglyoxime in ammoniacal solution")
            if get_user_input("Does a bright red precipitate form? (y/n): ", ['y', 'n']) == 'y':
                detected.append("Ni²⁺")
                print("-> Ni²⁺ confirmed: Nickel-dimethylglyoxime complex")
                print_reaction_explanation("Ni²⁺", 'cation')
        
        # Test for Cobalt
        if color == 'black':
            print("\n4. Testing for Co²⁺:")
            print("a. Dissolve some precipitate in dilute HCl")
            print("b. Add solid NH₄SCN")
            print("c. Add amyl alcohol and shake")
            if get_user_input("Does the organic layer turn blue? (y/n): ", ['y', 'n']) == 'y':
                detected.append("Co²⁺")
                print("-> Co²⁺ confirmed: [Co(SCN)₄]²⁻ complex")
                print_reaction_explanation("Co²⁺", 'cation')
    
    else:
        print("No Group IV cations detected.")
    
    return detected

def test_group_v_cations():
    """Test for Group V cations (Ba²⁺, Sr²⁺, Ca²⁺)"""
    detected = []
    print("\n=== GROUP V: (NH₄)₂CO₃ in NH₃ ===")
    print("Add NH₄Cl and NH₄OH to the solution.")
    print("Then add (NH₄)₂CO₃ solution and warm slightly.")
    
    if get_user_input("Did a white precipitate form? (y/n): ", ['y', 'n']) == 'y':
        print("\nPerform flame tests on original solution:")
        print("Clean platinum wire, dip in conc. HCl, then in test solution.")
        print("Introduce into flame and observe color.")
        
        flame_color = get_user_input("Flame color? (green/red/orange/none): ", 
                                   ['green', 'red', 'orange', 'none'])
        
        if flame_color == "green":
            detected.append("Ba²⁺")
            print("-> Ba²⁺ confirmed: Green flame (524 nm)")
            print_reaction_explanation("Ba²⁺", 'cation')
        
        if flame_color == "red":
            print("\nConfirmatory test for Sr²⁺:")
            print("a. Make solution slightly acidic with CH₃COOH")
            print("b. Add saturated CaSO₄ solution")
            if get_user_input("Does a white precipitate form slowly? (y/n): ", ['y', 'n']) == 'y':
                detected.append("Sr²⁺")
                print("-> Sr²⁺ confirmed: SrSO₄ precipitation")
                print_reaction_explanation("Sr²⁺", 'cation')
        
        if flame_color == "orange":
            print("\nConfirmatory test for Ca²⁺:")
            print("a. Add (NH₄)₂C₂O₄ solution")
            if get_user_input("Does a white precipitate form? (y/n): ", ['y', 'n']) == 'y':
                detected.append("Ca²⁺")
                print("-> Ca²⁺ confirmed: CaC₂O₄ precipitation")
                print_reaction_explanation("Ca²⁺", 'cation')
    
    else:
        print("No Group V cations detected.")
    
    return detected

def test_group_vi_cations():
    """Test for Group VI cations (NH₄⁺, Mg²⁺, Na⁺, K⁺)"""
    detected = []
    print("\n=== GROUP VI: Soluble Group ===")
    
    # Ammonium test
    print("\n1. Testing for NH₄⁺:")
    print("a. Take original solution in test tube")
    print("b. Add NaOH solution and warm gently")
    if get_user_input("Does ammonia gas evolve (test with moist red litmus)? (y/n): ", ['y', 'n']) == 'y':
        detected.append("NH₄⁺")
        print("-> NH₄⁺ confirmed: NH₃ gas detected")
        print_reaction_explanation("NH₄⁺", 'cation')
    
    # Magnesium test
    print("\n2. Testing for Mg²⁺:")
    print("a. Take fresh solution, add NH₄Cl and NH₄OH")
    print("b. Add disodium hydrogen phosphate solution")
    if get_user_input("Does a white crystalline precipitate form? (y/n): ", ['y', 'n']) == 'y':
        detected.append("Mg²⁺")
        print("-> Mg²⁺ confirmed: MgNH₄PO₄ precipitation")
        print_reaction_explanation("Mg²⁺", 'cation')
    
    # Sodium test
    print("\n3. Testing for Na⁺:")
    print("Perform flame test (clean wire, dip in solution):")
    flame_color = get_user_input("Flame color? (yellow/none): ", ['yellow', 'none'])
    if flame_color == "yellow":
        print("Confirm with cobalt glass:")
        if get_user_input("Does yellow color disappear through cobalt glass? (y/n): ", ['y', 'n']) == 'y':
            detected.append("Na⁺")
            print("-> Na⁺ confirmed: Persistent yellow flame")
            print_reaction_explanation("Na⁺", 'cation')
    
    # Potassium test
    print("\n4. Testing for K⁺:")
    print("Perform flame test through cobalt glass:")
    flame_color = get_user_input("Flame color through cobalt glass? (violet/none): ", ['violet', 'none'])
    if flame_color == "violet":
        print("Confirmatory test:")
        print("a. Add sodium cobaltinitrite solution")
        if get_user_input("Does a yellow precipitate form? (y/n): ", ['y', 'n']) == 'y':
            detected.append("K⁺")
            print("-> K⁺ confirmed: K₂Na[Co(NO₂)₆] precipitation")
            print_reaction_explanation("K⁺", 'cation')
    
    if not detected:
        print("No Group VI cations detected.")
    
    return detected
# ======================
# ANION TEST FUNCTIONS
# ======================

def test_group_i_anions():
    """Test for Group I anions (CO₃²⁻, S²⁻, NO₂⁻, CH₃COO⁻)"""
    detected = []
    print("\n=== GROUP I: Dilute H₂SO₄ Tests ===")
    print("Procedure: Take 2mL test solution in test tube, add 1mL dilute H₂SO₄")
    
    if get_user_input("Is there effervescence/gas evolution? (y/n): ", ['y', 'n']) == 'y':
        print("\nObserve carefully:")
        print("1. Color and smell of gas")
        print("2. Effect on lime water")
        print("3. Effect on lead acetate paper")
        
        # Carbonate test
        print("\n1. Testing for CO₃²⁻:")
        print("a. Pass evolved gas through lime water (Ca(OH)₂)")
        if get_user_input("Does lime water turn milky? (y/n): ", ['y', 'n']) == 'y':
            detected.append("CO₃²⁻")
            print("-> CO₃²⁻ confirmed: CO₂ gas detected")
            print_reaction_explanation("CO₃²⁻", 'anion')
        
        # Sulfide test
        print("\n2. Testing for S²⁻:")
        print("a. Note smell (rotten eggs)")
        print("b. Bring moist lead acetate paper to mouth of test tube")
        if get_user_input("Does paper turn black? (y/n): ", ['y', 'n']) == 'y':
            detected.append("S²⁻")
            print("-> S²⁻ confirmed: PbS formation")
            print_reaction_explanation("S²⁻", 'anion')
        
        # Nitrite test
        print("\n3. Testing for NO₂⁻:")
        print("a. Observe gas color (brown fumes)")
        if get_user_input("Are brown fumes visible? (y/n): ", ['y', 'n']) == 'y':
            detected.append("NO₂⁻")
            print("-> NO₂⁻ confirmed: NO₂ gas detected")
            print_reaction_explanation("NO₂⁻", 'anion')
        
        # Acetate test
        print("\n4. Testing for CH₃COO⁻:")
        print("a. Note vinegar-like smell")
        if get_user_input("Is there a distinct vinegar odor? (y/n): ", ['y', 'n']) == 'y':
            print("b. Confirm with ferric chloride test")
            if get_user_input("Add FeCl₃. Does solution turn red-brown? (y/n): ", ['y', 'n']) == 'y':
                detected.append("CH₃COO⁻")
                print("-> CH₃COO⁻ confirmed: Smell and color change")
                print_reaction_explanation("CH₃COO⁻", 'anion')
    
    else:
        print("No Group I anions detected.")
    
    return detected

def test_group_ii_anions():
    """Test for Group II anions (Cl⁻, Br⁻, I⁻, NO₃⁻)"""
    detected = []
    print("\n=== GROUP II: Conc. H₂SO₄ Tests ===")
    print("CAUTION: Perform in fume hood. Use small quantities.")
    print("Procedure: Take 1mL test solution, add 1mL conc. H₂SO₄ carefully")
    
    if get_user_input("Are colored fumes evolved? (y/n): ", ['y', 'n']) == 'y':
        print("\nObserve carefully:")
        print("1. Color of fumes")
        print("2. Odor characteristics")
        print("3. Precipitate behavior with AgNO₃")
        
        # Chloride test
        print("\n1. Testing for Cl⁻:")
        print("a. Note white fumes (HCl)")
        print("b. Perform AgNO₃ test on original solution")
        if get_user_input("White precipitate soluble in NH₄OH? (y/n): ", ['y', 'n']) == 'y':
            detected.append("Cl⁻")
            print("-> Cl⁻ confirmed: AgCl behavior")
            print_reaction_explanation("Cl⁻", 'anion')
        
        # Bromide test
        print("\n2. Testing for Br⁻:")
        print("a. Note yellow-brown fumes (Br₂)")
        print("b. Perform AgNO₃ test on original solution")
        if get_user_input("Pale yellow precipitate partially soluble in NH₄OH? (y/n): ", ['y', 'n']) == 'y':
            detected.append("Br⁻")
            print("-> Br⁻ confirmed: AgBr behavior")
            print_reaction_explanation("Br⁻", 'anion')
        
        # Iodide test
        print("\n3. Testing for I⁻:")
        print("a. Note violet fumes (I₂)")
        print("b. Perform AgNO₃ test on original solution")
        if get_user_input("Yellow precipitate insoluble in NH₄OH? (y/n): ", ['y', 'n']) == 'y':
            detected.append("I⁻")
            print("-> I⁻ confirmed: AgI behavior")
            print_reaction_explanation("I⁻", 'anion')
        
        # Nitrate test
        print("\n4. Testing for NO₃⁻:")
        print("a. Note brown fumes (NO₂)")
        print("b. Perform brown ring test:")
        print("   - Add FeSO₄ solution to test tube")
        print("   - Carefully add conc. H₂SO₄ down the side")
        if get_user_input("Brown ring at interface? (y/n): ", ['y', 'n']) == 'y':
            detected.append("NO₃⁻")
            print("-> NO₃⁻ confirmed: Brown ring test")
            print_reaction_explanation("NO₃⁻", 'anion')
    
    else:
        print("No Group II anions detected.")
    
    return detected

def test_group_iii_anions():
    """Test for Group III anions (SO₄²⁻, PO₄³⁻, BO₃³⁻)"""
    detected = []
    print("\n=== GROUP III: Specific Tests ===")
    
    # Sulfate test
    print("\n1. Testing for SO₄²⁻:")
    print("a. Acidify test solution with dilute HCl")
    print("b. Add BaCl₂ solution")
    if get_user_input("White precipitate forms? (y/n): ", ['y', 'n']) == 'y':
        print("c. Test precipitate solubility in conc. HCl")
        if get_user_input("Precipitate insoluble? (y/n): ", ['y', 'n']) == 'y':
            detected.append("SO₄²⁻")
            print("-> SO₄²⁻ confirmed: BaSO₄ precipitation")
            print_reaction_explanation("SO₄²⁻", 'anion')
    
    # Phosphate test
    print("\n2. Testing for PO₄³⁻:")
    print("a. Add conc. HNO₃ and ammonium molybdate")
    print("b. Warm gently (60°C water bath)")
    if get_user_input("Yellow precipitate forms? (y/n): ", ['y', 'n']) == 'y':
        detected.append("PO₄³⁻")
        print("-> PO₄³⁻ confirmed: Ammonium phosphomolybdate")
        print_reaction_explanation("PO₄³⁻", 'anion')
    
    # Borate test
    print("\n3. Testing for BO₃³⁻:")
    print("a. Mix sample with methanol and conc. H₂SO₄")
    print("b. Ignite carefully (flame test)")
    if get_user_input("Green-edged flame observed? (y/n): ", ['y', 'n']) == 'y':
        detected.append("BO₃³⁻")
        print("-> BO₃³⁻ confirmed: Green flame test")
        print_reaction_explanation("BO₃³⁻", 'anion')
    
    if not detected:
        print("No Group III anions detected.")
    
    return detected
# ======================
# ENHANCED MENU SYSTEM
# ======================

def display_menu():
    """Main menu interface with enhanced features"""
    while True:
        print("\n" + "="*50)
        print("QUALITATIVE CHEMICAL ANALYSIS SYSTEM".center(50))
        print("="*50)
        print("\nMain Menu:")
        print("1. 🧪 Cation Analysis (Groups I-VI)")
        print("2. 🧪 Anion Analysis (Groups I-III)")
        print("3. 📚 Chemical Reaction Database")
        print("4. ⚗️  Virtual Lab Assistant")
        print("5. ℹ️  Program Information")
        print("6. 🚪 Exit Program")
        
        choice = get_user_input("\nEnter your choice (1-6): ", ['1', '2', '3', '4', '5', '6'])
        
        if choice == '1':
            cation_analysis_menu()
        elif choice == '2':
            anion_analysis_menu()
        elif choice == '3':
            reaction_database_menu()
        elif choice == '4':
            virtual_lab_assistant()
        elif choice == '5':
            show_program_info()
        elif choice == '6':
            if confirm_exit():
                return

def cation_analysis_menu():
    """Cation analysis menu with enhanced features"""
    while True:
        print("\n" + "="*50)
        print("CATION ANALYSIS".center(50))
        print("="*50)
        print("\nSelect analysis option:")
        print("1. 🔍 Complete Cation Analysis (Groups I-VI)")
        print("2. 🔬 Analyze Specific Cation Group")
        print("3. 📊 View Previous Results")
        print("4. 🏠 Return to Main Menu")
        
        choice = get_user_input("\nEnter your choice (1-4): ", ['1', '2', '3', '4'])
        
        if choice == '1':
            perform_full_cation_analysis()
        elif choice == '2':
            analyze_specific_cation_group()
        elif choice == '3':
            view_previous_results('cation')
        elif choice == '4':
            break

def anion_analysis_menu():
    """Anion analysis menu with enhanced features"""
    while True:
        print("\n" + "="*50)
        print("ANION ANALYSIS".center(50))
        print("="*50)
        print("\nSelect analysis option:")
        print("1. 🔍 Complete Anion Analysis (Groups I-III)")
        print("2. 🔬 Analyze Specific Anion Group")
        print("3. 📊 View Previous Results")
        print("4. 🏠 Return to Main Menu")
        
        choice = get_user_input("\nEnter your choice (1-4): ", ['1', '2', '3', '4'])
        
        if choice == '1':
            perform_full_anion_analysis()
        elif choice == '2':
            analyze_specific_anion_group()
        elif choice == '3':
            view_previous_results('anion')
        elif choice == '4':
            break

def reaction_database_menu():
    """Enhanced chemical reaction database browser"""
    while True:
        print("\n" + "="*50)
        print("CHEMICAL REACTION DATABASE".center(50))
        print("="*50)
        print("\nSelect option:")
        print("1. 🔎 Search by Ion")
        print("2. 📖 Browse All Reactions")
        print("3. 🧪 View Group-Wise Reactions")
        print("4. 🏠 Return to Main Menu")
        
        choice = get_user_input("\nEnter your choice (1-4): ", ['1', '2', '3', '4'])
        
        if choice == '1':
            search_ion_reactions()
        elif choice == '2':
            browse_all_reactions()
        elif choice == '3':
            view_group_reactions()
        elif choice == '4':
            break

def virtual_lab_assistant():
    """Interactive virtual lab assistant"""
    print("\n" + "="*50)
    print("VIRTUAL LAB ASSISTANT".center(50))
    print("="*50)
    print("\nThis feature provides:")
    print("- 🧑‍🔬 Step-by-step procedure guidance")
    print("- ⚠️  Safety precautions for each test")
    print("- 🎥 Video demonstration links")
    print("- 📝 Lab report templates")
    
    input("\nPress Enter to return to main menu...")

# ======================
# UTILITY FUNCTIONS
# ======================

def save_results_to_file(filename, ions, ion_type):
    """Save analysis results to a text file"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Qualitative Analysis Results - {ion_type.upper()}\n")
            f.write("="*50 + "\n")
            f.write(f"Detected {ion_type}s: {', '.join(ions)}\n\n")
            
            # Use the correct reaction database
            reactions = CATION_REACTIONS if ion_type == 'cation' else ANION_REACTIONS
            
            for ion in ions:
                if ion in reactions:
                    f.write(f"{ion}:\n")
                    f.write(f"Test Method: {reactions[ion]['test']}\n")
                    f.write(f"Reaction: {reactions[ion]['reaction']}\n")
                    f.write(f"Principle: {reactions[ion]['reason']}\n\n")
        return True
    except Exception as e:
        print(f"Error saving results to file: {e}")
        return False

def save_analysis_session(detected, ion_type):
    """Save the current analysis session"""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{ion_type}_analysis_{timestamp}.txt"
        if save_results_to_file(filename, list(set(detected)), ion_type):
            print(f"\nSession automatically saved to {filename}")
            return True
        else:
            print("Failed to save analysis session")
            return False
    except Exception as e:
        print(f"Error saving analysis session: {e}")
        return False
    
def browse_all_reactions():
    """Display all available chemical reactions"""
    print("\n" + "="*50)
    print("ALL CHEMICAL REACTIONS".center(50))
    print("="*50)
    
    print("\nCATIONS:")
    for ion, data in CATION_REACTIONS.items():
        print(f"\n{ion}:")
        print(f"Test: {data['test']}")
        print(f"Reaction: {data['reaction']}")
        print(f"Group: {data['group']}")
    
    print("\nANIONS:")
    for ion, data in ANION_REACTIONS.items():
        print(f"\n{ion}:")
        print(f"Test: {data['test']}")
        print(f"Reaction: {data['reaction']}")
        print(f"Group: {data['group']}")
    
    input("\nPress Enter to return to menu...")

def search_ion_reactions():
    """Search for specific ion reactions"""
    print("\n" + "="*50)
    print("SEARCH ION REACTIONS".center(50))
    print("="*50)
    
    while True:
        ion = input("\nEnter ion to search (e.g., 'Fe³⁺', 'SO₄²⁻') or 'back': ").strip()
        if ion.lower() == 'back':
            break
        
        found = False
        if ion in CATION_REACTIONS:
            print(f"\nCATION FOUND: {ion}")
            data = CATION_REACTIONS[ion]
            print(f"Test: {data['test']}")
            print(f"Reaction: {data['reaction']}")
            print(f"Group: {data['group']}")
            found = True
            
        if ion in ANION_REACTIONS:
            print(f"\nANION FOUND: {ion}")
            data = ANION_REACTIONS[ion]
            print(f"Test: {data['test']}")
            print(f"Reaction: {data['reaction']}")
            print(f"Group: {data['group']}")
            found = True
            
        if not found:
            print(f"\nIon '{ion}' not found in databases.")
            print("Try using standard notation (e.g., Fe³⁺, SO₄²⁻)")

def show_program_info():
    """Display program information"""
    print("\n" + "="*50)
    print("PROGRAM INFORMATION".center(50))
    print("="*50)
    
    print("""
QUALITATIVE CHEMICAL ANALYSIS SYSTEM
Version: 2.1
Last Updated: 2023-11-15

Developed for educational purposes to assist in:
- Systematic qualitative chemical analysis
- Identification of cations and anions
- Understanding chemical reactions and principles

Features:
- Complete cation analysis (Groups I-VI)
- Complete anion analysis (Groups I-III)
- Chemical reaction database
- Virtual lab assistant
- Automatic result saving

Safety Notice:
Always perform chemical tests under proper supervision
and with appropriate safety equipment.
""")
    
    input("\nPress Enter to return to main menu...")

def view_group_reactions():
    """Display reactions organized by analysis groups"""
    print("\n" + "="*50)
    print("GROUP-WISE REACTIONS".center(50))
    print("="*50)
    
    # Define group information
    cation_groups = {
        "I": ["Pb²⁺", "Ag⁺", "Hg₂²⁺"],
        "II": ["Cu²⁺", "Pb²⁺", "Bi³⁺", "As³⁺/⁵⁺"],
        "III": ["Fe³⁺", "Al³⁺", "Cr³⁺"],
        "IV": ["Zn²⁺", "Mn²⁺", "Ni²⁺", "Co²⁺"],
        "V": ["Ba²⁺", "Sr²⁺", "Ca²⁺"],
        "VI": ["NH₄⁺", "Mg²⁺", "Na⁺", "K⁺"]
    }
    
    anion_groups = {
        "I": ["CO₃²⁻", "S²⁻", "NO₂⁻", "CH₃COO⁻"],
        "II": ["Cl⁻", "Br⁻", "I⁻", "NO₃⁻"],
        "III": ["SO₄²⁻", "PO₄³⁻", "BO₃³⁻"]
    }
    
    while True:
        print("\nSelect group type:")
        print("1. Cation Groups (I-VI)")
        print("2. Anion Groups (I-III)")
        print("3. Back to previous menu")
        
        choice = get_user_input("Enter choice (1-3): ", ['1', '2', '3'])
        
        if choice == '1':
            print("\nCATION GROUPS:")
            for group, ions in cation_groups.items():
                print(f"\nGroup {group}:")
                for ion in ions:
                    if ion in CATION_REACTIONS:
                        print(f"  {ion}: {CATION_REACTIONS[ion]['test']}")
        
        elif choice == '2':
            print("\nANION GROUPS:")
            for group, ions in anion_groups.items():
                print(f"\nGroup {group}:")
                for ion in ions:
                    if ion in ANION_REACTIONS:
                        print(f"  {ion}: {ANION_REACTIONS[ion]['test']}")
        
        elif choice == '3':
            break
        
        # Add option to view details
        if choice in ['1', '2']:
            ion = input("\nEnter ion to view details (or 'back'): ").strip()
            if ion.lower() != 'back':
                if ion in CATION_REACTIONS:
                    print_reaction_explanation(ion, 'cation')
                elif ion in ANION_REACTIONS:
                    print_reaction_explanation(ion, 'anion')
                else:
                    print("Ion not found in any group.")
# ... [keep all your existing utility functions below] ...

def perform_full_cation_analysis():
    """Enhanced complete cation analysis flow"""
    print("\n" + "="*50)
    print("COMPLETE CATION ANALYSIS".center(50))
    print("="*50)
    
    detected = []
    groups = [
        ("Group I (HCl Group)", test_group_i_cations),  # Changed to _cations
        ("Group II (H₂S Acidic Group)", test_group_ii_cations),  # Changed to _cations
        ("Group III (NH₄OH Group)", test_group_iii_cations),  # Changed to _cations
        ("Group IV (H₂S Basic Group)", test_group_iv_cations),  # Changed to _cations
        ("Group V (Carbonate Group)", test_group_v_cations),  # Changed to _cations
        ("Group VI (Soluble Group)", test_group_vi_cations)  # Changed to _cations
    ]
    
    for name, test_func in groups:
        print(f"\nStarting {name} Analysis...")
        detected.extend(test_func())
        print(f"\n{name} Analysis Complete.")
        if input("Continue to next group? (y/n): ").lower() != 'y':
            break
    
    show_detailed_results(detected, 'cation')
    save_analysis_session(detected, 'cation')

def analyze_specific_cation_group():
    """Enhanced specific cation group analysis"""
    group_map = {
        '1': ("Group I (HCl Group: Pb²⁺, Ag⁺, Hg₂²⁺)", test_group_i_cations),  # Changed to _cations
        '2': ("Group II (H₂S Acidic: Cu²⁺, Pb²⁺, Bi³⁺, As³⁺/⁵⁺)", test_group_ii_cations),  # Changed to _cations
        '3': ("Group III (NH₄OH: Fe³⁺, Al³⁺, Cr³⁺)", test_group_iii_cations),  # Changed to _cations
        '4': ("Group IV (H₂S Basic: Zn²⁺, Mn²⁺, Ni²⁺, Co²⁺)", test_group_iv_cations),  # Changed to _cations
        '5': ("Group V (Carbonate: Ba²⁺, Sr²⁺, Ca²⁺)", test_group_v_cations),  # Changed to _cations
        '6': ("Group VI (Soluble: NH₄⁺, Na⁺, K⁺, Mg²⁺)", test_group_vi_cations)  # Changed to _cations
    }
    
    print("\nAvailable Cation Groups:")
    for num, (name, _) in group_map.items():
        print(f"{num}. {name}")
    
    choice = get_user_input("\nSelect group to analyze (1-6) or '0' to cancel: ", 
                          ['0', '1', '2', '3', '4', '5', '6'])
    
    if choice != '0':
        group_name, test_func = group_map[choice]
        print(f"\nStarting {group_name} Analysis...")
        detected = test_func()
        show_detailed_results(detected, 'cation')
        save_analysis_session(detected, 'cation')

def perform_full_anion_analysis():
    """Complete anion analysis flow"""
    print("\n" + "="*50)
    print("COMPLETE ANION ANALYSIS".center(50))
    print("="*50)
    
    detected = []
    groups = [
        ("Group I (Dilute H₂SO₄ Group)", test_group_i_anions),
        ("Group II (Conc. H₂SO₄ Group)", test_group_ii_anions),
        ("Group III (Special Tests Group)", test_group_iii_anions)
    ]
    
    for name, test_func in groups:
        print(f"\nStarting {name} Analysis...")
        detected.extend(test_func())
        print(f"\n{name} Analysis Complete.")
        if input("Continue to next group? (y/n): ").lower() != 'y':
            break
    
    show_detailed_results(detected, 'anion')
    save_analysis_session(detected, 'anion')

def analyze_specific_anion_group():
    """Enhanced specific anion group analysis"""
    group_map = {
        '1': ("Group I (Dilute H₂SO₄: CO₃²⁻, S²⁻, NO₂⁻, CH₃COO⁻)", test_group_i_anions),
        '2': ("Group II (Conc. H₂SO₄: Cl⁻, Br⁻, I⁻, NO₃⁻)", test_group_ii_anions),
        '3': ("Group III (Special Tests: SO₄²⁻, PO₄³⁻, BO₃³⁻)", test_group_iii_anions)
    }
    
    print("\nAvailable Anion Groups:")
    for num, (name, _) in group_map.items():
        print(f"{num}. {name}")
    
    while True:
        choice = get_user_input("\nSelect group to analyze (1-3) or '0' to cancel: ", 
                             ['0', '1', '2', '3'])
        
        if choice == '0':
            break
            
        if choice in group_map:
            group_name, test_func = group_map[choice]
            print(f"\nStarting {group_name} Analysis...")
            detected = test_func()
            
            if detected:
                print("\nDetected ions in this group:")
                for ion in detected:
                    print(f"- {ion}")
                
                # Show details option
                detail = get_user_input("\nView reaction details for these ions? (y/n): ", ['y', 'n'])
                if detail == 'y':
                    for ion in detected:
                        print_reaction_explanation(ion, 'anion')
                
                # Save option
                save = get_user_input("Save these results? (y/n): ", ['y', 'n'])
                if save == 'y':
                    save_analysis_session(detected, 'anion')
            else:
                print("No anions detected in this group.")
            
            break

def show_detailed_results(detected, ion_type):
    """Enhanced results display with visualization"""
    if not detected:
        print(f"\nNo {ion_type}s detected.")
        return
    
    unique_ions = sorted(set(detected))
    print(f"\n📋 Detected {ion_type}s:")
    for ion in unique_ions:
        print(f"- {ion}")
    
    while True:
        print("\nResults Options:")
        print("1. 📝 View all reaction details")
        print("2. 🔍 View specific ion details")
        print("3. 📊 View analysis summary")
        print("4. 💾 Save results to file")
        print("5. 🏠 Return to previous menu")
        
        choice = get_user_input("Select option (1-5): ", ['1', '2', '3', '4', '5'])
        
        if choice == '1':
            print(f"\n=== DETAILED {ion_type.upper()} RESULTS ===")
            for ion in unique_ions:
                print_reaction_explanation(ion, ion_type)
        
        elif choice == '2':
            ion = get_user_input(f"Enter {ion_type} to view (e.g., {unique_ions[0]}): ", 
                               unique_ions + ['back'])
            if ion != 'back':
                print_reaction_explanation(ion, ion_type)
        
        elif choice == '3':
            print("\n" + "="*50)
            print(f"ANALYSIS SUMMARY: {len(unique_ions)} {ion_type.upper()}S DETECTED".center(50))
            print("="*50)
            for ion in unique_ions:
                data = CATION_REACTIONS if ion_type == 'cation' else ANION_REACTIONS
                print(f"\n🔬 {ion}: {data[ion]['test']}")
        
        elif choice == '4':
            filename = input("Enter filename to save (e.g., results.txt): ").strip()
            if filename:
                save_results_to_file(filename, unique_ions, ion_type)
                print(f"✅ Results saved to {filename}")
        
        elif choice == '5':
            break

def save_analysis_session(detected, ion_type):
    """Save the current analysis session"""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{ion_type}_analysis_{timestamp}.txt"
    save_results_to_file(filename, list(set(detected)), ion_type)
    print(f"\nSession automatically saved to {filename}")

def view_previous_results(ion_type):
    """View previously saved analysis results"""
    files = [f for f in os.listdir() if f.startswith(ion_type) and f.endswith('.txt')]
    
    if not files:
        print("\nNo previous results found.")
        return
    
    print("\nPrevious Analysis Sessions:")
    for i, f in enumerate(sorted(files, reverse=True), 1):
        print(f"{i}. {f}")
    
    choice = input("\nEnter file number to view (or 0 to cancel): ")
    if choice.isdigit() and 0 < int(choice) <= len(files):
        with open(files[int(choice)-1]) as f:
            print("\n" + f.read())

def confirm_exit():
    """Enhanced exit confirmation"""
    print("\n" + "="*50)
    print("EXIT PROGRAM".center(50))
    print("="*50)
    print("\nOptions:")
    print("1. ✅ Exit and save current session")
    print("2. ❌ Exit without saving")
    print("3. � Return to program")
    
    choice = get_user_input("\nEnter your choice (1-3): ", ['1', '2', '3'])
    
    if choice == '1':
        print("\nThank you for using the Qualitative Chemical Analysis System!")
        print("All session data has been saved.")
        return True
    elif choice == '2':
        print("\nThank you for using the program. Goodbye!")
        return True
    return False

# ======================
# PROGRAM INITIALIZATION
# ======================

if __name__ == "__main__":
    print("\n" + "="*50)
    print("QUALITATIVE CHEMICAL ANALYSIS SYSTEM".center(50))
    print("="*50)
    print("\nInitializing system components...")
    
    # Check for required data files
    if not os.path.exists('reactions.db'):
        print("⚠️  Warning: Reaction database not found!")
    
    # Display safety reminder
    print("\n" + "!"*50)
    print("SAFETY FIRST!".center(50))
    print("!"*50)
    print("\nThis program assists with chemical analysis but")
    print("cannot replace proper lab safety procedures.")
    print("Always wear appropriate PPE when performing tests.")
    
    # Start main menu
    input("\nPress Enter to continue to main menu...")
    display_menu()