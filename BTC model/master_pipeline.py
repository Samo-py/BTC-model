import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pipelines.pipeline_C import pipeline_C
from pipelines.pipeline_B import pipeline_B
from pipelines.pipeline_D import pipeline_D
from pipelines.pipeline_A import pipeline_A
from pipelines.loader_A import loader



class Pipeline:
    def __init__(self):
        pass

    def run(self):
        pass


class Visualizer:
    def __init__(self):
        pass

    def compute(self):
        pass

    def visualize(self):
        pass

def master_pipeline():
    pipeline = Pipeline(loader(), pipeline_A(), pipeline_B(), pipeline_C(), pipeline_D()).run()
    visualizer = Visualizer(pipeline).compute()
    visualizer.visualize()
 

