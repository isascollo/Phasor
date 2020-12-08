# Isa Scollo 2020
import math


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


sign = lambda x: x and (1, -1)[x < 0]
constrain = lambda x: x-360*sign(x) if abs(x) > 180 else x


print_instructions()
while True:
    real = 0
    complex = 0
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
            real = mod*math.cos(angle*math.pi/180)
            complex = mod*math.sin(angle*math.pi/180)
        if args[0] == 'r':
            real = float(args[1])
            complex = float(args[2])
            if real != 0:
                angle = math.atan(complex/real)*180/math.pi
            else:
                angle = 90*sign(complex)
            if real < 0:
                angle -= 180;
            mod = math.sqrt(real*real + complex*complex)
        angle = constrain(angle)
        if complex >= 0:
            print(f"rec {round(real,4)} + {round(complex,4)}j")
        else:
            print(f"rec {round(real,4)} - {round(complex,4)*-1}j")
        print(f"pol {round(mod,4)} ∠{round(angle,4)}°\n")
    else:
        print("Invalid input, try again.\n")
