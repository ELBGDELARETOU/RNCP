import sys

def sos(str):
    morse = {
        "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
        "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
        "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
        "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
        "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
        "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
        "Y": "-.--",  "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.", " ": "/"
    }
    code = []
    for key in str.upper():
        if key in morse:
            code.append(morse[key])
    res = " ".join(code)
    print(res)
def main():
    assert len(sys.argv) == 2
    str = sys.argv[1]
    sos(str)

if __name__ == "__main__":
    try:
        main()
    except AssertionError:
        print("AssertionError")