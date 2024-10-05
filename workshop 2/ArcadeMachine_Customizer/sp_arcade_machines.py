"""
This module contains abstract and concrete class definitions for various types of arcade machines.

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

from abstract_arcade_machine import AbstractArcadeMachine


class DanceRevolution(AbstractArcadeMachine):
    """
    Represents a Dance Revolution arcade machine with specific customization options and functionalities.
    """

    def __init__(self):
        """
        Initializes the DanceRevolution machine with default specifications.
        """
        super().__init__()
        self.difficulties = ["Easy", "Medium", "Hard", "Expert"]
        self.arrow_cardinalities = ["Up", "Down", "Left", "Right"]
        self.controls_price = 500
        self.base_price = 2000
        self.dimensions = "200x100x150 cm"
        self.weight = 150  # in kg
        self.processors = "Dual-core 2.5 GHz"
        self.memory = "8 GB"
        self.power_consumption = 500  # in watts

    def select_material(self):
        """
        Allows the user to select the material for the Dance Revolution machine and adjusts specifications accordingly.
        """
        print("Select the material for the Dance Revolution machine:")
        print("1. Wood")
        print("2. Aluminum")
        print("3. Carbon Fiber")
        choice = input("Enter the number of your choice: ")

        materials = {"1": "Wood", "2": "Aluminum", "3": "Carbon Fiber"}
        self.material = materials.get(choice, "Wood")

        if self.material == "Wood":
            self.weight *= 1.1
            self.base_price *= 0.95
            self.power_consumption *= 1.15
        elif self.material == "Aluminum":
            self.weight *= 0.95
            self.base_price *= 1.1
        elif self.material == "Carbon Fiber":
            self.weight *= 0.85
            self.base_price *= 1.2
            self.power_consumption *= 0.9

        print(f"You have selected: {self.material}")

    def select_color(self):
        """
        Allows the user to select the color for the Dance Revolution machine.
        """
        self.color = input("Enter the color for your Dance Revolution machine: ")
        print(f"You have selected the color: {self.color}")

    def add_game(self, game, definition):
        """
        Adds a compatible dance game to the Dance Revolution machine.

        Args:
            game (VideoGame): The game to be added.
            definition (str): The definition quality (e.g., Standard, High).
        """
        if "Dance" in game.category:
            self.selected_games.append(game)
            self.base_price += game.price
            print(
                f"{game.name} has been added to your machine in {definition} definition."
            )
        else:
            print(f"{game.name} is not compatible with the Dance Revolution machine.")

    def show_summary(self):
        """
        Displays a summary of the Dance Revolution machine's current configuration.
        """
        print("\n--- Dance Revolution Machine Summary ---")
        print(f"Material: {self.material}")
        print(f"Color: {self.color}")
        print(f"Dimensions: {self.dimensions}")
        print(f"Weight: {self.weight} kg")
        print(f"Power Consumption: {self.power_consumption} watts")
        print(f"Memory: {self.memory}")
        print(f"Processors: {self.processors}")
        print(f"Base Price: ${self.base_price}")
        print(f"Difficulties: {', '.join(self.difficulties)}")
        print(f"Arrow Cardinalities: {', '.join(self.arrow_cardinalities)}")
        print(f"Controls Price: ${self.controls_price}")
        print(f"Appearance: {self.appearance}")
        print(f"Controls: {self.controls}")
        print(f"Sound System: {self.sound_system}")
        print(f"Connectivity: {self.connectivity}")
        print(f"Storage: {self.storage}")

    def get_category(self):
        """
        Retrieves the category of the Dance Revolution machine.

        Returns:
            str: The category "Dance".
        """
        return "Dance"


class ClassicalArcade(AbstractArcadeMachine):
    """
    Represents a Classical Arcade machine with specific customization options and functionalities.
    """

    def __init__(self):
        """
        Initializes the ClassicalArcade machine with default specifications.
        """
        super().__init__()
        self.base_price = 1500
        self.dimensions = "150x80x180 cm"
        self.weight = 100  # in kg
        self.processors = "Single-core 2.0 GHz"
        self.memory = "4 GB"
        self.power_consumption = 300  # in watts

    def select_material(self):
        """
        Allows the user to select the material for the Classical Arcade machine and adjusts specifications accordingly.
        """
        print("Select the material for the Classical Machine:")
        print("1. Wood")
        print("2. Aluminum")
        print("3. Carbon Fiber")
        choice = input("Enter the number of your choice: ")

        materials = {"1": "Wood", "2": "Aluminum", "3": "Carbon Fiber"}
        self.material = materials.get(choice, "Wood")

        if self.material == "Wood":
            self.weight *= 1.1
            self.base_price *= 0.95
            self.power_consumption *= 1.15
        elif self.material == "Aluminum":
            self.weight *= 0.95
            self.base_price *= 1.1
        elif self.material == "Carbon Fiber":
            self.weight *= 0.85
            self.base_price *= 1.2
            self.power_consumption *= 0.9

        print(f"You have selected: {self.material}")

    def select_color(self):
        """
        Allows the user to select the color for the Classical Arcade machine.
        """
        self.color = input("Enter the color for your Classical Arcade machine: ")
        print(f"You have selected the color: {self.color}")

    def add_game(self, game, definition):
        """
        Adds a compatible classic game to the Classical Arcade machine.

        Args:
            game (VideoGame): The game to be added.
            definition (str): The definition quality (e.g., Standard, High).
        """
        if "Classic" in game.category:
            self.selected_games.append(game)
            self.base_price += game.price
            print(
                f"{game.name} has been added to your Classical Arcade machine in {definition} definition."
            )
        else:
            print(f"{game.name} is not compatible with the Classical Arcade machine.")

    def show_summary(self):
        """
        Displays a summary of the Classical Arcade machine's current configuration.
        """
        print("\n--- Classical Arcade Machine Summary ---")
        print(f"Material: {self.material}")
        print(f"Color: {self.color}")
        print(f"Dimensions: {self.dimensions}")
        print(f"Weight: {self.weight} kg")
        print(f"Power Consumption: {self.power_consumption} watts")
        print(f"Memory: {self.memory}")
        print(f"Processors: {self.processors}")
        print(f"Base Price: ${self.base_price}")
        print(f"Appearance: {self.appearance}")
        print(f"Controls: {self.controls}")
        print(f"Sound System: {self.sound_system}")
        print(f"Connectivity: {self.connectivity}")
        print(f"Storage: {self.storage}")

    def get_category(self):
        """
        Retrieves the category of the Classical Arcade machine.

        Returns:
            str: The category "Classic".
        """
        return "Classic"

    def make_vibration(self):
        """
        Triggers a vibration effect for the Classical Arcade machine.
        """
        print("The Classical Arcade machine is vibrating!")

    def sound_record_alert(self):
        """
        Alerts that the Classical Arcade machine is recording sound.
        """
        print("Alert: The Classical Arcade machine is recording sound!")


class VirtualRealityMachine(AbstractArcadeMachine):
    """
    Represents a Virtual Reality arcade machine with specific customization options and functionalities.
    """

    def __init__(self):
        """
        Initializes the VirtualRealityMachine with default specifications.
        """
        super().__init__()
        self.base_price = 3000
        self.dimensions = "180x120x180 cm"
        self.weight = 120  # in kg
        self.processors = "Quad-core 3.2 GHz"
        self.memory = "16 GB"
        self.power_consumption = 600  # in watts
        self.glasses_type = None
        self.glasses_resolution = None
        self.glasses_price = 800

    def select_material(self):
        """
        Allows the user to select the material for the Virtual Reality machine and adjusts specifications accordingly.
        """
        print("Select the material for the Virtual Reality Machine:")
        print("1. Wood")
        print("2. Aluminum")
        print("3. Carbon Fiber")
        choice = input("Enter the number of your choice: ")

        materials = {"1": "Wood", "2": "Aluminum", "3": "Carbon Fiber"}
        self.material = materials.get(choice, "Wood")

        if self.material == "Wood":
            self.weight *= 1.1
            self.base_price *= 0.95
            self.power_consumption *= 1.15
        elif self.material == "Aluminum":
            self.weight *= 0.95
            self.base_price *= 1.1
        elif self.material == "Carbon Fiber":
            self.weight *= 0.85
            self.base_price *= 1.2
            self.power_consumption *= 0.9

        print(f"You have selected: {self.material}")

    def select_color(self):
        """
        Allows the user to select the color for the Virtual Reality machine.
        """
        self.color = input("Enter the color for your Virtual Reality Machine: ")
        print(f"You have selected the color: {self.color}")

    def select_glasses(self):
        """
        Allows the user to select the type of VR glasses and adjusts specifications accordingly.
        """
        print("Select the type of VR glasses:")
        print("1. Basic Glasses")
        print("2. Advanced Glasses")
        choice = input("Enter the number of your choice: ")

        glasses_types = {"1": "Basic Glasses", "2": "Advanced Glasses"}
        self.glasses_type = glasses_types.get(choice, "Basic Glasses")

        if self.glasses_type == "Basic Glasses":
            self.glasses_price = 800
            self.glasses_resolution = "1080p"
        elif self.glasses_type == "Advanced Glasses":
            self.glasses_price = 1200
            self.glasses_resolution = "4K"

        self.base_price += self.glasses_price
        print(
            f"You have selected {self.glasses_type} with {self.glasses_resolution} resolution."
        )

    def add_game(self, game, definition):
        """
        Adds a compatible virtual reality game to the Virtual Reality machine.

        Args:
            game (VideoGame): The game to be added.
            definition (str): The definition quality (e.g., Standard, High).
        """
        if "VirtualReality" in game.category:
            self.selected_games.append(game)
            self.base_price += game.price
            print(
                f"{game.name} has been added to your Virtual Reality machine in {definition} definition."
            )
        else:
            print(f"{game.name} is not compatible with the Virtual Reality machine.")

    def show_summary(self):
        """
        Displays a summary of the Virtual Reality machine's current configuration.
        """
        print("\n--- Virtual Reality Machine Summary ---")
        print(f"Material: {self.material}")
        print(f"Color: {self.color}")
        print(f"Dimensions: {self.dimensions}")
        print(f"Weight: {self.weight} kg")
        print(f"Power Consumption: {self.power_consumption} watts")
        print(f"Memory: {self.memory}")
        print(f"Processors: {self.processors}")
        print(f"Base Price: ${self.base_price}")
        print(f"VR Glasses: {self.glasses_type}")
        print(f"Glasses Resolution: {self.glasses_resolution}")
        print(f"Appearance: {self.appearance}")
        print(f"Controls: {self.controls}")
        print(f"Sound System: {self.sound_system}")
        print(f"Connectivity: {self.connectivity}")
        print(f"Storage: {self.storage}")

    def get_category(self):
        """
        Retrieves the category of the Virtual Reality machine.

        Returns:
            str: The category "VirtualReality".
        """
        return "VirtualReality"


class ShootingMachine(AbstractArcadeMachine):
    """
    Represents a Shooting arcade machine with specific customization options and functionalities.
    """

    def __init__(self):
        """
        Initializes the ShootingMachine with default specifications.
        """
        super().__init__()
        self.base_price = 2200
        self.dimensions = "180x100x160 cm"
        self.weight = 140  # in kg
        self.processors = "Dual-core 2.8 GHz"
        self.memory = "8 GB"
        self.power_consumption = 450  # in watts
        self.weapon_type = None

    def select_material(self):
        """
        Allows the user to select the material for the Shooting machine and adjusts specifications accordingly.
        """
        print("Select the material for the Shooting Machine:")
        print("1. Wood")
        print("2. Aluminum")
        print("3. Carbon Fiber")
        choice = input("Enter the number of your choice: ")

        materials = {"1": "Wood", "2": "Aluminum", "3": "Carbon Fiber"}
        self.material = materials.get(choice, "Wood")

        if self.material == "Wood":
            self.weight *= 1.1
            self.base_price *= 0.95
            self.power_consumption *= 1.15
        elif self.material == "Aluminum":
            self.weight *= 0.95
            self.base_price *= 1.1
        elif self.material == "Carbon Fiber":
            self.weight *= 0.85
            self.base_price *= 1.2
            self.power_consumption *= 0.9

        print(f"You have selected: {self.material}")

    def select_color(self):
        """
        Allows the user to select the color for the Shooting machine.
        """
        self.color = input("Enter the color for your Shooting Machine: ")
        print(f"You have selected the color: {self.color}")

    def select_weapon_type(self):
        """
        Allows the user to select the type of weapon for the Shooting machine.
        """
        print("Select the weapon type for the Shooting Machine:")
        print("1. Laser Gun")
        print("2. Rifle")
        print("3. Dual Pistols")
        choice = input("Enter the number of your choice: ")

        weapon_types = {"1": "Laser Gun", "2": "Rifle", "3": "Dual Pistols"}
        self.weapon_type = weapon_types.get(choice, "Laser Gun")
        print(f"You have selected: {self.weapon_type}")

    def add_game(self, game, definition):
        """
        Adds a compatible shooting game to the Shooting machine.

        Args:
            game (VideoGame): The game to be added.
            definition (str): The definition quality (e.g., Standard, High).
        """
        if "Shooting" in game.category:
            self.selected_games.append(game)
            self.base_price += game.price
            print(
                f"{game.name} has been added to your Shooting Machine in {definition} definition."
            )
        else:
            print(f"{game.name} is not compatible with the Shooting Machine.")

    def show_summary(self):
        """
        Displays a summary of the Shooting machine's current configuration.
        """
        print("\n--- Shooting Machine Summary ---")
        print(f"Material: {self.material}")
        print(f"Color: {self.color}")
        print(f"Dimensions: {self.dimensions}")
        print(f"Weight: {self.weight} kg")
        print(f"Power Consumption: {self.power_consumption} watts")
        print(f"Memory: {self.memory}")
        print(f"Processors: {self.processors}")
        print(f"Base Price: ${self.base_price}")
        print(f"Weapon Type: {self.weapon_type}")
        print(f"Selected games: {', '.join([game.name for game in self.selected_games])}")
        print(f"Appearance: {self.appearance}")
        print(f"Controls: {self.controls}")
        print(f"Sound System: {self.sound_system}")
        print(f"Connectivity: {self.connectivity}")
        print(f"Storage: {self.storage}")

    def get_category(self):
        """
        Retrieves the category of the Shooting machine.

        Returns:
            str: The category "Shooting".
        """
        return "Shooting"


class RacingMachine(AbstractArcadeMachine):
    """
    Represents a Racing arcade machine with specific customization options and functionalities.
    """

    def __init__(self):
        """
        Initializes the RacingMachine with default specifications.
        """
        super().__init__()
        self.base_price = 2500
        self.dimensions = "200x120x180 cm"
        self.weight = 180  # in kg
        self.processors = "Quad-core 3.0 GHz"
        self.memory = "12 GB"
        self.power_consumption = 550  # in watts
        self.control_type = None

    def select_material(self):
        """
        Allows the user to select the material for the Racing machine and adjusts specifications accordingly.
        """
        print("Select the material for the Racing Machine:")
        print("1. Wood")
        print("2. Aluminum")
        print("3. Carbon Fiber")
        choice = input("Enter the number of your choice: ")

        materials = {"1": "Wood", "2": "Aluminum", "3": "Carbon Fiber"}
        self.material = materials.get(choice, "Wood")

        if self.material == "Wood":
            self.weight *= 1.1
            self.base_price *= 0.95
            self.power_consumption *= 1.15
        elif self.material == "Aluminum":
            self.weight *= 0.95
            self.base_price *= 1.1
        elif self.material == "Carbon Fiber":
            self.weight *= 0.85
            self.base_price *= 1.2
            self.power_consumption *= 0.9

        print(f"You have selected: {self.material}")

    def select_color(self):
        """
        Allows the user to select the color for the Racing machine.
        """
        self.color = input("Enter the color for your Racing Machine: ")
        print(f"You have selected the color: {self.color}")

    def select_controls(self):
        """
        Allows the user to select the control configuration for the Racing machine.
        """
        print("Select the control configuration for the Racing Machine:")
        print("1. Steering Wheel and Pedals")
        print("2. Arcade Stick")
        choice = input("Enter the number of your choice: ")

        controls = {"1": "Steering Wheel and Pedals", "2": "Arcade Stick"}
        self.control_type = controls.get(choice, "Steering Wheel and Pedals")
        print(f"You have selected: {self.control_type}")

    def add_game(self, game, definition):
        """
        Adds a compatible racing game to the Racing machine.

        Args:
            game (VideoGame): The game to be added.
            definition (str): The definition quality (e.g., Standard, High).
        """
        if "Racing" in game.category:
            self.selected_games.append(game)
            self.base_price += game.price
            print(
                f"{game.name} has been added to your Racing Machine in {definition} definition."
            )
        else:
            print(f"{game.name} is not compatible with the Racing Machine.")

    def show_summary(self):
        """
        Displays a summary of the Racing machine's current configuration.
        """
        print("\n--- Racing Machine Summary ---")
        print(f"Material: {self.material}")
        print(f"Color: {self.color}")
        print(f"Dimensions: {self.dimensions}")
        print(f"Weight: {self.weight} kg")
        print(f"Power Consumption: {self.power_consumption} watts")
        print(f"Memory: {self.memory}")
        print(f"Processors: {self.processors}")
        print(f"Base Price: ${self.base_price}")
        print(f"Control Type: {self.control_type}")
        print(f"Appearance: {self.appearance}")
        print(f"Controls: {self.controls}")
        print(f"Sound System: {self.sound_system}")
        print(f"Connectivity: {self.connectivity}")
        print(f"Storage: {self.storage}")

    def get_category(self):
        """
        Retrieves the category of the Racing machine.

        Returns:
            str: The category "Racing".
        """
        return "Racing"
