def ft_mean(lst):
    try: 
        x = 0
        for val in lst:
            x += val
        print(x / len(lst))
    except:
        print("ERROR")

def median(lst):
    try:
        lst.sort()
        n = len(lst)
        mid = n // 2
        if n % 2 == 0:
            print (lst[mid - 1] + lst[mid]) / 2
        else:
            print (lst[mid])
    except:
        print("ERROR")

def quartile(lst):
    try:
        lst.sort()
        n = len(lst)
        Q1 = lst[int(0.25 * (n-1))]
        Q3 = lst[int(0.75 * (n-1))]
        res = [float(Q1), float(Q3)]
        print("quartile :", res)
    except:
        print("ERROR")

def std(lst):
    try:
        count = len(lst)
        x = 0
        for val in lst:
            x += val
        mean = x / count
        sq_diff_sum = 0

        for x in lst:
            diff = x - mean
            sq_diff_sum += diff * diff
        variance = sq_diff_sum / count

        def sqrt(number):
            approx = number / 2
            for _ in range(20):
                approx = (approx + number / approx) / 2
            return approx
        print("std :", sqrt(variance))
    except:
        print("ERROR")
    
def var(lst):
    try:
        res = 0
        x = 0
        for val in lst:
            x += val
        mean = x / len(lst)
        for num in lst:
            res += (num - mean)**2
        print("var :", res / len(lst))
    except:
        print("ERROR")

def ft_statistics(*args: any, **kwargs: any)-> None:
    lst = []
    for num in args:
        lst.append(num)
    for kwg, value in kwargs.items():
        if value == "mean":
            ft_mean(lst)
        elif value == "median":
            median(lst)
        elif value == "quartile":
            quartile(lst)
        elif value == "std":
            std(lst)
        elif value == "var":
            var(lst)
