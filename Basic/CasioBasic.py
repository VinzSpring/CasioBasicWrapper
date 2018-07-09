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
    return "For " + assign(var, _from) + " to " + str(to) + " Step " + str(step) + exec() + \
           exec().join([str(x) for x in lines]) + exec() + "Next" + exec()


def _while(condition, *code):
    return "While " + condition + exec() + exec().join([str(x) for x in code]) + exec() + "WhileEnd" + exec()


if __name__ == '__main__':
    prgrm = main(
        pr("hello user!"),
        rd("A"),
        assign("B", 51),
        assign("C", "A+B"),
        "C",
        _for(
            "A", 1, 100, 1,
            pr("A")
        ),
        _while(
            "A<10",
            assign("A", "A+1"),
            pr("A")

        )
    )
    print(prgrm)

    with open("Output.txt", "w") as text_file:
        text_file.write(prgrm)
