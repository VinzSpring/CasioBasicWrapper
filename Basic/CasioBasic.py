def exec():
    return 'Ù\n'


def pr_txt(txt):
    return '"' + txt + '"'


def pr_var(var):
    return str(var) + "Ø"


def assign(var, val):
    return str(val) + "ã" + str(var)


def rd(var):
    return assign(var, "?")


def main(*lines, globals=[]):
    return (exec()).join(globals) + exec() + (exec()).join(lines) + exec()


def _if(cond, then, _else):
    cmd = "If " + cond + exec() + then + exec()
    if _else is not None:
        cmd += "\nElse " + _else + exec()
    return cmd + exec() + "IfEnd"


def _for(var, _from, to, step, *lines):
    return "For " + assign(var, _from) + " To " + str(to) + " Step " + str(step) + exec() + \
           exec().join([str(x) for x in lines]) + exec() + "Next"


def _while(condition, *code):
    return "While " + condition + exec() + exec().join([str(x) for x in code]) + exec() + "WhileEnd"


def div(a, b):
    return "(" + str(a) + ")»(" + str(b) + ")"


def square(a):
    return a + "’"


def alloc_list(list_num, length):
    return assign("Dim List " + str(list_num), length)


def alloc_matrix(mat_name, i, j):
    return assign("Dim Mat " + mat_name, "{" + str(i) + "," + str(j) + "}")

def mult(a, b):
    return str(a) + "À" + str(b)

def clear(var):
    return assign(var, 0)

def logab(a, b):
    return "log a(b)" + str(a) + "," + str(b) + ")"


if __name__ == '__main__':
    global_vars = [
        assign("D", 10),
    ]

    prgrm = main(
        pr_txt("hello user!"),
        pr_txt("global vars:"),
        pr_txt("D:"), pr_var("D"),

        alloc_matrix("A", 2, 2),
        pr_var("Mat A"),

        alloc_list(1, 10),
        pr_var("List 1"),

        rd("A"),
        assign("B", 51),
        assign("C", "A+B"),
        pr_var("C"),
        _for(
            "A", 1, 30, 1,
            pr_var("A")
        ),
        assign("A", 1),
        _while(
            "A<10",
            assign("A", "A+1"),
            pr_var("A")
        ),

        globals=global_vars
    )

    entropy = main(
        pr_txt("Entropy"),

        pr_txt("sub intervals:"),
        rd("C"),
        pr_txt("N:"),
        rd("N"),
        #sum
        clear("A"),
        clear("B"),
        _for(
            "I", 0, "N-1", 1,
            pr_txt("enter p(i):"),
            rd("A"),
            assign("B", "B+" + mult(div("A", "C"), logab(2, div("C", "A"))))
        ),

        pr_var("B"),
    )

    print(entropy)