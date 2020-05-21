
from model import FakeLight ,HomeBuilder
from subject import Daddy

if __name__ == "__main__":
    
    # Building home stuffs
    config = HomeBuilder("Tony Stark Home")
    topLight = FakeLight("topLight",consumption=100)    
    floorLight = FakeLight("bottomLight",consumption=200)
    leftLight = FakeLight("leftWallLight",consumption=20)
    rightLight = FakeLight("rightWallLight",consumption=100)
    subject = Daddy()

    # Attaching devices to home
    home = config \
        .with_device(topLight) \
        .with_device(floorLight)\
        .with_device(leftLight)\
        .with_device(rightLight)\
        .with_subject(subject) \
        .build()

    # Display states and possible actions
    home.display()

    # Run the first possible actions  and display the new state
    actions = home.get_possible_actions()
    home.interact(actions[0])
    home.display()