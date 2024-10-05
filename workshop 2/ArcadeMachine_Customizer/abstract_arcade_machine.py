"""
This module contains the definition of the AbstractArcadeMachine class, which serves as the base class for all specific types of arcade machines.

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

Module Functionality:
- Defines the AbstractArcadeMachine abstract base class, which outlines the common properties and methods for all arcade machine types.
- Provides concrete implementations for selecting appearance, controls, sound system, connectivity, and storage.
- Implements methods to add and remove games, ensuring compatibility based on the machine's category.
- Enforces the implementation of essential methods like select_material, select_color, show_summary, and get_category in all subclasses.
"""

from abc import ABC, abstractmethod


class AbstractArcadeMachine(ABC):
    """
    Abstract base class representing a generic arcade machine. Defines the common attributes and methods that all specific arcade machine types must implement.
    """

    def __init__(self):
        """
        Initializes the AbstractArcadeMachine with default attributes.
        """
        self.material = None
        self.dimensions = None
        self.weight = None
        self.power_consumption = None
        self.memory = None
        self.processors = None
        self.base_price = None
        self.color = None
        self.selected_games = []
        self.appearance = None
        self.controls = None
        self.sound_system = None
        self.connectivity = None
        self.storage = None

    @abstractmethod
    def select_material(self):
        """
        Abstract method to allow the user to select the material of the arcade machine.
        Must be implemented by all subclasses.
        """
        pass

    @abstractmethod
    def select_color(self):
        """
        Abstract method to allow the user to select the color of the arcade machine.
        Must be implemented by all subclasses.
        """
        pass

    @abstractmethod
    def show_summary(self):
        """
        Abstract method to display a summary of the arcade machine's current configuration.
        Must be implemented by all subclasses.
        """
        pass

    def select_appearance(self):
        """
        Allows the user to select the appearance of the arcade machine.
        Updates the appearance attribute based on user input.
        """
        print("Select the appearance of the machine:")
        print("1. Classic")
        print("2. Modern")
        print("3. Customized")
        choice = input("Enter the number of your choice: ")

        appearances = {"1": "Classic", "2": "Modern", "3": "Customized"}
        self.appearance = appearances.get(choice, "Classic")
        print(f"You have selected the appearance: {self.appearance}")

    def select_controls(self):
        """
        Allows the user to select the control configuration of the arcade machine.
        Updates the controls attribute based on user input.
        """
        print("Select the control configuration:")
        print("1. Classic Controls (Joystick and Buttons)")
        print("2. Modern Controls (Stick and Buttons)")
        choice = input("Enter the number of your choice: ")

        controls = {"1": "Classic Controls", "2": "Modern Controls"}
        self.controls = controls.get(choice, "Classic Controls")
        print(f"You have selected: {self.controls}")

    def select_sound_system(self):
        """
        Allows the user to select the sound system of the arcade machine.
        Updates the sound_system attribute based on user input.
        """
        print("Select the sound system:")
        print("1. Standard")
        print("2. Premium (Surround Sound)")
        choice = input("Enter the number of your choice: ")

        sound_systems = {"1": "Standard", "2": "Premium"}
        self.sound_system = sound_systems.get(choice, "Standard")
        print(f"You have selected the sound: {self.sound_system}")

    def select_connectivity(self):
        """
        Allows the user to select the connectivity options of the arcade machine.
        Updates the connectivity attribute based on user input.
        """
        print("Select the connectivity options:")
        print("1. Wi-Fi")
        print("2. Bluetooth")
        print("3. Both")
        choice = input("Enter the number of your choice: ")

        connectivity_options = {"1": "Wi-Fi", "2": "Bluetooth", "3": "Both"}
        self.connectivity = connectivity_options.get(choice, "Wi-Fi")
        print(f"You have selected connectivity: {self.connectivity}")

    def select_storage(self):
        """
        Allows the user to select the storage capacity of the arcade machine.
        Updates the storage attribute based on user input.
        """
        print("Select the storage capacity of the machine:")
        print("1. 500 GB")
        print("2. 1 TB")
        print("3. 2 TB")
        choice = input("Enter the number of your choice: ")

        storage_options = {"1": "500 GB", "2": "1 TB", "3": "2 TB"}
        self.storage = storage_options.get(choice, "500 GB")
        print(f"You have selected: {self.storage} of storage")

    def add_game(self, game, definition):
        """
        Adds a compatible game to the arcade machine based on its category.
        Updates the base price accordingly.

        Args:
            game (VideoGame): The game to be added.
            definition (str): The definition quality of the game (e.g., Standard, High).
        """
        if game.category != self.get_category():
            print(
                f"Cannot add {game.name}. It doesn't belong to the category {self.get_category()}."
            )
            return

        self.selected_games.append(game)
        self.base_price += game.price
        print(f"{game.name} has been added to your machine in {definition} definition.")

    def remove_game(self, game):
        """
        Removes a game from the arcade machine if it exists in the selected_games list.
        Updates the base price accordingly.

        Args:
            game (VideoGame): The game to be removed.
        """
        if game in self.selected_games:
            self.selected_games.remove(game)
            self.base_price -= game.price
            print(f"{game.name} has been removed from your machine.")
        else:
            print(f"{game.name} not found in the selected games.")

    @abstractmethod
    def get_category(self):
        """
        Abstract method to retrieve the category of the arcade machine.
        Must be implemented by all subclasses.

        Returns:
            str: The category of the arcade machine.
        """
        pass
