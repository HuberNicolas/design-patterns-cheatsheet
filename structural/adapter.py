# Adapter Pattern


class EuropeanPlug:
    """The interface the European outlet expects (Type F, "Schuko")."""

    def round_pins(self) -> int:
        return 2


class SwissPlug:
    """An existing class with an incompatible interface (Type J)."""

    def pins(self) -> list[str]:
        return ["live", "neutral", "earth"]


class EuropeanPowerOutlet:
    def __init__(self):
        self.plugged_in: EuropeanPlug | None = None

    def plug(self, plug: EuropeanPlug):
        if plug.round_pins() != 2:
            raise ValueError("This plug does not fit")
        self.plugged_in = plug
        print("Power on")


class SwissToEuropeanAdapter(EuropeanPlug):
    """Wraps a SwissPlug and offers the EuropeanPlug interface."""

    def __init__(self, swiss_plug: SwissPlug):
        self.swiss_plug = swiss_plug

    def round_pins(self) -> int:
        # live and neutral are mapped to the two round pins, earth to the side clips
        return len([pin for pin in self.swiss_plug.pins() if pin != "earth"])


# Usage
def demo():
    outlet = EuropeanPowerOutlet()
    swiss_plug = SwissPlug()
    # outlet.plug(swiss_plug)  # fails: SwissPlug has no round_pins()
    outlet.plug(SwissToEuropeanAdapter(swiss_plug))  # Output: Power on
