import random
from model import FakeLight ,HomeBuilder
    
def build_virtual_home(room=4):
    config = HomeBuilder("Tony Stark Home")
    topLight = FakeLight("Top Wall Light",consumption=100)    
    floorLight = FakeLight("Bottom Ligth",consumption=200)
    leftLight = FakeLight("Left Bottom",consumption=20)
    rightLight = FakeLight("Right Bottom",consumption=100)
    
    for roomId in range(1,room+1):
        config.with_device(FakeLight(f"Light N°{roomId}"))
        
    return config.build()