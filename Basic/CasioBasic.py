
def exec():
    return 'Ù'

def pr(txt):
    return '"' + txt + '"'

def assign(var, val):
    return val.upper() + "ã" + var.upper()

def rd(var):
    return assign(var, "?")

def l(*words):
    return ' '.join(words)

def main(*lines):
    return (exec() + '\n').join(lines) + exec()


if __name__ == '__main__':
    prgrm = main(
        pr("hello user!"),
        rd("A"),
        assign("B", "55"),
        assign("C", "A+B"),
        "C"
    )
    print(prgrm.upper())

    with open("Output.txt", "w") as text_file:
        text_file.write(prgrm)