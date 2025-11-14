def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    assert len(height) == len(weight)
    
    bmi_list = []
    for h, w in zip(height, weight):
        bmi = w / (h ** 2)
        bmi_list.append(bmi)
    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    res = []
    for b in bmi:
        if b < limit:
            res.append(False)
        else:
            res.append(True)
    return res