
from model import FakeLight ,InteractiveHome

if __name__ == "__main__":
    
    home = InteractiveHome("Tony Stark Home")
    topLight = FakeLight("Top Living Romm",consumption=100)    
    floorLight = FakeLight("Bottom Living Romm",consumption=200)

    home.add_device(topLight)
    home.add_device(floorLight)
    home.display()

    actions = home.get_possible_actions()
    home.interact(actions[0])
    home.display()