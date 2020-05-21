import sys
import logging
import bonsai_ai as bsa
from model import FakeLight ,HomeBuilder
from subject import Daddy

console = logging.StreamHandler()
logger = logging.Logger(__name__,logging.DEBUG)
logger.addHandler(console)

class InteractiveHomeSimulation:

    def __init__(self):
        self._home = self._build_home()
        self.lastAction = 0
        self.currentState = 0
        self.comfort = 0
        
    def reset(self):
        self._home.reset()
        
    def get_home_state(self):
        return self._home.get_state()
    
    def do_all_actions(self,actions_map):
        
        for device_name,action_type in actions_map.items():
            self._home.do_action(device_name,action_type)
            
    def get_subjects_comfort(self):
        return self._home.get_comfor()
    
    def _build_home(self):
        
        config = HomeBuilder("Tony Stark Home")
        topLight = FakeLight("topLight",consumption=100)    
        floorLight = FakeLight("bottomLight",consumption=200)
        leftLight = FakeLight("leftWallLight",consumption=20)
        rightLight = FakeLight("rightWallLight",consumption=100)
        subject = Daddy()
        
        return config \
            .with_device(topLight) \
            .with_device(floorLight)\
            .with_device(leftLight)\
            .with_device(rightLight)\
            .with_subject(subject) \
            .build()

class InteractiveHomeBridge(bsa.Simulator):
    
    def __init__(self,*args):
        
        self.num_episodes = 0
        self.simulation = InteractiveHomeSimulation()
        self._statesMap = {}
        super().__init__(*args)
        
    def _is_terminal(self):
        """
        We're done either if the AI gets close enough to the target
        state, or if too many steps have passed.
        """
        return False
    
    def _reset_sim(self):
        """
        Reset simulator state before the next training episode.
        """
        pass

    
    def episode_start(self, episode_config):
        """ called at the start of every episode. should
        reset the simulation and return the initial state
        """
        self._reset_sim()
        return self._get_state()

        
    def simulate(self, actions):
        """
        Simulate one step. Takes the action from the BRAIN as defined
        in the Inkling file.

        Args:
            action: a dictionary with action key values
        Returns:
            (state, reward, terminal) tuple, where state is a dict with keys 
                defined in the Inkling schema
        """
        logger.debug(f"Simulation actions: {actions}")
        self.simulation.do_all_actions(actions)
        reward = self.reward_shaped()
        state = self._get_state()
        terminal = self._is_terminal()
        
        logger.debug(f"Reward : {reward} , New State:{state}")
        return (state, reward, terminal)
    

    def _get_state(self):
        """ 
            Gets the state of the simulation, converting it to the form specified in Inkling.
        """
        state =  self.simulation.get_home_state()
        state = self._get_numeric_state_from(state)
        
        return {
            
                "currentState": state,
                "comfort": self.simulation.comfort,
                "lastAction":self.simulation.lastAction
        }
    
    def _shape_reward(self):
        """
            Return a reward for approaching the target. Max 1, min -2.
        """
        return 0
    
    def reward_shaped(self):
        """Reward for approaching target"""
        return self.simulation.get_subjects_comfort()
    
    def _get_numeric_state_from(self,state):
        
        if state not in self._statesMap:
            self._statesMap[state] = len(self._statesMap)
        return self._statesMap[state]
    
if __name__ == "__main__":
    
    logger.info('starting...')
    config = bsa.Config(sys.argv)
    brain = bsa.Brain(config)
    sim = InteractiveHomeBridge(brain, "home_sim")
    while sim.run():
        continue