"""
This module contains the definition of the ArcadeMachineFactory class, which is responsible for creating instances of various arcade machine types based on user selection.

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

from sp_arcade_machines import (
    DanceRevolution,
    ClassicalArcade,
    ShootingMachine,
    RacingMachine,
    VirtualRealityMachine,
)


class ArcadeMachineFactory:
    """
    Factory class responsible for creating instances of different arcade machine types.
    """

    @staticmethod
    def create_machine(machine_type: str):
        """
        Creates and returns an instance of the specified arcade machine type.

        Args:
            machine_type (str): The type of arcade machine to create. 
                                Expected values are:
                                - "Dance Revolution"
                                - "Classical Arcade"
                                - "Shooting Machine"
                                - "Racing Machine"
                                - "Virtual Reality Machine"

        Returns:
            AbstractArcadeMachine: An instance of the requested arcade machine type.

        Raises:
            ValueError: If the provided machine_type does not match any known types.
        """
        if machine_type == "Dance Revolution":
            return DanceRevolution()
        elif machine_type == "Classical Arcade":
            return ClassicalArcade()
        elif machine_type == "Shooting Machine":
            return ShootingMachine()
        elif machine_type == "Racing Machine":
            return RacingMachine()
        elif machine_type == "Virtual Reality Machine":
            return VirtualRealityMachine()
        else:
            raise ValueError(f"Unknown machine type: {machine_type}")
