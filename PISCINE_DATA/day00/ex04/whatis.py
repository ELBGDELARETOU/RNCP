import sys

def whatis(argv):
    if len(sys.argv) != 2:
        print("Wrong number of arguments !")
        return

    try:
        value = int(argv[1])
    except ValueError:
        return print("Wrong argument !")
    
    if (int(sys.argv[1]) % 2) == 0:
        return print("I'm Even.")
    
    return print("I'm Odd.")

whatis(sys.argv)