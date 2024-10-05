"""
This module provides a command-line interface (CLI) for interacting with the 
ArcadeMachine class, allowing users to customize their arcade machines.

Author: Jhomar Armando Bojaca Landinez <jabojacal@udistrital.edu.co>

This file is part of ArcadeMachine-Customizer.

ArcadeMachine-Customizer is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

ArcadeMachine-Customizer is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with ArcadeMachine-Customizer. If not, see <https://www.gnu.org/licenses/>.
"""

from arcade_machine import ArcadeMachine


def main():
    """
    The main function that runs the CLI application.

    This function provides a menu with options for the user to customize their arcade machine:
    1. Select material.
    2. Customize appearance.
    3. Modify controls.
    4. Configure sound.
    5. Configure connectivity.
    6. Select storage.
    7. Show game catalog.
    8. Add games to the machine.
    9. Finalize purchase.
    10. Exit.

    The function creates an instance of the ArcadeMachine class and enters a loop where it
    presents the user with a menu and processes their choices by calling appropriate methods
    on the ArcadeMachine instance.

    """
    machine = ArcadeMachine()

    while True:
        print("\n--- Main Menu ---")
        print("1. Select material")
        print("2. Customize appearance")
        print("3. Modify controls")
        print("4. Configure sound")
        print("5. Configure connectivity")
        print("6. Select storage")
        print("7. Show game catalog")
        print("8. Add games to the machine")
        print("9. Finalize purchase")
        print("10. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            machine.select_material()
        elif choice == "2":
            machine.select_appearance()
        elif choice == "3":
            machine.select_controls()
        elif choice == "4":
            machine.select_sound_system()
        elif choice == "5":
            machine.select_connectivity()
        elif choice == "6":
            machine.select_storage()
        elif choice == "7":
            machine.show_catalog()
        elif choice == "8":
            machine.add_game()
        elif choice == "9":
            machine.finalize_purchase()
            break
        elif choice == "10":
            print("Exiting the application...")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
