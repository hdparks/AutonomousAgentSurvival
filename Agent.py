import numpy as np, numpy.random
import Tools

class Agent():
    """
    Represents a household in the cape town crisis that must decide which one of
    three water wells to choose to draw from

    variables:
    dist_params - ndarray ((3,1) array) - the parameters of the tri-noulli distribution
    location (x,y): randomly generates a location for the agent
    health (float): Initializes health to 1.

    """

    def __init__(self, dist_params, world, confidence = 20):
        #prior distribution parameters
        self.dist_params = dist_params
        self.confidence = confidence
        self.location = np.array([np.random.random(),np.random.random()])

        self.dist_to_well = np.array([
            np.linalg.norm(np.array(world.wellA) - self.location),
            np.linalg.norm(np.array(world.wellB) - self.location),
            np.linalg.norm(np.array(world.wellC) - self.location)
        ])

        self.health = 3

    def set_dist_params(self, dist_params):
        self.dist_params = dist_params


    def act(self,observations):
        """
        parameters:
            observations
        """
        observed_dist = np.array([Tools.percent_correct(observations,0),
                                  Tools.percent_correct(observations,1),
                                  Tools.percent_correct(observations,2)])

        n = len(observations)

        post_dist = self.dist_params * self.confidence + n * observed_dist

        return np.argmax( post_dist )
