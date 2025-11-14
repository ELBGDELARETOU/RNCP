import pandas as pd
import matplotlib.pyplot as plt


def load(path: str):
    try:
        data = pd.read_csv(path)
        
        france = data[data["country"] == "France"].iloc[0, 1:]
        japon = data[data["country"] == "Japan"].iloc[0, 1:]

        annees = data.columns[1:]
        
        plt.figure(figsize=(12, 6))
        
        plt.plot(annees, france, label="France")
        plt.plot(annees, japon, label="Japan")

        annees_affichees = ["1800", "1840", "1880", "1920", "1960", "2000", "2040", "2080"]
        
        plt.xticks(["1800", "1840", "1880", "1920", "1960", "2000", "2040", "2080"])
        plt.yticks(range(0, 101, 10))        
        min_y = int(france.min()//10*10)
        max_y = int(france.max()//10*10 + 10)
        plt.yticks(range(min_y, max_y+1, 10))
        plt.title("Espérance de vie en France")
        plt.xlabel("Année")
        plt.ylabel("Espérance de vie")
        plt.grid(True)
        plt.legend()
        plt.show()
        return data
    except OSError:
        print("ERROR FILE NOT FOUND")
        return None
    except ValueError:
        print("ERROR WRONG FORMAT")
        return None

load("life_expectancy_years.csv")