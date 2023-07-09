# Singelton Pattern

class RadioSettings:
    instance = None

    def __init__(self):
        self.volume = 50
        self.frequency = 101.5

    @staticmethod
    def getSettings():
        if not RadioSettings.instance:
            RadioSettings.instance = RadioSettings()
        return RadioSettings.instance


class Radio:
    def __init__(self):
        self.settings = RadioSettings.getSettings()

    def setVolume(self, volume):
        self.settings.volume = volume

    def setFrequency(self, frequency):
        self.settings.frequency = frequency

    def printSettings(self):
        print(f"Volume: {self.settings.volume}")
        print(f"Frequency: {self.settings.frequency}")

# Usage
def demo():
    radio1 = Radio()
    radio1.printSettings()

    radio2 = Radio()
    radio2.setVolume(70)
    radio2.setFrequency(92.3)

    radio1.printSettings()
    radio2.printSettings()
