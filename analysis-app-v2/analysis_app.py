#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QUALITATIVE CHEMICAL ANALYSIS PROGRAM
Updated for new database structure with enhanced logging
"""

# ======================
# IMPORTS
# ======================
import os
import sys
import json
import logging
from datetime import datetime
from typing import Dict, List, Optional, TypedDict, Tuple

# ======================
# TYPE DEFINITIONS
# ======================
class ConfirmatoryTest(TypedDict):
    reagent: str
    observation: str
    equation: str
    explanation: str

class IonData(TypedDict):
    name: str
    confirmatory_test: ConfirmatoryTest

class GroupData(TypedDict):
    title: str
    description: str
    separation_reagent: str
    ions: Dict[str, IonData]

class Database(TypedDict):
    cations: Dict[str, GroupData]
    anions: Dict[str, GroupData]
    metadata: Dict[str, str]

# ======================
# CONSTANTS
# ======================
DATABASE_FILE = "database.json"
MAX_LOG_FILES = 10
MENU_WIDTH = 50

# ======================
# GLOBAL STATE
# ======================
chemical_db: Database = {
    "cations": {},
    "anions": {},
    "metadata": {}
}

# ======================
# UTILITY FUNCTIONS
# ======================
def setup_logging() -> None:
    """Configure logging system with rotation"""
    logging.basicConfig(
        filename='qualitative_analysis.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='w'  # Start fresh each run
    )
    logging.info("Logging system initialized")

def load_database() -> bool:
    """Load chemical database from JSON file"""
    try:
        global chemical_db
        with open(DATABASE_FILE, 'r', encoding='utf-8') as f:
            chemical_db = json.load(f)
        logging.info("Database loaded successfully")
        return True
    except FileNotFoundError:
        logging.critical("Database file not found")
        print(f"Error: Database file {DATABASE_FILE} not found!")
        return False
    except json.JSONDecodeError as e:
        logging.critical(f"Invalid JSON format: {str(e)}")
        print(f"Error: Invalid database format - {str(e)}")
        return False

def clear_screen() -> None:
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header(title: str) -> None:
    """Display consistent menu headers"""
    print("\n" + "=" * MENU_WIDTH)
    print(title.center(MENU_WIDTH))
    print("=" * MENU_WIDTH)

def get_user_input(prompt: str, valid_options: Optional[List[str]] = None) -> str:
    """Get validated user input with case-insensitive matching"""
    while True:
        try:
            response = input(prompt).lower().strip()
            logging.debug(f"User input: {response}")
            if not valid_options or response in valid_options:
                return response
            print(f"Please enter one of: {', '.join(valid_options)}")
            logging.warning(f"Invalid input: {response}")
        except (EOFError, KeyboardInterrupt):
            if confirm_exit():
                sys.exit(0)

# ======================
# CORE ANALYSIS CLASSES
# ======================
class ChemicalAnalyzer:
    """Base class for chemical analysis functionality"""
    
    def __init__(self, ion_type: str):
        self.ion_type = ion_type
        self.detected_ions: List[str] = []
        self.groups: Dict[str, GroupData] = {}
        self.all_reactions: Dict[str, IonData] = {}
        logging.info(f"{ion_type.capitalize()} analyzer initialized")
        
        if ion_type == "cation":
            self.groups = chemical_db["cations"]
        else:
            self.groups = chemical_db["anions"]
            
        # Flatten all ions into a single dict
        for group in self.groups.values():
            self.all_reactions.update(group["ions"])
    
    def print_reaction_details(self, ion: str) -> None:
        """Print detailed information about a specific ion"""
        if ion in self.all_reactions:
            data = self.all_reactions[ion]
            test = data["confirmatory_test"]
            print(f"\nReaction Details for {ion}:")
            print(f"Test Method: {test['reagent']}")
            print(f"Observation: {test['observation']}")
            print(f"Chemical Equation:\n{test['equation']}")
            print(f"Scientific Principle: {test['explanation']}")
            logging.info(f"Displayed details for {ion}")
        else:
            print(f"\nNo data available for {ion}")
            logging.warning(f"Requested unknown ion: {ion}")

    def save_results(self) -> bool:
        """Save analysis results to file"""
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{self.ion_type}_analysis_{timestamp}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Qualitative Analysis Results - {self.ion_type.upper()}\n")
                f.write("=" * MENU_WIDTH + "\n")
                
                if not self.detected_ions:
                    f.write("No ions detected.\n")
                else:
                    unique_ions = sorted(set(self.detected_ions))
                    f.write(f"Detected {self.ion_type}s: {', '.join(unique_ions)}\n\n")
                    
                    for ion in unique_ions:
                        if ion in self.all_reactions:
                            data = self.all_reactions[ion]
                            test = data["confirmatory_test"]
                            f.write(f"{ion}:\n")
                            f.write(f"Test Method: {test['reagent']}\n")
                            f.write(f"Observation: {test['observation']}\n")
                            f.write(f"Reaction: {test['equation']}\n")
                            f.write(f"Principle: {test['explanation']}\n\n")
            
            print(f"\nResults saved to {filename}")
            logging.info(f"Results saved to {filename}")
            return True
            
        except IOError as e:
            print(f"Error saving results: {e}")
            logging.error(f"Save failed: {str(e)}")
            return False

    def show_detailed_results(self) -> None:
        """Display detailed results of analysis"""
        if not self.detected_ions:
            print(f"\nNo {self.ion_type}s detected.")
            logging.info("No ions detected in results")
            return
        
        unique_ions = sorted(set(self.detected_ions))
        print(f"\n📋 Detected {self.ion_type}s:")
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
                print(f"\n=== DETAILED {self.ion_type.upper()} RESULTS ===")
                for ion in unique_ions:
                    self.print_reaction_details(ion)
            
            elif choice == '2':
                ion = get_user_input(
                    f"Enter {self.ion_type} to view (e.g., {unique_ions[0]}): ",
                    unique_ions + ['back']
                )
                if ion != 'back':
                    self.print_reaction_details(ion)
            
            elif choice == '3':
                display_header(f"ANALYSIS SUMMARY: {len(unique_ions)} {self.ion_type.upper()}S DETECTED")
                for ion in unique_ions:
                    print(f"\n🔬 {ion}: {self.all_reactions[ion]['confirmatory_test']['reagent']}")
            
            elif choice == '4':
                if self.save_results():
                    print("✅ Results saved successfully")
                else:
                    print("❌ Failed to save results")
            
            elif choice == '5':
                break

class CationAnalyzer(ChemicalAnalyzer):
    """Handles cation analysis procedures"""
    
    def __init__(self):
        super().__init__("cation")
        self.group_order = ["Group I", "Group II", "Group III", "Group IV", "Group V"]
    
    def test_group(self, group_key: str) -> List[str]:
        """Generic group testing function"""
        detected = []
        group = self.groups[group_key]
        
        display_header(group["title"])
        print(group["description"])
        print(f"\nSeparation Reagent: {group['separation_reagent']}")
        
        logging.info(f"Testing {group_key} - {group['title']}")
        
        # Get group-specific ions
        ions = group["ions"].keys()
        print(f"\nPossible ions in this group: {', '.join(ions)}")
        
        if get_user_input("\nDid precipitation occur? (y/n): ", ['y', 'n']) == 'y':
            print("\nPerforming confirmatory tests...")
            for ion in ions:
                test = group["ions"][ion]["confirmatory_test"]
                print(f"\nTesting for {ion}:")
                print(f"Reagent: {test['reagent']}")
                print(f"Expected Observation: {test['observation']}")
                
                if get_user_input("Did you observe this result? (y/n): ", ['y', 'n']) == 'y':
                    detected.append(ion)
                    logging.info(f"Detected {ion} in {group_key}")
                    self.print_reaction_details(ion)
        
        self.detected_ions.extend(detected)
        return detected

    def perform_full_analysis(self) -> None:
        """Perform complete cation analysis (Groups I-V)"""
        display_header("COMPLETE CATION ANALYSIS")
        logging.info("Starting full cation analysis")
        
        for group_key in self.group_order:
            group_name = self.groups[group_key]["title"]
            print(f"\nStarting {group_name} Analysis...")
            self.test_group(group_key)
            print(f"\n{group_name} Analysis Complete.")
            if get_user_input("Continue to next group? (y/n): ", ['y', 'n']) != 'y':
                break
        
        self.show_detailed_results()
        self.save_results()

class AnionAnalyzer(ChemicalAnalyzer):
    """Handles anion analysis procedures"""
    
    def __init__(self):
        super().__init__("anion")
        self.group_order = ["Group I", "Group II", "Group III"]
    
    def test_group(self, group_key: str) -> List[str]:
        """Generic group testing function"""
        detected = []
        group = self.groups[group_key]
        
        display_header(group["title"])
        print(group["description"])
        print(f"\nSeparation Reagent: {group['separation_reagent']}")
        
        logging.info(f"Testing {group_key} - {group['title']}")
        
        # Get group-specific ions
        ions = group["ions"].keys()
        print(f"\nPossible ions in this group: {', '.join(ions)}")
        
        if get_user_input("\nDid reaction occur? (y/n): ", ['y', 'n']) == 'y':
            print("\nPerforming confirmatory tests...")
            for ion in ions:
                test = group["ions"][ion]["confirmatory_test"]
                print(f"\nTesting for {ion}:")
                print(f"Reagent: {test['reagent']}")
                print(f"Expected Observation: {test['observation']}")
                
                if get_user_input("Did you observe this result? (y/n): ", ['y', 'n']) == 'y':
                    detected.append(ion)
                    logging.info(f"Detected {ion} in {group_key}")
                    self.print_reaction_details(ion)
        
        self.detected_ions.extend(detected)
        return detected

    def perform_full_analysis(self) -> None:
        """Perform complete anion analysis (Groups I-III)"""
        display_header("COMPLETE ANION ANALYSIS")
        logging.info("Starting full anion analysis")
        
        for group_key in self.group_order:
            group_name = self.groups[group_key]["title"]
            print(f"\nStarting {group_name} Analysis...")
            self.test_group(group_key)
            print(f"\n{group_name} Analysis Complete.")
            if get_user_input("Continue to next group? (y/n): ", ['y', 'n']) != 'y':
                break
        
        self.show_detailed_results()
        self.save_results()

# ======================
# MENU SYSTEM IMPLEMENTATION
# ======================

def confirm_exit() -> bool:
    """Confirm program exit"""
    clear_screen()
    display_header("EXIT PROGRAM")
    
    print("\nOptions:")
    print("1. ✅ Exit and save current sessions")
    print("2. ❌ Exit without saving")
    print("3. ↩ Return to program")
    
    choice = get_user_input("\nEnter your choice (1-3): ", ['1', '2', '3'])
    
    if choice == '1':
        print("\nAll session data has been saved.")
        return True
    elif choice == '2':
        print("\nNo data will be saved.")
        return True
    return False


def cation_analysis_menu(analyzer: CationAnalyzer) -> None:
    """Cation analysis menu"""
    while True:
        clear_screen()
        display_header("CATION ANALYSIS")
        
        print("\nSelect analysis option:")
        print("1. 🔍 Complete Cation Analysis (Groups I-V)")
        print("2. 🔬 Analyze Specific Cation Group")
        print("3. 📊 View Current Results")
        print("4. 🏠 Return to Main Menu")
        
        choice = get_user_input("\nEnter your choice (1-4): ", ['1', '2', '3', '4'])
        
        if choice == '1':
            analyzer.perform_full_analysis()
            input("\nPress Enter to continue...")
        elif choice == '2':
            analyze_specific_cation_group(analyzer)
        elif choice == '3':
            analyzer.show_detailed_results()
            input("\nPress Enter to continue...")
        elif choice == '4':
            break

def analyze_specific_cation_group(analyzer: CationAnalyzer) -> None:
    """Menu for selecting specific cation groups"""
    group_map = {
        '1': ("Group I (HCl Group)", "Group I"),
        '2': ("Group II (H₂S Acidic)", "Group II"),
        '3': ("Group III (NH₄OH)", "Group III"),
        '4': ("Group IV (H₂S Basic)", "Group IV"),
        '5': ("Group V (Carbonate)", "Group V")
    }
    
    while True:
        clear_screen()
        display_header("SELECT CATION GROUP")
        
        print("\nAvailable Cation Groups:")
        for num, (name, _) in group_map.items():
            print(f"{num}. {name}")
        print("0. ↩ Back to Cation Menu")
        
        choice = get_user_input("\nSelect group to analyze (1-5) or 0 to cancel: ", 
                              ['0', '1', '2', '3', '4', '5'])
        
        if choice == '0':
            break
            
        if choice in group_map:
            group_name, group_key = group_map[choice]
            clear_screen()
            display_header(group_name.upper())
            
            detected = analyzer.test_group(group_key)
            if detected:
                print("\nDetected ions:")
                for ion in detected:
                    print(f"- {ion}")
                
                detail = get_user_input("\nView reaction details for these ions? (y/n): ", ['y', 'n'])
                if detail == 'y':
                    for ion in detected:
                        analyzer.print_reaction_details(ion)
                
                save = get_user_input("\nSave these results? (y/n): ", ['y', 'n'])
                if save == 'y':
                    analyzer.save_results()
            else:
                print("\nNo cations detected in this group.")
            
            input("\nPress Enter to continue...")

def anion_analysis_menu(analyzer: AnionAnalyzer) -> None:
    """Anion analysis menu"""
    while True:
        clear_screen()
        display_header("ANION ANALYSIS")
        
        print("\nSelect analysis option:")
        print("1. 🔍 Complete Anion Analysis (Groups I-III)")
        print("2. 🔬 Analyze Specific Anion Group")
        print("3. 📊 View Current Results")
        print("4. 🏠 Return to Main Menu")
        
        choice = get_user_input("\nEnter your choice (1-4): ", ['1', '2', '3', '4'])
        
        if choice == '1':
            analyzer.perform_full_analysis()
            input("\nPress Enter to continue...")
        elif choice == '2':
            analyze_specific_anion_group(analyzer)
        elif choice == '3':
            analyzer.show_detailed_results()
            input("\nPress Enter to continue...")
        elif choice == '4':
            break

def analyze_specific_anion_group(analyzer: AnionAnalyzer) -> None:
    """Menu for selecting specific anion groups"""
    group_map = {
        '1': ("Group I (Dilute H₂SO₄)", "Group I"),
        '2': ("Group II (Conc. H₂SO₄)", "Group II"),
        '3': ("Group III (Special Tests)", "Group III")
    }
    
    while True:
        clear_screen()
        display_header("SELECT ANION GROUP")
        
        print("\nAvailable Anion Groups:")
        for num, (name, _) in group_map.items():
            print(f"{num}. {name}")
        print("0. ↩ Back to Anion Menu")
        
        choice = get_user_input("\nSelect group to analyze (1-3) or 0 to cancel: ", 
                              ['0', '1', '2', '3'])
        
        if choice == '0':
            break
            
        if choice in group_map:
            group_name, group_key = group_map[choice]
            clear_screen()
            display_header(group_name.upper())
            
            detected = analyzer.test_group(group_key)
            if detected:
                print("\nDetected ions:")
                for ion in detected:
                    print(f"- {ion}")
                
                detail = get_user_input("\nView reaction details for these ions? (y/n): ", ['y', 'n'])
                if detail == 'y':
                    for ion in detected:
                        analyzer.print_reaction_details(ion)
                
                save = get_user_input("\nSave these results? (y/n): ", ['y', 'n'])
                if save == 'y':
                    analyzer.save_results()
            else:
                print("\nNo anions detected in this group.")
            
            input("\nPress Enter to continue...")

def reaction_database_menu() -> None:
    """Chemical reaction database browser"""
    while True:
        clear_screen()
        display_header("CHEMICAL REACTION DATABASE")
        
        print("\nSelect option:")
        print("1. 🔎 Search by Ion")
        print("2. 📖 Browse All Reactions")
        print("3. 🧪 View Group-Wise Reactions")
        print("4. 🏠 Return to Main Menu")
        
        choice = get_user_input("\nEnter your choice (1-4): ", ['1', '2', '3', '4'])
        
        if choice == '1':
            search_ion_reactions()
            input("\nPress Enter to continue...")
        elif choice == '2':
            browse_all_reactions()
            input("\nPress Enter to continue...")
        elif choice == '3':
            view_group_reactions()
            input("\nPress Enter to continue...")
        elif choice == '4':
            break

def virtual_lab_assistant() -> None:
    """Virtual lab assistant feature"""
    clear_screen()
    display_header("VIRTUAL LAB ASSISTANT")
    
    print("\nThis feature provides:")
    print("- 🧑‍🔬 Step-by-step procedure guidance")
    print("- ⚠️  Safety precautions for each test")
    print("- 🎥 Video demonstration links")
    print("- 📝 Lab report templates")
    print("\nComing in future versions!")
    
    input("\nPress Enter to return to main menu...")

def show_program_info() -> None:
    """Display program information"""
    clear_screen()
    display_header("PROGRAM INFORMATION")
    
    print(f"""
