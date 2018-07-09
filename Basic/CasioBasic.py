def exec():
    return 'Ù\n'


def pr(txt):
    return '"' + txt + '"'


def assign(var, val):
    return str(val).upper() + "ã" + str(var).upper()


def rd(var):
    return assign(var, "?")


def main(*lines, globals=[]):
    return (exec()).join(globals) + exec() + (exec()).join(lines) + exec()


def _if(cond, then, _else):
    cmd = "If " + cond + exec() + then + exec()
    if _else is not None:
        cmd += "\nElse " + _else + exec()
    return cmd


def _for(var, _from, to, step, *lines):
    return "For " + assign(var, _from) + " To " + str(to) + " Step " + str(step) + exec() + \
           exec().join([str(x) for x in lines]) + exec() + "Next"


def _while(condition, *code):
    return "While " + condition + exec() + exec().join([str(x) for x in code]) + exec() + "WhileEnd"


if __name__ == '__main__':
    global_vars = [
        assign("D", 10),
    ]

    prgrm = main(
        pr("hello user!"),
        pr("global vars:"),
        pr("D:"), "D",
        rd("A"),
        pr("A"),
        assign("B", 51),
        assign("C", "A+B"),
        pr("C"),
        "C",
        _for(
            "A", 1, 30, 1,
            "A"
        ),
        assign("A", 1),
        _while(
            "A<10",
            assign("A", "A+1"),
            "A"
        ),

        globals=global_vars
    )
    print(prgrm)

    with open("Output.txt", "w") as text_file:
        text_file.write(prgrm)
