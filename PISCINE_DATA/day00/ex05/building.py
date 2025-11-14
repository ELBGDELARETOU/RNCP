import sys


def main():
    """Elle fait ce que le sujet demande."""
    assert len(sys.argv) < 3
    if len(sys.argv) < 2:
        text = input("I BEG U PROVIDE ME A STRING : ")
    else:
        text = sys.argv[1]
    spaces = 0
    punctuation_marks = 0
    upper_letters = 0
    lower_letters = 0
    digits = 0
    chars = 0
    for char in text:
        chars += 1
        if char == " ":
            spaces += 1
        if char == '.' or char == ',' or char == '-':
            punctuation_marks += 1
        if char.isupper():
            upper_letters += 1
        if char.islower():
            lower_letters += 1
        if char.isdigit():
            digits += 1
    print("The text contains", chars, "characters:")
    print(upper_letters, " upper letters")
    print(lower_letters, " lower letters")
    print(punctuation_marks, " punctuation marks")
    print(spaces, " spaces")
    print(digits, " digits")
    print(main.__doc__)


main()
