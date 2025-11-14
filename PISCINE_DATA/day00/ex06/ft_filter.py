import sys


def ft_filter(txt, nbr):
    text = txt.split()
    res = []

    big_enough = lambda mot, nbr: len(mot) > nbr
    for mot in text:
        if big_enough(mot, nbr):
            res.append(mot)
    print(res)

def main():
    assert len(sys.argv) == 3
    assert sys.argv[2].isdigit()
    valeur = int(sys.argv[2])
    ft_filter(sys.argv[1], valeur)

if __name__ == "__main__":
    try:
        main()
    except AssertionError:
        print("AssertionError")