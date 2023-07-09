# Adapter Pattern

class SwissPowerPlug:
    def __init__(self):
        self.isPlugged = False
    
    def plugIn(self):
        self.isPlugged = True

class EuropeanPowerOutlet:
    def __init__(self):
        self.outletAvailable = True
    
    def plug(self, swissAdapter):
        if self.outletAvailable:
            swissAdapter.plugIn()
            self.outletAvailable = False

class SwissToEuropeanAdapter:
    def __init__(self, swissPlug):
        self.swissPlug = swissPlug
        self.swissPlug.plugIn()
    def plugIn(self):
        self.swissPlug.plugIn()

class SwissToEuropeanAdapterClient:
    def __init__(self):
        swissPlug = SwissPowerPlug()
        europeanOutlet = EuropeanPowerOutlet()
        adapter = SwissToEuropeanAdapter(swissPlug)
        europeanOutlet.plug(adapter)

# Usage
def demo():
    swissPlug = SwissPowerPlug()
    europeanOutlet = EuropeanPowerOutlet()
    adapter = SwissToEuropeanAdapter(swissPlug)
    europeanOutlet.plug(adapter)
