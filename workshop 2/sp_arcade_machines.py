from abstract_arcade_machine import AbstractArcadeMachine


class DanceRevolution(AbstractArcadeMachine):
    def __init__(self):
        super().__init__()
        self.difficulties = ["Easy", "Medium", "Hard", "Expert"]
        self.arrow_cardinalities = ["Up", "Down", "Left", "Right"]
        self.controls_price = 500
        self.base_price = 2000
        self.dimensions = "200x100x150 cm"
        self.weight = 150
        self.processors = "Dual-core 2.5 GHz"
        self.memory = "8 GB"
        self.power_consumption = 500

    def select_material(self):
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
        self.color = input("Enter the color for your Dance Revolution machine: ")
        print(f"You have selected the color: {self.color}")

    def add_game(self, game, definition):

        if "Dance" in game.category:
            self.selected_games.append(game)
            self.base_price += game.price
            print(
                f"{game.name} has been added to your machine in {definition} definition."
            )
        else:
            print(f"{game.name} is not compatible with the Dance Revolution machine.")

    def show_summary(self):
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
        return "Dance"


class ClassicalArcade(AbstractArcadeMachine):
    def __init__(self):
        super().__init__()
        self.base_price = 1500
        self.dimensions = "150x80x180 cm"
        self.weight = 100
        self.processors = "Single-core 2.0 GHz"
        self.memory = "4 GB"
        self.power_consumption = 300

    def select_material(self):
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
        self.color = input("Enter the color for your Classical Arcade machine: ")
        print(f"You have selected the color: {self.color}")

    def add_game(self, game, definition):
        if "Classic" in game.category:
            self.selected_games.append(game)
            self.base_price += game.price
            print(
                f"{game.name} has been added to your Classical Arcade machine in {definition} definition."
            )
        else:
            print(f"{game.name} is not compatible with the Classical Arcade machine.")

    def show_summary(self):
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
        return "Classic"

    def make_vibration(self):
        print("The Classical Arcade machine is vibrating!")

    def sound_record_alert(self):
        print("Alert: The Classical Arcade machine is recording sound!")


class VirtualRealityMachine(AbstractArcadeMachine):
    def __init__(self):
        super().__init__()
        self.base_price = 3000
        self.dimensions = "180x120x180 cm"
        self.weight = 120
        self.processors = "Quad-core 3.2 GHz"
        self.memory = "16 GB"
        self.power_consumption = 600
        self.glasses_type = None
        self.glasses_resolution = None
        self.glasses_price = 800

    def select_material(self):
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
        self.color = input("Enter the color for your Virtual Reality Machine: ")
        print(f"You have selected the color: {self.color}")

    def select_glasses(self):
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
        if "VirtualReality" in game.category:  
            self.selected_games.append(game)
            self.base_price += game.price
            print(
                f"{game.name} has been added to your Virtual Reality machine in {definition} definition."
            )
            
        else:
            print(f"{game.name} is not compatible with the Virtual Reality machine.")

    def show_summary(self):
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
        

    def get_category(self):
        return "VirtualReality"


class ShootingMachine(AbstractArcadeMachine):
    def __init__(self):
        super().__init__()
        self.base_price = 2200
        self.dimensions = "180x100x160 cm"
        self.weight = 140  
        self.processors = "Dual-core 2.8 GHz"
        self.memory = "8 GB"
        self.power_consumption = 450  
        self.weapon_type = None

    def select_material(self):
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
        self.color = input("Enter the color for your Shooting Machine: ")
        print(f"You have selected the color: {self.color}")

    def select_weapon_type(self):
        print("Select the weapon type for the Shooting Machine:")
        print("1. Laser Gun")
        print("2. Rifle")
        print("3. Dual Pistols")
        choice = input("Enter the number of your choice: ")

        weapon_types = {"1": "Laser Gun", "2": "Rifle", "3": "Dual Pistols"}
        self.weapon_type = weapon_types.get(choice, "Laser Gun")
        print(f"You have selected: {self.weapon_type}")

    def add_game(self, game, definition):
        if "Shooting" in game.category:  
            self.selected_games.append(game)
            self.base_price += game.price
            print(
                f"{game.name} has been added to your Shooting Machine in {definition} definition."
            )
        else:
            print(f"{game.name} is not compatible with the Shooting Machine.")

    def show_summary(self):
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
        print(f"Selected games: {', '.join([game[0] for game in self.selected_games])}")

    def get_category(self):
        return "Shooting"


class RacingMachine(AbstractArcadeMachine):
    def __init__(self):
        super().__init__()
        self.base_price = 2500
        self.dimensions = "200x120x180 cm"
        self.weight = 180
        self.processors = "Quad-core 3.0 GHz"
        self.memory = "12 GB"
        self.power_consumption = 550
        self.control_type = None

    def select_material(self):
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
        self.color = input("Enter the color for your Racing Machine: ")
        print(f"You have selected the color: {self.color}")

    def select_controls(self):
        print("Select the control configuration for the Racing Machine:")
        print("1. Steering Wheel and Pedals")
        print("2. Arcade Stick")
        choice = input("Enter the number of your choice: ")

        controls = {"1": "Steering Wheel and Pedals", "2": "Arcade Stick"}
        self.control_type = controls.get(choice, "Steering Wheel and Pedals")
        print(f"You have selected: {self.control_type}")

    def add_game(self, game, definition):
        if "Racing" in game.category:
            self.selected_games.append(game)
            self.base_price += game.price
            print(
                f"{game.name} has been added to your Racing Machine in {definition} definition."
            )
        else:
            print(f"{game.name} is not compatible with the Racing Machine.")

    def show_summary(self):
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
        


    def get_category(self):
        return "Racing"
