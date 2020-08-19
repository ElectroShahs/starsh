
from os.path import split, splitext

code = ""


def read_file(filename):
    f = splitext(filename)
    if f[1] == ".stsh":
        with open(filename, "r") as f:
            content = f.read()
            return content
    else: 
        raise Exception("Please only run the filename with .stsh extension.")


def evaluate(code):
    code = cleanup(code)
    out = []

    brac1 = 0
    brac2 = 0

    stack = 0
    temp = False
    mode = False

    debug = False

    for i in code:
        if i == "(":
            mode = True
        elif i == ")":
            if not temp:
                mode = False
                temp = True
            elif temp:
                mode = False
                temp = False
                stack = stack + (brac1 * brac2)
                brac1 = 0
                brac2 = 0
        elif mode and not temp:
            if i == "*":
                brac1 += 1
            elif i == "!":
                brac1 -= 1
            elif i == "-" and not debug:
                out.append(chr(stack))
            elif debug:
                out.append(stack)
        elif mode and temp:
            if i == "*":
                brac2 += 1
            elif i == "!":
                brac2 -= 1
            elif i == "-" and not debug:
                out.append(chr(stack))
            elif debug:
                out.append(stack)
        elif not mode:
            if i == "*":
                stack += 1
            elif i == "!":
                stack -= 1
            elif i == "0":
                stack = 0
            elif i == "-" and not debug:
                out.append(chr(stack))
            elif debug:
                out.append(stack)

    return ''.join(out)


def cleanup(code):
    clean_code = [i for i in code if i in ["!", "*", "-", "(", ")", "0"]]
    return clean_code


def main():
    filename = "test.stsh" # Edit this to whatever file name you have, please have the same extension
    code = read_file(filename)
    out = evaluate(code)
    print(out)


if __name__ == "__main__": main()