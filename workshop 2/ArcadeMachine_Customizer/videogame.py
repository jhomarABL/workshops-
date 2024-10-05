"""
This module contains the definition of the VideoGame class, which represents a video game with its essential attributes and basic behaviors.

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

class VideoGame:
    """
    Represents a video game with its essential attributes and provides methods to interact with them.
    """

    def __init__(
        self,
        name: str,
        creator_story: str,
        creator_graphics: str,
        category: str,
        price: float,
        year: int,
        definition: str = "Standard",
    ):
        """
        Initializes a new instance of VideoGame with the provided attributes.

        Args:
            name (str): The name of the video game.
            creator_story (str): The creator or developer of the game.
            creator_graphics (str): The type of graphics used in the game.
            category (str): The category or genre of the game (e.g., Dance, Racing, Shooting).
            price (float): The base price of the game.
            year (int): The release year of the game.
            definition (str, optional): The definition quality of the game, can be "Standard" or "High". Defaults to "Standard".

        Attributes:
            name (str): The name of the video game.
            creator_story (str): The creator or developer of the game.
            creator_graphics (str): The type of graphics used in the game.
            category (str): The category or genre of the game.
            price (float): The adjusted price of the game based on the definition.
            year (int): The release year of the game.
            definition (str): The definition quality of the game.
        """
        self.name = name
        self.creator_story = creator_story
        self.creator_graphics = creator_graphics
        self.category = category
        self.price = price * (1.1 if definition == "High" else 1)
        self.year = year
        self.definition = definition

    def __str__(self) -> str:
        """
        Returns a string representation of the video game, including its name, definition, price, category, and year.

        Returns:
            str: A string that represents the video game.
        """
        return f"{self.name} ({self.definition}): ${self.price:.2f}, Category: {self.category}, Year: {self.year}"
