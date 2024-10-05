from abc import ABC, abstractmethod


class AbstractArcadeMachine(ABC):
    def __init__(self):
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
        pass

    @abstractmethod
    def select_color(self):
        pass

    @abstractmethod
    def show_summary(self):
        pass

    def select_appearance(self):
        print("Select the appearance of the machine:")
        print("1. Classic")
        print("2. Modern")
        print("3. Customized")
        choice = input("Enter the number of your choice: ")

        appearances = {"1": "Classic", "2": "Modern", "3": "Customized"}
        self.appearance = appearances.get(choice, "Classic")
        print(f"You have selected the appearance: {self.appearance}")

    def select_controls(self):
        print("Select the control configuration:")
        print("1. Classic Controls (Joystick and Buttons)")
        print("2. Modern Controls (Stick and Buttons)")
        choice = input("Enter the number of your choice: ")

        controls = {"1": "Classic Controls", "2": "Modern Controls"}
        self.controls = controls.get(choice, "Classic Controls")
        print(f"You have selected: {self.controls}")

    def select_sound_system(self):
        print("Select the sound system:")
        print("1. Standard")
        print("2. Premium (Surround Sound)")
        choice = input("Enter the number of your choice: ")

        sound_systems = {"1": "Standard", "2": "Premium"}
        self.sound_system = sound_systems.get(choice, "Standard")
        print(f"You have selected the sound: {self.sound_system}")

    def select_connectivity(self):
        print("Select the connectivity options:")
        print("1. Wi-Fi")
        print("2. Bluetooth")
        print("3. Both")
        choice = input("Enter the number of your choice: ")

        connectivity_options = {"1": "Wi-Fi", "2": "Bluetooth", "3": "Both"}
        self.connectivity = connectivity_options.get(choice, "Wi-Fi")
        print(f"You have selected connectivity: {self.connectivity}")

    def select_storage(self):
        print("Select the storage capacity of the machine:")
        print("1. 500 GB")
        print("2. 1 TB")
        print("3. 2 TB")
        choice = input("Enter the number of your choice: ")

        storage_options = {"1": "500 GB", "2": "1 TB", "3": "2 TB"}
        self.storage = storage_options.get(choice, "500 GB")
        print(f"You have selected: {self.storage} of storage")

    def add_game(self, game, definition):
        if game.category != self.get_category():
            print(
                f"Cannot add {game.name}. It doesn't belong to the category {self.get_category()}."
            )
            return

        self.selected_games.append(game)
        self.base_price += game.price  
        print(f"{game.name} has been added to your machine in {definition} definition.")

    def remove_game(self, game):
        if game in self.selected_games:
            self.selected_games.remove(game)
            self.base_price -= game.price  
            print(f"{game.name} has been removed from your machine.")
        else:
            print(f"{game.name} not found in the selected games.")

    @abstractmethod
    def get_category(self):
        pass
