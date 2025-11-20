import csv

def dslr(path):
    with open(path, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        
        data = {col: [] for col in header}
        
        for row in reader:
            for i, value in enumerate(row):
                try:
                    data[header[i]].append(float(value))
                except ValueError:
                    pass
        
        for col, values in data.items():
            if values:
                mean = sum(values) / len(values)
                print(f"{col} : moyenne = {mean}")

dslr("dataset_train.csv")