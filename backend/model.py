import logging
from abc import ABC, abstractmethod

console = logging.StreamHandler()
logger = logging.Logger(__name__,logging.DEBUG)
logger.addHandler(console)

class IoTDevice(ABC):
    
    def __init__(self,name):
        self.name = name
        self._state = None
        self._settings = {}
    
    @abstractmethod
    def get_possible_actions(self):
        pass

    def get_state(self):
        return self._state
    
    def set_state(self,state_value):
        self._state = state_value
    
    @abstractmethod
    def reset(self):
        pass
    def __repr__(self):
        return self.name
    

class Action:
    
    def __init__(self,label,func):
        self.label = label
        self.runner = func
        
    def run(self, world):
        logger.debug(f"Running Action {self.label}")
        self.runner(world)
        
    def __repr__(self):
        return self.label
    
class FakeLight(IoTDevice):
    
    def __init__(self,name,consumption=0):
        super().__init__(name)
        self._state = 0
        self._settings = {"label":name,"consumption":consumption}
        self._actions = {
            0: Action("TurnOnLight",lambda world: self.turn_on()), 
            1: Action("TurnOffLight",lambda world: self.turn_off()), 
            }
        
    def get_possible_actions(self):
        return [self._actions[self._state]]
    
    def turn_on(self):
        logger.debug(f"Turning On light: {self.name}")
        self.set_state(1)
    
    def turn_off(self):
        logger.debug(f"Turning Off light: {self.name}")
        self.set_state(0)
        
    def reset(self):
        self.turn_off()
        
class HomeBuilder:
    
    class InteractiveHome:
        
        def __init__(self,devices,name) :
            self.name = name
            self._devices = devices
        
        def interact(self,action):
            action.run(self)
            
        def get_state(self):
            states = "-".join([str(device.get_state()) for device in self._devices])
            return states
        
        def get_possible_actions(self):
            actions = [] 
            for device in self._devices:
                actions.extend(device.get_possible_actions())
                
            return actions
        
        def reset(self):
            for device in self._devices:
                device.reset()

        def display(self):
            
            logger.debug(f"Devices states : {self.get_state()}")
            logger.debug(f"Possible acions : {self.get_possible_actions()}")
    
    def __init__(self,name):
        self.name = name
        self._devices = []
    
    def with_device(self,device:IoTDevice):
        assert device.name
        logger.debug(f"Adding device {device}")
        self._devices.append(device)
        return self
        
    def build(self) -> InteractiveHome:
        return HomeBuilder.InteractiveHome(self._devices,self.name)
