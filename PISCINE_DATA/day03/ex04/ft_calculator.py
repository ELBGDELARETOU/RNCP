class calculator:

    def dotproduct(V1: list[float], V2:list[float])-> None:
        x = 0
        for v1, v2 in zip(V1, V2):
            x += v1 * v2
        print(x)
        return x    
    
    def add_vec(V1: list[float], V2:list[float])-> None:
        tmp = []
        for v1, v2 in zip(V1, V2):
            tmp.append(v1 + v2)
        tmp = [float(x) for x in tmp]
        print(tmp)
        return tmp
    
    def sous_vec(V1: list[float], V2:list[float])-> None:
        tmp = []
        for v1, v2 in zip(V1, V2):
            tmp.append(v1 - v2)
        tmp = [float(x) for x in tmp]
        print(tmp)
        return tmp
