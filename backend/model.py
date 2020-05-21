import logging
from abc import ABC, abstractmethod

console = logging.StreamHandler()
logger = logging.Logger(__name__,logging.DEBUG)
logger.addHandler(console)

class IoTDevice(ABC):
    
    def __init__(self,name):
        self.name = name
        self._state = None
    
    @abstractmethod
    def get_possible_actions(self):
        pass

    def get_state(self):
        return self._state
    
    def set_state(self,state_value):
        self._state = state_value

class FakeLight(IoTDevice):
    
    def __init__(self,name):
        super().__init__(name)
        self._actions = {0: self.turn_on, 1:self.turn_off}
        
    def get_possible_actions(self):
        return [self._actions[self._state]]
    
    def turn_on(self):
        logger.debug(f"Turning On light of :  {self.name}")
        self.set_state(1)
    
    def turn_off(self):
        logger.debug(f"Turning Off light of : {self.name}")
        self.set_state(0)