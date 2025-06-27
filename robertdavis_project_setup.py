"""
Filename: robertdavis_project_setup.py
Purpose: Automate project folder creation and demonstrate basic Python scripting.
Author: Robert Davis
"""

#####################################
# Imports
#####################################

from utils_robert import get_byline  # Correct import from P1
from pathlib import Path             # For folder and file operations
import time                          # For timing or delays

#####################################
# Define Functions
#####################################

# Function to print the byline
def print_byline():
    print(get_byline())

# Function to create project folders for a range of years
def create_project_folders(base_folder: str = "data", start_year: int = 2021, end_year: int = 2024) -> None:
    """
    Create subfolders for each year from start_year to end_year inside the base_folder.
    """
    print(f"Creating folders inside '{base_folder}' from {start_year} to {end_year}...")

    base_path = Path(base_folder)
    base_path.mkdir(parents=True, exist_ok=True)

    for year in range(start_year, end_year + 1):
        year_folder = base_path / str(year)
        year_folder.mkdir(parents=True, exist_ok=True)
        print(f"Created: {year_folder}")

# Function to simulate monitoring (optional/extra feature)
def simulate_monitoring(seconds: int = 5):
    """
    Simulate a wait period to represent monitoring activity.
    """
    print(f"Monitoring... Waiting {seconds} seconds.")
    time.sleep(seconds)
    print("Monitoring complete.")

#####################################
# Define main() Function
#####################################

def main():
    """Run all our script actions here."""
    print("START main()")

    print_byline()
    create_project_folders()
    simulate_monitoring()

    print("END main()")

#####################################
# Execute main() only if run directly
#####################################

if __name__ == "__main__":
    main()
