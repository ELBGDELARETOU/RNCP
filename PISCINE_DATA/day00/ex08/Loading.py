def ft_tqdm(lst: range) -> None:
    total = len(lst)
    for i, item in enumerate(lst, start=1):
        percent = i / total * 100

        bar_len = 47
        filled_len = int(bar_len * i // total)
        bar = ("=" * filled_len) + ">" + "-"  * (bar_len - filled_len)
        print(str(int(percent)) + "%" + "[" + bar + "]" + str(i) + "/" + str(total), end="\r")
        yield item