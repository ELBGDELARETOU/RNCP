import pandas as pd
import matplotlib.pyplot as plt


def load(path: str):
    try:
        data = pd.read_csv(path) 
        print("Loading dataset of dimensions:", data.shape)
        print(data)
        return data
    except OSError:
        print("ERROR FILE NOT FOUND")
        return None
    except ValueError:
        print("ERROR WRONG FORMAT")
        return None

load("population_total.csv")