QUALITATIVE CHEMICAL ANALYSIS SYSTEM
Version: {chemical_db['metadata']['version']}
Last Updated: {chemical_db['metadata']['revision_date']}

Database System: {chemical_db['metadata']['group_system']}
Reference: {chemical_db['metadata']['reference']}

Developed for educational purposes to assist in:
- Systematic qualitative chemical analysis
- Identification of cations and anions
- Understanding chemical reactions and principles

Safety Notice:
Always perform chemical tests under proper supervision
and with appropriate safety equipment.
""")
    
    input("\nPress Enter to return to main menu...")

def browse_all_reactions() -> None:
    """Display all chemical reactions"""
    clear_screen()
    display_header("ALL CHEMICAL REACTIONS")
    
    print("\nCATIONS:")
    for group in chemical_db['cations'].values():
        for ion, data in group['ions'].items():
            print(f"\n{ion}:")
            print(f"Test: {data['confirmatory_test']['reagent']}")
            print(f"Reaction: {data['confirmatory_test']['equation']}")
    
    print("\nANIONS:")
    for group in chemical_db['anions'].values():
        for ion, data in group['ions'].items():
            print(f"\n{ion}:")
            print(f"Test: {data['confirmatory_test']['reagent']}")
            print(f"Reaction: {data['confirmatory_test']['equation']}")

def search_ion_reactions() -> None:
    """Search for specific ion reactions"""
    clear_screen()
    display_header("SEARCH ION REACTIONS")
    
    while True:
        ion = input("\nEnter ion to search (e.g., 'Fe³⁺', 'SO₄²⁻') or 'back': ").strip()
        if ion.lower() == 'back':
            break
        
        found = False
        # Search cations
        for group in chemical_db['cations'].values():
            if ion in group['ions']:
                data = group['ions'][ion]
                print(f"\nCATION FOUND: {ion}")
                print(f"Test: {data['confirmatory_test']['reagent']}")
                print(f"Reaction: {data['confirmatory_test']['equation']}")
                found = True
                
        # Search anions
        for group in chemical_db['anions'].values():
            if ion in group['ions']:
                data = group['ions'][ion]
                print(f"\nANION FOUND: {ion}")
                print(f"Test: {data['confirmatory_test']['reagent']}")
                print(f"Reaction: {data['confirmatory_test']['equation']}")
                found = True
                
        if not found:
            print(f"\nIon '{ion}' not found in databases.")
            print("Try using standard notation (e.g., Fe³⁺, SO₄²⁻)")

def view_group_reactions() -> None:
    """Display reactions organized by analysis groups"""
    while True:
        clear_screen()
        display_header("GROUP-WISE REACTIONS")
        
        print("\nSelect group type:")
        print("1. Cation Groups")
        print("2. Anion Groups")
        print("3. Back to Database Menu")
        
        choice = get_user_input("\nEnter choice (1-3): ", ['1', '2', '3'])
        
        if choice == '1':
            print("\nCATION GROUPS:")
            for group_name, group in chemical_db['cations'].items():
                print(f"\n{group['title']}:")
                for ion in group['ions']:
                    print(f"  {ion}: {group['ions'][ion]['confirmatory_test']['reagent']}")
        
        elif choice == '2':
            print("\nANION GROUPS:")
            for group_name, group in chemical_db['anions'].items():
                print(f"\n{group['title']}:")
                for ion in group['ions']:
                    print(f"  {ion}: {group['ions'][ion]['confirmatory_test']['reagent']}")
        
        elif choice == '3':
            break
        
        input("\nPress Enter to continue...")

def main_menu() -> None:
    """Main menu for the program"""
    while True:
        clear_screen()
        display_header("MAIN MENU")
        
        print("\nSelect an option:")
        print("1. ⚗️ Cation Analysis")
        print("2. 🧪 Anion Analysis")
        print("3. 📚 Chemical Reaction Database")
        print("4. 🤖 Virtual Lab Assistant")
        print("5. ℹ️ Program Information")
        print("6. ❌ Exit Program")
        
        choice = get_user_input("\nEnter your choice (1-6): ", ['1', '2', '3', '4', '5', '6'])
        
        if choice == '1':
            cation_analyzer = CationAnalyzer()
            cation_analysis_menu(cation_analyzer)
        elif choice == '2':
            anion_analyzer = AnionAnalyzer()
            anion_analysis_menu(anion_analyzer)
        elif choice == '3':
            reaction_database_menu()
        elif choice == '4':
            virtual_lab_assistant()
        elif choice == '5':
            show_program_info()
        elif choice == '6':
            if confirm_exit():
                break

# ======================
# PROGRAM INITIALIZATION
# ======================
if __name__ == "__main__":
    try:
        setup_logging()
        logging.info("Program started")
        
        if not load_database():
            sys.exit(1)
            
        clear_screen()
        display_header("QUALITATIVE CHEMICAL ANALYSIS SYSTEM")
        print(f"\nLoaded database version {chemical_db['metadata']['version']}")
        print(f"Last updated: {chemical_db['metadata']['revision_date']}")
        
        # Display safety reminder
        display_header("SAFETY FIRST!")
        print("\nThis program assists with chemical analysis but")
        print("cannot replace proper lab safety procedures.")
        print("Always wear appropriate PPE when performing tests.")
        
        input("\nPress Enter to continue to main menu...")
        main_menu()
        
    except Exception as e:
        logging.critical(f"Program crashed: {str(e)}", exc_info=True)
        print(f"\nA critical error occurred: {str(e)}")
        print("Please check the log file for details.")
    finally:
        logging.info("Program terminated")
        print("\nThank you for using the Qualitative Chemical Analysis System!")