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


def list(i, j):
    return " List" + str(i) + "[" + str(i) + "] "

class List([]):

    @staticmethod
    def alloc(var, length):
        return assign(var, " DimList " + length)

    @staticmethod
    def get(var, i):
        return var + "[" + i + "]"



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
        assign("X", list())
        _while(
            "A=1",
            assign("A", "A+1"),
            pr("A")

        )
    )
    print(prgrm)

    with open("Output.txt", "w") as text_file:
        text_file.write(prgrm)
