# Singleton Pattern


class RadioSettings:
    _instance: "RadioSettings | None" = None

    def __init__(self):
        self.volume = 50
        self.frequency = 101.5

    @classmethod
    def get_settings(cls) -> "RadioSettings":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


class Radio:
    def __init__(self):
        self.settings = RadioSettings.get_settings()

    def set_volume(self, volume: int):
        self.settings.volume = volume

    def set_frequency(self, frequency: float):
        self.settings.frequency = frequency

    def print_settings(self):
        print(f"Volume: {self.settings.volume}, Frequency: {self.settings.frequency}")


# Usage
def demo():
    radio1 = Radio()
    radio1.print_settings()  # Output: Volume: 50, Frequency: 101.5

    radio2 = Radio()
    radio2.set_volume(70)
    radio2.set_frequency(92.3)

    # Both radios share the same settings object
    radio1.print_settings()  # Output: Volume: 70, Frequency: 92.3
    radio2.print_settings()  # Output: Volume: 70, Frequency: 92.3
