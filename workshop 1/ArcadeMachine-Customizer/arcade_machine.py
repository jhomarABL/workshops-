"""
This module defines the ArcadeMachine class with options for selecting materials,
customizing appearance, modifying controls, configuring sound, and adding storage,
as well as managing games.

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

import re



class ArcadeMachine:
    """
    This class represents a customizable arcade machine with options to select materials,
    add games, customize appearance, modify controls, configure sound, and add storage.
    """

    def __init__(self):
        """
        Initializes the attributes of the arcade machine.
        """
        self.material = None
        self.selected_games = []
        self.customer_info = {}
        self.game_catalog = {
            "001": ("Street Fighter II", "Arcade"),
            "002": ("Pac-Man", "Arcade"),
            "003": ("Donkey Kong", "Arcade"),
            "004": ("Space Invaders", "Arcade"),
            "005": ("Galaga", "Arcade"),
            "006": ("Super Mario Bros.", "NES"),
            "007": ("The Legend of Zelda", "NES"),
            "008": ("Metroid", "NES"),
            "009": ("Contra", "NES"),
            "010": ("Mega Man 2", "NES"),
            "011": ("Sonic the Hedgehog", "Sega Genesis"),
            "012": ("Streets of Rage", "Sega Genesis"),
            "013": ("Altered Beast", "Sega Genesis"),
            "014": ("Golden Axe", "Sega Genesis"),
            "015": ("Shinobi", "Sega Genesis"),
            "016": ("Final Fantasy VII", "PlayStation"),
            "017": ("Metal Gear Solid", "PlayStation"),
            "018": ("Castlevania: Symphony of the Night", "PlayStation"),
            "019": ("Gran Turismo", "PlayStation"),
            "020": ("Tekken 3", "PlayStation"),
            "021": ("Halo: Combat Evolved", "Xbox"),
            "022": ("Fable", "Xbox"),
            "023": ("Ninja Gaiden", "Xbox"),
            "024": ("Gears of War", "Xbox 360"),
            "025": ("Forza Motorsport 2", "Xbox 360"),
            "026": ("The Elder Scrolls V: Skyrim", "PC"),
            "027": ("Half-Life 2", "PC"),
            "028": ("Portal", "PC"),
            "029": ("Counter-Strike", "PC"),
            "030": ("World of Warcraft", "PC"),
            "031": ("The Legend of Zelda: Breath of the Wild", "Switch"),
            "032": ("Super Mario Odyssey", "Switch"),
            "033": ("Animal Crossing: New Horizons", "Switch"),
            "034": ("Splatoon 2", "Switch"),
            "035": ("Xenoblade Chronicles 2", "Switch"),
            "036": ("Super Metroid", "SNES"),
            "037": ("Chrono Trigger", "SNES"),
            "038": ("EarthBound", "SNES"),
            "039": ("Donkey Kong Country", "SNES"),
            "040": ("Secret of Mana", "SNES"),
            "041": ("Super Mario World", "SNES"),
            "042": ("The Legend of Zelda: A Link to the Past", "SNES"),
            "043": ("Super Punch-Out!!", "SNES"),
            "044": ("Star Fox", "SNES"),
            "045": ("F-Zero", "SNES"),
            "046": ("Final Fantasy VI", "SNES"),
            "047": ("Super Mario Kart", "SNES"),
            "048": ("Donkey Kong Country 2: Diddy’s Kong Quest", "SNES"),
            "049": ("Tales of Symphonia", "GameCube"),
            "050": ("Metroid Prime", "GameCube"),
            "051": ("The Legend of Zelda: The Wind Waker", "GameCube"),
            "052": ("Super Smash Bros. Melee", "GameCube"),
            "053": ("Luigi's Mansion", "GameCube"),
            "054": ("Halo 2", "Xbox"),
            "055": ("Burnout 3: Takedown", "Xbox"),
            "056": ("Star Wars: Knights of the Old Republic", "Xbox"),
            "057": ("Morrowind", "Xbox"),
            "058": ("Jet Set Radio Future", "Xbox"),
            "059": ("Gran Turismo 4", "PlayStation 2"),
            "060": ("Metal Gear Solid 3: Snake Eater", "PlayStation 2"),
            "061": ("God of War II", "PlayStation 2"),
            "062": ("Kingdom Hearts", "PlayStation 2"),
            "063": ("Jak and Daxter: The Precursor Legacy", "PlayStation 2"),
            "064": ("Ratchet & Clank", "PlayStation 2"),
            "065": ("Silent Hill 2", "PlayStation 2"),
            "066": ("Grand Theft Auto III", "PlayStation 2"),
            "067": ("Tekken Tag Tournament", "PlayStation 2"),
            "068": ("Persona 4", "PlayStation 2"),
            "069": ("Burnout Revenge", "Xbox 360"),
            "070": ("Mass Effect", "Xbox 360"),
            "071": ("Dead Space", "Xbox 360"),
            "072": ("BioShock Infinite", "Xbox 360"),
            "073": ("Red Dead Redemption 2", "Xbox One"),
            "074": ("Forza Horizon 4", "Xbox One"),
            "075": ("Gears 5", "Xbox One"),
            "076": ("The Witcher 3: Wild Hunt", "Xbox One"),
            "077": ("Horizon Zero Dawn", "PlayStation 4"),
            "078": ("Spider-Man", "PlayStation 4"),
            "079": ("God of War", "PlayStation 4"),
            "080": ("Bloodborne", "PlayStation 4"),
            "081": ("Final Fantasy XV", "PlayStation 4"),
            "082": ("The Last of Us Part II", "PlayStation 4"),
            "083": ("Gran Turismo Sport", "PlayStation 4"),
            "084": ("Uncharted 4: A Thief's End", "PlayStation 4"),
            "085": ("Persona 5", "PlayStation 4"),
            "086": ("Sekiro: Shadows Die Twice", "PlayStation 4"),
            "087": ("Death Stranding", "PlayStation 4"),
            "088": ("Ghost of Tsushima", "PlayStation 4"),
            "089": ("Super Mario 3D World", "Switch"),
            "090": ("The Legend of Zelda: Link's Awakening", "Switch"),
            "091": ("Fire Emblem: Three Houses", "Switch"),
            "092": ("Hades", "Switch"),
            "093": ("Celeste", "Switch"),
            "094": ("Stardew Valley", "Switch"),
            "095": ("Octopath Traveler", "Switch"),
            "096": ("Astral Chain", "Switch"),
            "097": ("Luigi's Mansion 3", "Switch"),
            "098": ("Xenoblade Chronicles Definitive Edition", "Switch"),
            "099": ("Metroid Dread", "Switch"),
            "100": ("Pokémon Sword", "Switch"),
            "101": ("Pokémon Shield", "Switch"),
            "102": ("Super Mario Kart 8 Deluxe", "Switch"),
            "103": ("The Legend of Zelda: Breath of the Wild", "Switch"),
            "104": ("Animal Crossing: New Horizons", "Switch"),
            "105": ("Super Smash Bros. Ultimate", "Switch"),
            "106": ("Among Us", "PC"),
            "107": ("PUBG", "PC"),
            "108": ("Call of Duty: Warzone", "PC"),
            "109": ("Clash Royale", "PC"),
            "110": ("Hearthstone", "PC"),
            "111": ("Final Fantasy XIV", "PC"),
            "112": ("Elden Ring", "PC"),
            "113": ("Cyberpunk 2077", "PC"),
            "114": ("Dota 2", "PC"),
            "115": ("League of Legends", "PC"),
            "116": ("Starcraft II", "PC"),
            "117": ("Counter-Strike: Global Offensive", "PC"),
            "118": ("Overwatch", "PC"),
            "119": ("Rainbow Six Siege", "PC"),
            "120": ("World of Warcraft: Shadowlands", "PC"),
 
           
            
        }
        self.appearance = None
        self.controls = None
        self.sound_system = None
        self.connectivity = None
        self.storage = None

    def select_material(self):
        """
        Allows the user to select the material for the arcade machine.

        This method presents options to choose between different materials and updates
        the material attribute based on the user's choice.

        """
        print("Select the material for the machine:")
        print("1. Wood")
        print("2. Aluminum")
        print("3. Carbon Fiber")
        choice = input("Enter the number of your choice: ")

        materials = {"1": "Wood", "2": "Aluminum", "3": "Carbon Fiber"}
        self.material = materials.get(choice, "Wood")
        print(f"You have selected: {self.material}")

    def select_appearance(self):
        """
        Allows the user to customize the appearance of the arcade machine.

        This method presents options to choose between different appearances and updates
        the appearance attribute based on the user's choice.


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
        Allows the user to modify the controls of the arcade machine.

        This method presents options to choose between different control configurations and
        updates the controls attribute based on the user's choice.

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
        Allows the user to modify the sound system of the arcade machine.

        This method presents options to choose between different sound systems and updates
        the sound_system attribute based on the user's choice.
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
        Allows the user to customize the connectivity options of the arcade machine.

        This method presents options to choose between different connectivity options and
        updates the connectivity attribute based on the user's choice.
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

        This method presents options to choose between different storage capacities and
        updates the storage attribute based on the user's choice.

        """
        print("Select the storage capacity of the machine:")
        print("1. 500 GB")
        print("2. 1 TB")
        print("3. 2 TB")
        choice = input("Enter the number of your choice: ")

        storage_options = {"1": "500 GB", "2": "1 TB", "3": "2 TB"}
        self.storage = storage_options.get(choice, "500 GB")
        print(f"You have selected: {self.storage} of storage")

    def show_catalog(self):
        """
        Displays the catalog of available games.

        This method prints out the list of games available for the arcade machine.

        """
        print("Available games:")
        for code, game in self.game_catalog.items():
            print(f"{code}: {game}")

    def add_game(self):
        """
        Allows the user to add games to the arcade machine by entering a game code.

        This method checks the validity of the entered game code and adds the corresponding
        game to the selected_games list if valid.

        """
        self.show_catalog()
        game_code = input("Enter the code of the game you want to add: ")

        game = self.game_catalog.get(game_code)
        if game:
            self.selected_games.append(game)
            print(f"{game} has been added to your machine.")
        else:
            print("Invalid game code.")

    def finalize_purchase(self):
        """
        Finalizes the purchase of the arcade machine and collects customer information.

        This method prompts the user to enter their name and address, validates the inputs,
        and then displays a summary of the purchase.
        """
        print("Finalize Purchase:")

        while True:
            name = input("Customer name (letters and spaces only): ")
            if re.match(r"^[A-Za-z\s]+$", name) and name.strip():
                self.customer_info["name"] = name
                break
            else:
                print(
                    "Invalid name. It must contain only letters and spaces and cannot be empty."
                )

        while True:
            address = input("Delivery address (minimum 5 characters): ")
            if len(address.strip()) >= 5:
                self.customer_info["address"] = address
                break
            else:
                print(
                    "Invalid address. It must be at least 5 characters long and cannot be empty."
                )

        print("Purchase finalized.")
        self.show_summary()

    def show_summary(self):
        """
        Displays a detailed summary of the purchase.

        This method prints out a summary of all selected options and customer information.
        """
        print("\n--- Purchase Summary ---")
        print(f"Material of the machine: {self.material}")
        print(f"Selected appearance: {self.appearance}")
        print(f"Selected controls: {self.controls}")
        print(f"Selected sound system: {self.sound_system}")
        print(f"Selected connectivity: {self.connectivity}")
        print(f"Selected storage: {self.storage}")
        print(
            f"Selected games: {', '.join(self.selected_games) if self.selected_games else 'None'}"
        )
        print(f"Customer: {self.customer_info.get('name')}")
        print(f"Delivery address: {self.customer_info.get('address')}")
        print("---------------------------\n")
