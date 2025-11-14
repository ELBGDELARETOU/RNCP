def slice_me(family: list, start: int, end: int) -> list:
    print("My shape is :", "(" , len(family), "," ,len(family[0]) , ")")
    new_list = family[start:end]
    print("My new shape is :", "(", len(family[start:end]),",", len(family[start]), ")")
    print(new_list)

family = [[1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]]
slice_me(family, 0, 2)
slice_me(family, 1, -2)