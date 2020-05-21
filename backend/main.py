
from model import FakeLight ,HomeBuilder

if __name__ == "__main__":
    
    # Building home stuffs
    config = HomeBuilder("Tony Stark Home")
    topLight = FakeLight("Top Wall Light",consumption=100)    
    floorLight = FakeLight("Bottom Ligth",consumption=200)
    leftLight = FakeLight("Left Bottom",consumption=20)
    rightLight = FakeLight("Right Bottom",consumption=100)

    # Attaching devices to home
    home = config \
        .with_device(topLight) \
        .with_device(floorLight)\
        .with_device(leftLight)\
        .with_device(rightLight)\
        .build()

    # Display states and possible actions
    home.display()

    # Run the first possible actions  and display the new state
    actions = home.get_possible_actions()
    home.interact(actions[0])
    home.display()