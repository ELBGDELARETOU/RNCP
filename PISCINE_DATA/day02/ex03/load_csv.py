import pandas as pd
import matplotlib.pyplot as plt


def load(path: str):
    try:
        data = pd.read_csv(path) 
        print("Loading dataset of dimensions:", data.shape)
        return data
    except OSError:
        print("ERROR FILE NOT FOUND")
        return None
    except ValueError:
        print("ERROR WRONG FORMAT")
        return None

def projection_life(life_file, gdp_file, year="1900"):
    life = load(life_file)
    gdp = load(gdp_file)

    if life is None or gdp is None:
        return
    if year not in life.columns or year not in gdp.columns:
        print("year not found in files")
        return
        
    life_1900 = life[["country", year]] 
    gdp_1900 = gdp[["country", year]]

    merged = pd.merge(life_1900, gdp_1900, on="country", suffixes=("_life", "_gdp"))
    plt.figure(figsize=(12, 6))
    plt.scatter(merged[f"{year}_gdp"], merged[f"{year}_life"], color='red')
    plt.xlabel(f"GDP per person in {year} (PPP)")
    plt.ylabel(f"Life expectancy in {year}")
    plt.title(f"Life expectancy vs GDP per person in {year}")
    plt.show()

projection_life("life_expectancy_years.csv", "income_per_person_gdppercapita_ppp_inflation_adjusted.csv", "1900")