

from arcade_machine_factory import ArcadeMachineFactory
from videogame import VideoGame

def main():
    print("Select a machine type:")
    print("1. Dance Revolution")
    print("2. Classical Arcade")
    print("3. Shooting Machine")
    print("4. Racing Machine")
    print("5. Virtual Reality Machine")
    
    choice = input("Enter the number of your choice: ")
    
    machine_types = {
        "1": "Dance Revolution",
        "2": "Classical Arcade",
        "3": "Shooting Machine",
        "4": "Racing Machine",
        "5": "Virtual Reality Machine"
    }
    
    machine_type = machine_types.get(choice)
    if machine_type:
        machine = ArcadeMachineFactory.create_machine(machine_type)
    else:
        print("Invalid choice. Exiting.")
        return
    
    available_games = [
        VideoGame("Dance Dance Revolution", "Konami", "Realista", "Dance", 60, 1998),
        VideoGame("Just Dance 2021", "Ubisoft", "Realista", "Dance", 60, 2020),
        VideoGame("Dance Central", "Harmonix", "Realista", "Dance", 50, 2010), 
        VideoGame("Beat Saber", "Beat Games", "Realista", "VirtualReality", 30, 2018),
        VideoGame("Virtual Reality Dance", "VR Studio", "3D", "VirtualReality", 40, 2021),
        VideoGame("Mario Kart 8 Deluxe", "Nintendo", "Realista", "Racing", 60, 2017),
        VideoGame("Gran Turismo 7", "Polyphony Digital", "Realista", "Racing", 60, 2022),
        VideoGame("Need for Speed Heat", "Ghost Games", "Realista", "Racing", 60, 2019),
        VideoGame("Forza Horizon 5", "Playground Games", "Realista", "Racing", 60, 2021),
        VideoGame("Wipeout Omega Collection", "Sony XDEV", "Realista", "Racing", 40, 2017),
        VideoGame("Overwatch", "Blizzard Entertainment", "Realista", "Shooting", 40, 2016),
        VideoGame("Call of Duty: Warzone", "Infinity Ward", "Realista", "Shooting", 0, 2020),
        VideoGame("DOOM Eternal", "id Software", "Realista", "Shooting", 60, 2020),
        VideoGame("Battlefield V", "DICE", "Realista", "Shooting", 60, 2018),
        VideoGame("Apex Legends", "Respawn Entertainment", "Realista", "Shooting", 0, 2019),
        VideoGame("Counter-Strike: Global Offensive", "Valve", "Realista", "Shooting", 0, 2012),
        VideoGame("Left 4 Dead 2", "Valve", "Realista", "Shooting", 20, 2009),
        VideoGame("Splatoon 2", "Nintendo", "Colorido", "Shooting", 60, 2017),
        VideoGame("Rage 2", "Avalanche Studios", "Realista", "Shooting", 60, 2019),
        VideoGame("Destiny 2", "Bungie", "Realista", "Shooting", 0, 2017),
        VideoGame("Mario Kart Wii", "Nintendo", "Colorido", "Racing", 50, 2008),
        VideoGame("F1 2021", "Codemasters", "Realista", "Racing", 60, 2021),
        VideoGame("Dirt 5", "Codemasters", "Realista", "Racing", 60, 2020),
        VideoGame("Rocket League", "Psyonix", "Realista", "Racing", 20, 2015),
        VideoGame("Gran Turismo Sport", "Polyphony Digital", "Realista", "Racing", 60, 2017),
        VideoGame("Trackmania", "Nadeo", "Colorido", "Racing", 30, 2020),
        VideoGame("Super Bomberman R Online", "Konami", "Colorido", "Shooting", 30, 2021),
        VideoGame("Dead by Daylight", "Behaviour Interactive", "Realista", "Shooting", 20, 2016),
        VideoGame("Borderlands 3", "Gearbox Software", "Cómic", "Shooting", 60, 2019),
        VideoGame("Unturned", "Smartly Dressed Games", "Pixel Art", "Shooting", 0, 2014),
        VideoGame("Gunfire Reborn", "Tianyou Games", "Cómic", "Shooting", 20, 2021),
        VideoGame("Wreckfest", "Bugbear Entertainment", "Realista", "Racing", 40, 2018),
        VideoGame("CarX Drift Racing Online", "CarX Technologies", "Realista", "Racing", 15, 2017),
        VideoGame("Trials Rising", "RedLynx", "Realista", "Racing", 40, 2019),
        VideoGame("Sonic & All-Stars Racing Transformed", "Sumo Digital", "Colorido", "Racing", 30, 2012),
        VideoGame("Team Sonic Racing", "Sumo Digital", "Colorido", "Racing", 40, 2019),
        VideoGame("Rising Storm 2: Vietnam", "Antimatter Games", "Realista", "Shooting", 30, 2017),
        VideoGame("Metro Exodus", "4A Games", "Realista", "Shooting", 60, 2019),
        VideoGame("Escape from Tarkov", "Battlestate Games", "Realista", "Shooting", 0, 2020),
        VideoGame("Ghost Recon Breakpoint", "Ubisoft", "Realista", "Shooting", 60, 2019),
        VideoGame("Valorant", "Riot Games", "Realista", "Shooting", 0, 2020),
        VideoGame("Mario Kart 7", "Nintendo", "Colorido", "Racing", 40, 2011),
        VideoGame("F1 2020", "Codemasters", "Realista", "Racing", 60, 2020),  
        VideoGame("Pac-Man", "Namco", "2D", "Classic", 25, 1980),
        VideoGame("Space Invaders", "Taito", "Pixel Art", "Classic", 20, 1978),
        VideoGame("Donkey Kong", "Nintendo", "2D", "Classic", 30, 1981),
        VideoGame("Galaga", "Namco", "Pixel Art", "Classic", 25, 1981),
        VideoGame("Street Fighter II", "Capcom", "2D", "Classic", 40, 1991),
        VideoGame("Super Mario Bros.", "Nintendo", "Pixel Art", "Classic", 30, 1985),
        VideoGame("Tetris", "Alexey Pajitnov", "Pixel Art", "Classic", 15, 1984),
        VideoGame("Sonic the Hedgehog", "Sega", "2D", "Classic", 35, 1991),
        VideoGame("Mortal Kombat", "Midway Games", "2D", "Classic", 40, 1992),
        VideoGame("The Legend of Zelda", "Nintendo", "2D", "Classic", 45, 1986),

    ]

    while True:
        print("\n--- Main Menu ---")
        print("1. Select material")
        print("2. Select color")
        print("3. Customize appearance")
        print("4. Modify controls")
        print("5. Configure sound")
        print("6. Configure connectivity")
        print("7. Select storage")
        print("8. Add game to the machine")
        print("9. Show machine summary")
        print("10. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            machine.select_material()
        elif choice == "2":
            machine.select_color()
        elif choice == "3":
            machine.select_appearance()
        elif choice == "4":
            machine.select_controls()
        elif choice == "5":
            machine.select_sound_system()
        elif choice == "6":
            machine.select_connectivity()
        elif choice == "7":
            machine.select_storage()
        elif choice == "8":
            print(available_games)
            for game in available_games:
                if game.category == machine.get_category():  

                    # Dance Games
                    print(VideoGame("Dance Dance Revolution", "Konami", "Realistic", "Dance", 60, 1998))
                    print(VideoGame("Just Dance 2021", "Ubisoft", "Realistic", "Dance", 60, 2020))
                    print(VideoGame("Dance Central", "Harmonix", "Realistic", "Dance", 50, 2010))

                    # Virtual Reality Games
                    print(VideoGame("Beat Saber", "Beat Games", "Realistic", "VirtualReality", 30, 2018))
                    print(VideoGame("Virtual Reality Dance", "VR Studio", "3D", "VirtualReality", 40, 2021))

                    # Racing Games
                    print(VideoGame("Mario Kart 8 Deluxe", "Nintendo", "Realistic", "Racing", 60, 2017))
                    print(VideoGame("Gran Turismo 7", "Polyphony Digital", "Realistic", "Racing", 60, 2022))
                    print(VideoGame("Need for Speed Heat", "Ghost Games", "Realistic", "Racing", 60, 2019))
                    print(VideoGame("Forza Horizon 5", "Playground Games", "Realistic", "Racing", 60, 2021))
                    print(VideoGame("Wipeout Omega Collection", "Sony XDEV", "Realistic", "Racing", 40, 2017))

                    # Shooting Games
                    print(VideoGame("Overwatch", "Blizzard Entertainment", "Realistic", "Shooting", 40, 2016))
                    print(VideoGame("Call of Duty: Warzone", "Infinity Ward", "Realistic", "Shooting", 0, 2020))
                    print(VideoGame("DOOM Eternal", "id Software", "Realistic", "Shooting", 60, 2020))
                    print(VideoGame("Battlefield V", "DICE", "Realistic", "Shooting", 60, 2018))
                    print(VideoGame("Apex Legends", "Respawn Entertainment", "Realistic", "Shooting", 0, 2019))
                    print(VideoGame("Counter-Strike: Global Offensive", "Valve", "Realistic", "Shooting", 0, 2012))
                    print(VideoGame("Left 4 Dead 2", "Valve", "Realistic", "Shooting", 20, 2009))
                    print(VideoGame("Splatoon 2", "Nintendo", "Colorful", "Shooting", 60, 2017))
                    print(VideoGame("Rage 2", "Avalanche Studios", "Realistic", "Shooting", 60, 2019))
                    print(VideoGame("Destiny 2", "Bungie", "Realistic", "Shooting", 0, 2017))

                    # More Racing Games
                    print(VideoGame("Mario Kart Wii", "Nintendo", "Colorful", "Racing", 50, 2008))
                    print(VideoGame("F1 2021", "Codemasters", "Realistic", "Racing", 60, 2021))
                    print(VideoGame("Dirt 5", "Codemasters", "Realistic", "Racing", 60, 2020))
                    print(VideoGame("Rocket League", "Psyonix", "Realistic", "Racing", 20, 2015))
                    print(VideoGame("Gran Turismo Sport", "Polyphony Digital", "Realistic", "Racing", 60, 2017))
                    print(VideoGame("Trackmania", "Nadeo", "Colorful", "Racing", 30, 2020))

                    # More Shooting Games
                    print(VideoGame("Super Bomberman R Online", "Konami", "Colorful", "Shooting", 30, 2021))
                    print(VideoGame("Dead by Daylight", "Behaviour Interactive", "Realistic", "Shooting", 20, 2016))
                    print(VideoGame("Borderlands 3", "Gearbox Software", "Comic", "Shooting", 60, 2019))
                    print(VideoGame("Unturned", "Smartly Dressed Games", "Pixel Art", "Shooting", 0, 2014))
                    print(VideoGame("Gunfire Reborn", "Tianyou Games", "Comic", "Shooting", 20, 2021))
                    print(VideoGame("Wreckfest", "Bugbear Entertainment", "Realistic", "Racing", 40, 2018))
                    print(VideoGame("CarX Drift Racing Online", "CarX Technologies", "Realistic", "Racing", 15, 2017))
                    print(VideoGame("Trials Rising", "RedLynx", "Realistic", "Racing", 40, 2019))
                    print(VideoGame("Sonic & All-Stars Racing Transformed", "Sumo Digital", "Colorful", "Racing", 30, 2012))
                    print(VideoGame("Team Sonic Racing", "Sumo Digital", "Colorful", "Racing", 40, 2019))

                    # More Shooting Games
                    print(VideoGame("Rising Storm 2: Vietnam", "Antimatter Games", "Realistic", "Shooting", 30, 2017))
                    print(VideoGame("Metro Exodus", "4A Games", "Realistic", "Shooting", 60, 2019))
                    print(VideoGame("Escape from Tarkov", "Battlestate Games", "Realistic", "Shooting", 0, 2020))
                    print(VideoGame("Ghost Recon Breakpoint", "Ubisoft", "Realistic", "Shooting", 60, 2019))
                    print(VideoGame("Valorant", "Riot Games", "Realistic", "Shooting", 0, 2020))

                    # Classic Games
                    print(VideoGame("Pac-Man", "Namco", "2D", "Classic", 25, 1980))
                    print(VideoGame("Space Invaders", "Taito", "Pixel Art", "Classic", 20, 1978))
                    print(VideoGame("Donkey Kong", "Nintendo", "2D", "Classic", 30, 1981))
                    print(VideoGame("Galaga", "Namco", "Pixel Art", "Classic", 25, 1981))
                    print(VideoGame("Street Fighter II", "Capcom", "2D", "Classic", 40, 1991))
                    print(VideoGame("Super Mario Bros.", "Nintendo", "Pixel Art", "Classic", 30, 1985))
                    print(VideoGame("Tetris", "Alexey Pajitnov", "Pixel Art", "Classic", 15, 1984))
                    print(VideoGame("Sonic the Hedgehog", "Sega", "2D", "Classic", 35, 1991))
                    print(VideoGame("Mortal Kombat", "Midway Games", "2D", "Classic", 40, 1992))
                    print(VideoGame("The Legend of Zelda", "Nintendo", "2D", "Classic", 45, 1986))

                    
                    game_name = input("Enter the name of the game you want to add: ")
                    selected_game = next((game for game in available_games if game.name == game_name), None)
                    if selected_game:
                        definition = input("Enter the definition (Standard/High): ")
                        machine.add_game(selected_game, definition) 
                        break
                        
                    else:
                        print("Game not found.")
        elif choice == "9":
            machine.show_summary()
        elif choice == "10":
            print("Exiting the application...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
