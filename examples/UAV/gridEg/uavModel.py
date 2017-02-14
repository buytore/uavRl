import random
from mesa import Model, Agent
from mesa.space import SingleGrid, MultiGrid
from mesa.time import RandomActivation

#######################################################################################################
####  Build AGENT
#######################################################################################################
class Walker(Agent):
    def __init__(self, unique_id, model, pos, heading=(1, 0)):
        super().__init__(unique_id, model)
        self.pos = pos
        self.heading = heading
        self.headings = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def rotateAgent(self):
        print("Mark's great")

    def move(self):
        xValue = self.pos[0] + self.heading[0]
        yValue = self.pos[1] + self.heading[1]
        if (xValue > 14) or (xValue < 0) or (yValue > 9) or (yValue < 0):
            self.rotateAgent()
        else:
            possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
            new_position = random.choice(possible_steps)
            self.model.grid.move_agent(self, new_position)

    def step(self):
        self.move()

    def rotateAgent(self):
        print("Agent: " + str(self.unique_id) + " is heading " + str(self.heading) + " at " + str(self.pos))
        count = 0
        for headingInd in self.headings:
            if headingInd == self.heading:
                ind = count
                if ind < len(self.headings)-1:
                    self.heading = self.headings[ind + 1]
                    break
                else:
                    self.heading = self.headings[0]
                    break
            count += 1
        print("Agent: " + str(self.unique_id) + " is now heading " + str(self.heading))



#######################################################################################################
####  Build MODEL - grid environment
#######################################################################################################
class GridModel(Model):
    def __init__(self, N, width=20, height=10):
        self.running = True
        self.N = N    # num of agents
        self.headings = ((1, 0), (0, 1), (-1, 0), (0, -1))  # tuples are fast
        self.grid = MultiGrid(width, height, torus=False)
        self.schedule = RandomActivation(self)
        self.make_walker_agents()

    def make_walker_agents(self):
        unique_id = 0
        while True:
            if unique_id == self.N:
                break
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            pos = (x, y)
            heading = random.choice(self.headings)
            # heading = (1, 0)
            if self.grid.is_cell_empty(pos):
                print("Creating agent {2} at ({0}, {1})".format(x, y, unique_id))
                a = Walker(unique_id, self, pos, heading)
                self.schedule.add(a)
                self.grid.place_agent(a, pos)
                unique_id += 1


    def step(self):
        self.schedule.step()