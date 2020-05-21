import bonsai_ai as bsa


class InteractiveHomeSimulation:

    pass
    
    

class InteractiveHomeBridge(bsa.Simulator):
    
    def __init__(self,*args):
        
        self.num_episodes = 0
        self.simulation = InteractiveHomeSimulation()
        super().__init__(*args)
        
    def _is_terminal(self):
        """
        We're done either if the AI gets close enough to the target
        state, or if too many steps have passed.
        """
        pass
    
    def _reset_sim(self):
        """
        Reset simulator state before the next training episode.
        """
        pass
    
    def episode_start(self, episode_config):
        """ called at the start of every episode. should
        reset the simulation and return the initial state
        """
        pass
        
    def simulate(self, action):
        """
        Simulate one step. Takes the action from the BRAIN as defined
        in the Inkling file.

        Args:
            action: a dictionary with one key: 'direction_radians'
        Returns:
            (state, reward, terminal) tuple, where state is a dict with keys 
                defined in the Inkling schema
        """
        pass
    
    def _get_state(self):
        """ 
            Gets the state of the simulation, converting it to the form specified in Inkling.
        """
        pass
    
    def _shape_reward(self, current, previous, target):
        """
            Return a reward for approaching the target. Max 1, min -2.
        """
        pass
    
if __name__ == "__main__":
    config = bsa.Config(sys.argv)
    brain = bsa.Brain(config)
    sim = InteractiveHomeBridge(brain, "interact_with_home_sim")
    print('starting...')
    while sim.run():
        continue