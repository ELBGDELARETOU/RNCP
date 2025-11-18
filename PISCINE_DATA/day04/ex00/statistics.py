def mean(tmp):
    x = 0
    for val in tmp:
        x += val
    print(x / len(tmp))
    

def median(tmp):
    tmp.sort()
    n = len(tmp)
    mid = n // 2
    print("je suis mid", mid)
    if n % 2 == 0:
        print((tmp[mid - 1] + tmp[mid]) / 2)
        return (tmp[mid - 1] + tmp[mid]) / 2
    else:
        print(tmp[mid])
        return tmp[mid]

def quartile(tmp):
    tmp.sort()
    n = len(tmp)
    lower = tmp[:n//2]
    higer = tmp[(n+1)//2:]
    Q1 = median(lower)
    Q3 = median(higer)
    print("quartile : [", Q1,  Q3, "]" )

def std():
    pass

def var():
    pass


def statistics(*args: any, **kwargs: any)-> None:
    tmp = []
    for ar in args:
        tmp.append(ar)
    for kwg in kwargs:
        if kwg == "mean":
            print(mean(tmp))
        elif kwg == "median":
            median()
        elif kwg == "quartile":
            quartile(tmp)
        elif kwg == "std":
            pass
        elif kwg == "var":
            pass


# mean([1, 42, 360, 11, 64])
# median([1, 42, 360, 11, 64])
quartile([1, 42, 360, 11, 64])