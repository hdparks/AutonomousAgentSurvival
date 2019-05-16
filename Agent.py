import numpy as np, numpy.random
from World import World
from scipy.optimize import minimize
from scipy.optimize import LinearConstraint
import autograd.numpy as a_np
from autograd import grad, jacobian

from sympy import solve, Poly, Eq, Function, exp
from sympy.abc import x, y, z, a, b, c

class Agent():
    """
    Represents a household in the cape town crisis that must decide which one of
    three water wells to choose to draw from

    variables:
    dist_params - ndarray (3 x 1) - the parameters of the tri-noulli distribution
    location (x,y): randomly generates a location for the agent
    health (float): Initializes health to 1.

    """

    def __init__(self, dist_params):
        #prior distribution parameters
        self.dist_params = dist_params

        domain = np.linspace(-1.,1.,101)
        self.location = np.array([np.random.choice(domain),np.random.choice(domain)])
        self.health = 1.



    def get_MLE(self, observations):
        """
        Paramters:
        observations - ndarray (n x 3):

        Returns ndarray (n x 3):  most likely parameters given the observations
        """
        # theta_1 = 3
        # theta_2 = 6
        # theta_3 = 12

        # liklihood = lambda x: -(x[0]**theta_1 * x[1]**theta_2 * (x[0] - x[1])**theta_3)
        # liklihood_jac = jacobian(liklihood)
        # x0 = np.ones(3)/3
        # linear_constraint = LinearConstraint([[1, 0], [0, 1]], [0, 0], [np.inf, np.inf])
        # res = minimize(liklihood, x0, method='trust-constr', jac=liklihood_jac,  constraints=[linear_constraint])


    def update_dist_params(self, observations, c):
        """
        c - float - confidence weight of other agents decisions
        observations - ndarray (n x 3)
        """
        m = np.mean(self.observations)
        #update prior to posterior
        self.dist_params = self.dist_params + c*(self.observations/m)
        #normalize
        self.dist_params /= sum(self.dist_params)

    def act(self, correct_well):
        """
            returns highest probable good choice
            This is where we would code up the utility function as well
            Enacts Consequences (such as death if health = 0)
        """
        choice = np.argmax(self.dist_params)

        #update health depending on right or wrong choice
        self.health = self.health - 1./3 if choice != correct_well else 1.

        return choice
