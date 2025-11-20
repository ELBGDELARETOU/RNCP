import csv


def training():
    theta0 = 0.0
    theta1 = 0.0
    alpha = 0.01
    iterations = 10000

    mileages = []
    prices = []

    with open('data.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            mileages.append(float(row[0]))
            prices.append(float(row[1]))

    max_mileage = max(mileages)
    max_price = max(prices)

    mileages = [m / max_mileage for m in mileages]
    prices = [p / max_price for p in prices]

    m = len(mileages)

    for _ in range(iterations):
        sum0 = 0
        sum1 = 0
        for i in range(m):
            prediction = theta0 + theta1 * mileages[i]
            error = prediction - prices[i]
            sum0 += error
            sum1 += error * mileages[i]

        theta0 -= alpha * (sum0 / m)
        theta1 -= alpha * (sum1 / m)

    return theta0 , theta1, max_mileage, max_price

def prevision():
    try:
        mileage = int(input("Enter the mileage of your car please ... "))
        theta0, theta1, max_mileage, max_price = training()
        mileage_norm = mileage / max_mileage
        pred_norm = theta0 + (theta1 * mileage_norm)
        estimated_price = pred_norm * max_price
        print("Here is your estimated price :", estimated_price)
    except ValueError:
        print("Please enter a valide mileage !") 

prevision()