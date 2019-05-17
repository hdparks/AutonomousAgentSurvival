from Agent import Agent
import Tools
import numpy as np

class CurrentDay():
    def __init__(self,num_agents):
        self.correct_well = np.random.choice(np.array([0,1,2]))
        self.agent_order = np.arange(num_agents)
        np.random.shuffle(self.agent_order)
        self.index = 0
        self.observations = []



class World():
    """
    Objective of this class is to determine what is the well the water is
    being pumped to and create agents according to the prior type passed in.

    Parameters:
        prior_type ((3,), ndarray): [%uninformed, %informed, %bad]
        correctWell (int): 0, 1, or 2
        wellA (x,y): Tuple of the x- and y-coordinates
        wellB (x,y): Tuple of the x- and y-coordinates
        wellC (x,y): Tuple of the x- and y-coordinates
        population (int): Keeps track of our population numbers
    """



    def __init__(self, agent_type_dist=[1,0,0], people=100):
        """ Initialize the case of Uniform, Unique, Good or Bad
        """
        # establish locations of the wells
        distance = np.linspace(-1,1,101)
        self.wellA = (np.random.random(),np.random.random())
        self.wellB = (np.random.random(),np.random.random())
        self.wellC = (np.random.random(),np.random.random())

        self.population = people

        self.make_agents(agent_type_dist)
        self.start_day()

    def make_agents(self,agent_type_dist):
        self.good = int(self.population * agent_type_dist[1])
        self.bad = int(self.population * agent_type_dist[2])
        self.agent_list = [Agent([1/3,1/3,1/3]) for _ in range(self.population)]

    def update_agent_dist_params(self,correct_well):
        # The first chunk is good
        for agent in self.agent_list[:self.good]:
            agent.set_dist_params(World.create_informed_agent(correct_well))

        for agent in self.agent_list[self.good:self.good + self.bad]:
            agent.set_dist_params(World.create_bad_agent(correct_well))

        for agent in self.agent_list[self.good + self.bad :]:
            agent.set_dist_params(World.create_uninformed_agent())


    def start_day(self):
        self.current_day = CurrentDay(len(self.agent_list))
        self.update_agent_dist_params(self.current_day.correct_well)

    def act(self):
        """ makes the next agent in the list make their choice,
            returns agent_index, choice, whether the day is over or not """
        agent_index = self.current_day.agent_order[self.current_day.index]

        choice = self.agent_list[agent_index].act(self.current_day.observations)

        self.current_day.observations.append(choice)
        self.current_day.index += 1

        day_end = False
        if self.current_day.index == len(self.current_day.agent_order):
            day_end = True
            self.end_day()

        return agent_index, choice, day_end

    def end_day(self):
        obs = np.array(self.current_day.observations)
        dist = [percent_correct(obs,0),
                percent_correct(obs,1),
                percent_correct(obs,2)]
        print("End of day report")
        print(dist * obs.size)
        print(dist)
        self.start_day()

    def create_bad_agent(correct_well):
        dist_params = np.ones(3)
        dist_params[correct_well] = 0
        rand = np.random.random()
        dist_params[dist_params==1] = np.array([rand, 1.-rand])
        return dist_params

    def create_informed_agent(correct_well,low_variance = True):
        """
        Creates a probable informed agent. If variance is low then
        there is a very high chance the agent will have really good info.
        If variance is high, then there is a roughly 50% chance the agent
        will have really good information.

        well_index (int) - 0,1,2 representing the correct well
        """
        well_index = self.correct_well


        a, b = (0, 0)
        dist_params = np.zeros(3)

        #get variables for beta distrb.
        #these effect the variance
        if low_variance:
            a, b = (5, .5)
        #well-informed
        else:
             a, b = (.5, .5)

        #assign infomred probability to the well distr. index
        dist_params[well_index] = np.random.beta(a, b, 1)
        #indicies with corresponding zero entries
        m, = np.where(dist_params == 0)

        #randomly assign other two proabilities
        t = np.random.random(2)
        #make sure they add up to 1 - dist_params[well_index]
        t = (t/np.sum(dist_params)) * (1-dist_params[well_index])
        dist_params[m] = t

        #re-normalize to account for floating point arth. error
        dist_params /= sum(dist_params)

        return dist_params

    def create_uninformed_agent():
        dist_params = np.random.random(3)
        dist_params /= np.sum(dist_params)

        return dist_params
