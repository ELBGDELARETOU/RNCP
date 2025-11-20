def callLimit(limit:int):
    count = 0
    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
           nonlocal count
           if count < limit:
                count += 1
                return function(*args, **kwds)
           else:
               print("limit reached")
               return None
        return limit_function
    return callLimiter 

