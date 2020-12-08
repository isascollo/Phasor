# Isa Scollo 2020
import math as m
import cmath as c


def print_instructions():
    print("\nRec<->pol converter")
    print("input: >> r,Re,Im   or")
    print("input: >> p,mag,deg")
    print("'q' to quit or 'use' for instructions :)\n")


def valid_input(list):
    try:
        float(list[1])
        float(list[2])
    except (ValueError, IndexError):
        return False
    if list[0] != 'p' and list[0] != 'r':
        return False
    if list[0] == 'p' and float(list[1]) < 0:
        print("mod must be positive value")
        return False
    return True


print_instructions()
while True:
    Re = 0
    Im = 0
    mod = 0
    angle = 0
    inp = input(">> ")
    if "q" in inp:
        break
    if "use" in inp:
        print_instructions()
        continue
    args = list(inp.split(','))
    if valid_input(args):
        if args[0] == 'p':
            mod = float(args[1])
            angle = float(args[2])
            Re = c.rect(mod,m.radians(angle)).real
            Im = c.rect(mod,m.radians(angle)).imag
        if args[0] == 'r':
            Re = float(args[1])
            Im = float(args[2])
            mod = c.polar(complex(Re,Im))[0]
            angle = m.degrees(c.polar(complex(Re,Im))[1])
        if Im >= 0:
            print(f"rec {round(Re,4)} + {round(Im,4)}j")
        else:
            print(f"rec {round(Re,4)} - {round(Im,4)*-1}j")
        print(f"pol {round(mod,4)} ∠{round(angle,4)}°\n")
    else:
        print("Invalid input, try again.\n")
