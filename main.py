"""
Bonzi Buddy Safe - A malware-free virtual desktop assistant
Main entry point for the application
"""

import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

def main():
    """Main application entry point"""
    print("=" * 50)
    print("Welcome to Bonzi Buddy Safe!")
    print("=" * 50)
    print("\nA safe, malware-free virtual desktop assistant")
    print("Version 1.0.0")
    print("\nThis project is currently in development.")
    print("Stay tuned for updates!\n")
    
    # Future: Initialize and run the main application
    # from bonzi_buddy import BonziBuddy
    # app = BonziBuddy()
    # app.run()

if __name__ == "__main__":
    main()