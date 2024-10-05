from sp_arcade_machines import (
    DanceRevolution,
    ClassicalArcade,
    ShootingMachine,
    RacingMachine,
    VirtualRealityMachine,
)


class ArcadeMachineFactory:
    @staticmethod
    def create_machine(machine_type):
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
