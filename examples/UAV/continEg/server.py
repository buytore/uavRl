import random
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from examples.UAV.gridEg.uavModel import GridModel

def agent_draw(agent):
    portrayal = None
    #print("Uid: {0}, Heading: {1}".format(agent.unique_id, agent.heading))
    portrayal = {"Shape": "arrowHead",
                 "Filled": "true",
                 "Layer": 2,
                 "Color": "green",
                 "Filled": "true",
                 "heading_x": agent.heading[0],
                 "heading_y": agent.heading[1],
                 "text": agent.unique_id,
                 "text_color": "white",
                 "scale": 0.8,
                 }
    return portrayal

def launch_shape_model():
    width = 15
    height = 10
    num_agents = 2
    pixel_ratio = 50

    grid = CanvasGrid(agent_draw, width, height, width * pixel_ratio, height * pixel_ratio)

    server = ModularServer(GridModel, [grid], "UAV Model Example", num_agents, width, height)

    server.port = 8521
    server.launch()

if __name__ == "__main__":
    random.seed(3)
    launch_shape_model()
